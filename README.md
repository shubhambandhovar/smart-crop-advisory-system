🌾 Smart Crop Advisory System

An AI-powered web platform that recommends the most suitable crops for farmers based on real-time weather conditions and estimated soil parameters using Machine Learning.

🚀 Project Overview

The Smart Crop Advisory System helps farmers make informed crop selection decisions by analyzing:

🌦 Live Weather Data (Temperature, Rainfall, Humidity)

🌱 Estimated Soil Nutrients (NPK, pH)

📍 Location-based Inputs (Village / City Search)

🤖 Machine Learning Crop Recommendation Model

Farmers only need to enter their village or city name, and the system automatically fetches environmental parameters and suggests the top suitable crops with confidence scores.

✨ Key Features

✔ Location search with live suggestions
✔ Automatic weather data fetching using API
✔ Soil nutrient estimation (Satellite/Global Dataset Based)
✔ Machine Learning crop prediction
✔ Top 3 crop recommendations with confidence percentage
✔ Simple farmer-friendly UI
✔ REST API based backend architecture
✔ Modular Flask backend structure

🧠 Machine Learning Model

The system uses a Random Forest Classifier trained on crop recommendation dataset.

Input Features:

Nitrogen (N)

Phosphorus (P)

Potassium (K)

Temperature

Humidity

Rainfall

Soil pH

Output:

Recommended Crop Label

🏗 Project Architecture
smart-crop-advisory-system
│
├── backend
│   ├── routes
│   │   └── prediction_routes.py
│   ├── services
│   │   ├── weather_service.py
│   │   ├── soil_service.py
│   │   └── geocode_service.py
│   ├── utils
│   └── app.py
│
├── model
│   ├── train_model.py
│   └── crop_model.pkl
│
├── dataset
│   └── Crop_recommendation.csv
│
├── frontend
│   ├── static
│   │   ├── css
│   │   └── js
│   └── templates
│       └── index.html
│
├── .env
├── requirements.txt
├── README.md
└── venv

🖥 Tech Stack
Frontend:

HTML

CSS

JavaScript

Backend:

Python

Flask REST API

Machine Learning:

Scikit-learn

Pandas

NumPy

APIs Used:

OpenWeatherMap API (Weather Data)

Geocoding API (Location Search)

Soil Estimation Dataset (FAO/SoilGrids Inspired)

📊 Dataset

The model is trained using the Crop Recommendation Dataset containing:

Soil nutrients

Weather parameters

Crop labels

Source:
Kaggle Crop Recommendation Dataset

⚙ Installation & Setup
Step 1 — Clone Repository
git clone https://github.com/yourusername/smart-crop-advisory-system.git
cd smart-crop-advisory-system

Step 2 — Create Virtual Environment
python -m venv venv


Activate:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

Step 3 — Install Dependencies
pip install -r requirements.txt

Step 4 — Create .env File

Inside project root:

OPENWEATHER_API_KEY=your_api_key_here

Step 5 — Train ML Model (Optional)

If model file is not present:

python model/train_model.py

Step 6 — Run Flask Server
python -m backend.app


Server will start at:

http://127.0.0.1:5000

🌐 How It Works

User enters village/city name

System fetches latitude and longitude

Weather API provides real-time data

Soil parameters are estimated

ML model predicts best crops

Top 3 recommendations are displayed

📸 UI Preview

Smart Crop Advisory Dashboard

Location Input

Predict Crop Button

Crop Recommendation Cards

Weather Information

Soil Data Summary

⚠ Important Note

Soil data is estimated using public datasets and not real-time physical sensors.
This system is designed for educational and advisory purposes.

👨‍💻 Developer

Shubham Shrivastava
Final Year B.Tech CSE Student
Capstone Project — Smart Agriculture Domain

📌 Future Enhancements

🌾 Crop disease detection using images

📱 Mobile app version

🛰 Satellite-based soil monitoring

📊 Yield prediction

🌍 Regional language support

🤖 AI Chatbot for farmers

⭐ Support

If you like this project:

Give ⭐ Star on GitHub

Fork for improvement

Share with others

📄 License

This project is licensed under the MIT License.
