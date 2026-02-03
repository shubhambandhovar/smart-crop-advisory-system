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

**Smart Crop Advisory System** is an AI-driven agriculture decision support platform that helps farmers choose the **best crop to grow** based on real-time environmental conditions.

The system automatically fetches weather and soil-related data using APIs and combines it with a trained Machine Learning model to provide accurate crop recommendations.

Farmers only need to **enter their village or city name** — the system handles the rest.

---

## 🎯 Problem Statement  

Farmers often struggle with crop planning due to unpredictable climate, lack of soil testing facilities, and dependency on traditional guess-based methods.

This project solves this problem by offering **data-driven intelligent crop recommendations** that improve productivity and promote sustainable farming.

---

## 🚀 Key Features  

✅ Live City/Village Search with Suggestions  
✅ Automatic Weather Data Fetching  
✅ Soil Nutrient Estimation (NPK + pH)  
✅ Machine Learning Based Crop Prediction  
✅ Top 3 Crop Recommendations with Confidence Score  
✅ Farmer Friendly Dashboard UI  
✅ REST API Based Backend Architecture  
✅ Modular Code Structure  

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

```
User Location Input
        ↓
Geocoding API
        ↓
Weather API + Soil Estimation
        ↓
Feature Processing
        ↓
Machine Learning Prediction Engine
        ↓
Crop Recommendation Output
```

---

## 🛠 Technology Stack  

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

The Machine Learning model is trained using the **Crop Recommendation Dataset** containing:

- Soil Nutrient Parameters  
- Weather Conditions  
- Crop Labels  

Dataset Source: Kaggle  

---

## ⚙ Installation & Setup  

### Step 1 — Clone Repository  

```bash
git clone https://github.com/yourusername/smart-crop-advisory-system.git
cd smart-crop-advisory-system
```

---

### Step 2 — Create Virtual Environment  

```bash
python -m venv venv
```

Activate:

Windows:
```bash
venv\Scripts\activate
```

Linux/Mac:
```bash
source venv/bin/activate
```

---

### Step 3 — Install Dependencies  

```bash
pip install -r requirements.txt
```

---

### Step 4 — Add API Key  

Create `.env` file in root folder:

```
OPENWEATHER_API_KEY=your_api_key_here
```

---

### Step 5 — Train Machine Learning Model  

```bash
python model/train_model.py
```

---

### Step 6 — Run Flask Application  

```bash
python -m backend.app
```

Open browser:

```
http://127.0.0.1:5000
```

---

## 🧪 How The System Works  

1️⃣ User enters village or city  
2️⃣ System fetches location coordinates  
3️⃣ Weather API provides live data  
4️⃣ Soil data is estimated  
5️⃣ ML model predicts best crops  
6️⃣ Top 3 crops displayed with confidence  

---

## 📸 Application Interface  

The application provides:

✔ Location Search Bar  
✔ Crop Recommendation Cards  
✔ Confidence Percentage Bars  
✔ Weather Information Panel  
✔ Soil Nutrient Display  

---

## ⚠ Disclaimer  

Soil parameters are estimated using public datasets and satellite-based averages.  
This platform is intended for **educational and advisory purposes only**.

---

## 👨‍💻 Developer  

### Shubham Shrivastava  
🎓 B.Tech Computer Science Engineering  
📌 Capstone Project – Smart Agriculture Domain  

---

## 🌱 Future Enhancements  

🚀 Crop Disease Detection System  
🚀 Yield Prediction Module  
🚀 Fertilizer Recommendation Engine  
🚀 Mobile Application Version  
🚀 Multi-language Farmer Support  
🚀 AI Assistant Chatbot  

---

## ⭐ Support This Project  

If you found this project useful:

⭐ Star the repository  
🍴 Fork the project  
📢 Share with others  

---

## 📄 License  

This project is licensed under the **MIT License**.

---

<div align="center">

### 🌾 Empowering Farmers Using Artificial Intelligence  
### Built with ❤️ for Smart Agriculture  

</div>
