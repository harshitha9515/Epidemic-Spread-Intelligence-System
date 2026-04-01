🦠 Epidemic Spread Intelligence System

An AI-powered epidemic analytics and forecasting platform built using Streamlit, Python, Plotly, and LLM intelligence.
The system analyzes epidemic datasets, visualizes disease spread, predicts future trends, and generates policy recommendations to support data-driven public health decisions.

🚀 Features

✅ Upload epidemic datasets (Excel format)

✅ Interactive data visualization dashboards

✅ Epidemic curve & growth rate analysis

✅ Region-wise outbreak monitoring

✅ AI-powered spread analysis using LLM

✅ Future case prediction & forecasting

✅ Intervention impact analysis

✅ Automated epidemic report generation

🛠️ Tech Stack
Frontend/UI: Streamlit

Backend: Python

Data Processing: Pandas, NumPy

Visualization: Plotly

AI Integration: Groq LLM (Llama3 / Mixtral)

File Handling: OpenPyXL

📂 Project Structure
Epidemic-Spread-Intelligence/
│

├── app.py                # Main Streamlit application

├── requirements.txt      # Dependencies

├── README.md             # Project documentation

└── sample_data.xlsx      # Test dataset (optional)

⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/your-username/Epidemic-Spread-Intelligence.git
cd Epidemic-Spread-Intelligence

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate     # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

Or install manually:

pip install streamlit pandas numpy plotly openpyxl requests
🔑 API Configuration

This project uses Groq LLM API.

Create an account at Groq
Generate API Key
Replace in app.py:
GROQ_API_KEY = "YOUR_API_KEY"

⚠️ Never upload real API keys to GitHub.

▶️ Run the Application
streamlit run app.py

Open browser:

http://localhost:8501

📊 Dataset Format

Upload an Excel file containing columns like:

Column	Description
date	Date of record
region	Geographic region
new_cases	Daily reported cases
deaths	Daily deaths
recoveries	Recoveries count
r_effective	Reproduction number (optional)

📈 System Modules

📊 Input Data
Dataset preview
Summary statistics

📈 Spread Model
Epidemic curve visualization
Growth rate analysis
Regional comparison

🔮 Predictions
Future case forecasting
Confidence intervals

💊 Interventions
Intervention effectiveness analysis
Policy recommendations (AI)

📋 Report
Automated epidemic intelligence report

🧠 AI Capabilities

The system uses Large Language Models to:

Analyze outbreak severity
Detect spread patterns
Recommend interventions
Generate policy insights
Produce final analytical reports

🌟 Future Improvements
Real-time API data integration
Advanced ML forecasting models
Hospital resource prediction
Geo-map visualization
Multi-disease tracking

📜 License

This project is for educational and research purposes.

👨‍💻 Author

Developed as an AI-based epidemic monitoring and intelligence system using modern data analytics and LLM technologies.
