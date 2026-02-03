<div align="center">

# 🌾 Smart Crop Advisory System  
### AI Powered Crop Recommendation Platform for Farmers  

🚜 Machine Learning | 🌦 Live Weather API | 🌱 Soil Intelligence | 📍 Location Based  

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Web_Framework-green)
![ML](https://img.shields.io/badge/Machine_Learning-RandomForest-orange)
![Status](https://img.shields.io/badge/Project-Capstone-success)

</div>

---

## 🌟 Project Overview  

**Smart Crop Advisory System** is an AI-driven agriculture decision support platform that helps farmers choose the **best crop to grow** based on:

- 🌦 Real-time Weather Conditions  
- 🌱 Soil Nutrient Estimation (NPK + pH)  
- 📍 Location-Based Data  
- 🤖 Machine Learning Prediction Model  

👉 Farmers only need to **enter their village or city name** — the system automatically fetches environmental data and provides **top crop recommendations with confidence score**.

---

## 🎯 Problem Statement  

Farmers often face challenges due to:

- Climate variability  
- Lack of soil testing facilities  
- Guess-based crop selection  
- Poor yield planning  

This system solves these issues by offering **data-driven intelligent crop recommendations**.

---

## 🚀 Key Features  

✅ Live City/Village Search  
✅ Automatic Weather Data Fetching  
✅ Soil Nutrient Estimation  
✅ Machine Learning Based Crop Prediction  
✅ Top 3 Crop Recommendations with Confidence  
✅ Farmer Friendly UI  
✅ REST API Based Architecture  
✅ Modular Backend Design  

---

## 🧠 Machine Learning Model  

### Algorithm Used  
✔ Random Forest Classifier  

### Input Parameters  

| Feature | Description |
--------|------------
Nitrogen (N) | Soil Nitrogen Content  
Phosphorus (P) | Soil Phosphorus Content  
Potassium (K) | Soil Potassium Content  
Temperature | Current Temperature  
Humidity | Atmospheric Humidity  
Rainfall | Weather Rainfall  
pH | Soil Acidity Level  

### Output  

🎯 Recommended Crop Label  

---

## 🏗 System Architecture  

User Location Input
↓
Geocoding API
↓
Weather API + Soil Estimation
↓
Feature Processing
↓
ML Prediction Engine
↓
Crop Recommendation Output


---

## 📂 Project Folder Structure  

smart-crop-advisory-system
│
├── backend
│ ├── routes
│ ├── services
│ ├── utils
│ └── app.py
│
├── model
│ ├── train_model.py
│ └── crop_model.pkl
│
├── dataset
│ └── Crop_recommendation.csv
│
├── frontend
│ ├── static
│ └── templates
│
├── .env
├── requirements.txt
└── README.md


---

## 🛠 Tech Stack  

### Frontend  
- HTML  
- CSS  
- JavaScript  

### Backend  
- Python  
- Flask REST API  

### Machine Learning  
- Scikit-learn  
- Pandas  
- NumPy  

### APIs Used  
- OpenWeatherMap API  
- OpenStreetMap Geocoding API  

---

## 📊 Dataset Information  

The model is trained using **Crop Recommendation Dataset** which contains:

- Soil Nutrient Values  
- Weather Parameters  
- Crop Labels  

Dataset Source: Kaggle  

---

## ⚙ Installation & Setup  

### 🔹 Step 1 — Clone Repository  

```bash
git clone https://github.com/yourusername/smart-crop-advisory-system.git
cd smart-crop-advisory-system
🔹 Step 2 — Create Virtual Environment
python -m venv venv
Activate:

Windows:

venv\Scripts\activate
Linux/Mac:

source venv/bin/activate
🔹 Step 3 — Install Dependencies
pip install -r requirements.txt
🔹 Step 4 — Add API Key
Create .env file:

OPENWEATHER_API_KEY=your_api_key_here
🔹 Step 5 — Train Model (Optional)
python model/train_model.py
🔹 Step 6 — Run Application
python -m backend.app
Open browser:

http://127.0.0.1:5000
🧪 How System Works
1️⃣ User enters location
2️⃣ System fetches latitude & longitude
3️⃣ Weather API provides real-time data
4️⃣ Soil data is estimated
5️⃣ ML model predicts crops
6️⃣ Top 3 crops displayed with confidence

📸 Application Preview
🟢 Location Search
🟢 Crop Recommendation Dashboard
🟢 Weather & Soil Information Panel

(Add screenshots here for GitHub visual impact)

⚠ Disclaimer
Soil parameters are estimated using public datasets.
This system is designed for educational and advisory purposes only.

👨‍💻 Developer
Shubham Shrivastava
🎓 B.Tech Computer Science Engineering
📌 Capstone Project – Smart Agriculture Domain

🌱 Future Enhancements
🚀 Crop Disease Detection
🚀 Yield Prediction System
🚀 Fertilizer Recommendation Engine
🚀 Mobile App Version
🚀 Regional Language Support
🚀 AI Chatbot for Farmers

⭐ Support This Project
If you found this project useful:

⭐ Star this repository
🍴 Fork for contributions
📢 Share with others

📄 License
This project is licensed under MIT License.

<div align="center">
🌾 Empowering Farmers With Artificial Intelligence 🚜
Made with ❤️ for Smart Agriculture
</div> ```
