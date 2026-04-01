import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import requests

# Page configuration
st.set_page_config(page_title="Epidemic Spread Intelligence", layout="wide")

# Initialize session state
if 'data' not in st.session_state:
    st.session_state.data = None
if 'results' not in st.session_state:
    st.session_state.results = None

# API Configuration
GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"


# ---------------- LLM ----------------
def query_llm(prompt, model="llama3-70b-8192"):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
        "max_tokens": 1000
    }

    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=data)
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"API Error: {str(e)}"


# ---------------- DATA PROCESS ----------------
def process_epidemic_data(df):

    if 'new_cases' in df.columns:
        cases_col = 'new_cases'
    elif 'cases' in df.columns:
        cases_col = 'cases'
    else:
        return None

    total_cases = df[cases_col].sum()
    avg_daily = df[cases_col].mean()
    peak_cases = df[cases_col].max()

    if len(df) > 1:
        df['growth_rate'] = df[cases_col].pct_change() * 100

    return {
        'total_cases': total_cases,
        'avg_daily': avg_daily,
        'peak_cases': peak_cases,
        'duration': len(df),
        'max_growth': df['growth_rate'].max() if 'growth_rate' in df.columns else 0,
        'cases_col': cases_col
    }


# ---------------- PREDICTION ----------------
def generate_predictions(df, days=30):

    if 'new_cases' not in df.columns or 'date' not in df.columns:
        return None

    df['date'] = pd.to_datetime(df['date'])

    last_cases = df['new_cases'].iloc[-1]
    avg_growth = df['new_cases'].pct_change().mean()

    last_date = df['date'].iloc[-1]

    future_dates = [last_date + timedelta(days=i) for i in range(1, days+1)]
    predicted_cases = [last_cases * (1 + avg_growth) ** i for i in range(1, days+1)]

    return pd.DataFrame({'date': future_dates, 'predicted_cases': predicted_cases})


# ---------------- UI ----------------
st.title("🦠 Epidemic Spread Intelligence System")
st.markdown("---")

with st.sidebar:

    st.header("📁 Data Input")
    uploaded_file = st.file_uploader("Upload Excel file", type=['xlsx', 'xls'])

    if uploaded_file:
        try:
            df = pd.read_excel(uploaded_file)

            # ✅ FIX: normalize column names
            df.columns = df.columns.str.strip().str.lower()

            st.session_state.data = df

            st.success("✅ File loaded successfully!")
            st.write("Preview:", df.head())
            st.write("Columns:", list(df.columns))

        except Exception as e:
            st.error(f"Error: {e}")

    st.markdown("---")
    st.header("⚙️ Settings")

    model_choice = st.selectbox(
        "Select Model",
        ["llama3-70b-8192", "llama3-8b-8192", "mixtral-8x7b-32768"]
    )

    prediction_days = st.slider("Prediction Days", 7, 90, 30)

    if st.session_state.data is not None and 'region' in st.session_state.data.columns:
        selected_region = st.selectbox(
            "Select Region",
            ["All"] + list(st.session_state.data['region'].unique())
        )
    else:
        selected_region = "All"


# ---------------- FILTER ----------------
if st.session_state.data is not None:
    if selected_region != "All":
        filtered_df = st.session_state.data[
            st.session_state.data['region'] == selected_region
        ].copy()
    else:
        filtered_df = st.session_state.data.copy()
else:
    filtered_df = None


# ---------------- TABS ----------------
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["📊 Input Data", "📈 Model Spread", "🔮 Predictions", "💊 Interventions", "📋 Report"]
)

# ================= TAB 1 =================
with tab1:
    if filtered_df is not None:
        st.header("Input Data Overview")
        st.dataframe(filtered_df, use_container_width=True)
        st.subheader("Data Summary")
        st.write(filtered_df.describe())
    else:
        st.info("👈 Please upload an Excel file to begin")

# ================= TAB 2 =================
with tab2:
    if filtered_df is not None and 'new_cases' in filtered_df.columns:
        fig = px.line(filtered_df, x='date', y='new_cases',
                      title=f"Epidemic Curve - {selected_region}",
                      markers=True)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Please upload data first")

# ================= TAB 3 =================
with tab3:
    if filtered_df is not None:
        predictions = generate_predictions(filtered_df, prediction_days)

        if predictions is not None:
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=filtered_df['date'],
                y=filtered_df['new_cases'],
                mode='lines+markers',
                name='Historical'
            ))
            fig.add_trace(go.Scatter(
                x=predictions['date'],
                y=predictions['predicted_cases'],
                mode='lines+markers',
                name='Predicted'
            ))
            st.plotly_chart(fig, use_container_width=True)

# ================= TAB 4 =================
with tab4:
    if filtered_df is not None:
        st.write("Intervention analysis ready.")

# ================= TAB 5 =================
with tab5:
    if filtered_df is not None:
        stats = process_epidemic_data(filtered_df)
        st.write(stats)

st.markdown("---")
st.markdown("🔬 Epidemic Spread Intelligence System v2.0 | Powered by Groq LLM")
