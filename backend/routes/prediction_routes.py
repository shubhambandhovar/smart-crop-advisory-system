from flask import Blueprint, request, jsonify
from backend.services.geocode_service import search_city
from backend.services.weather_service import get_weather_data_by_coords
from backend.services.soil_service import get_soil_data
import joblib

predict_bp = Blueprint("predict", __name__)

# Load ML model
model = joblib.load("model/crop_model.pkl")


# ===============================
# LOCATION SEARCH API
# ===============================

@predict_bp.route("/search/<query>")
def search_location(query):
    return jsonify(search_city(query))


# ===============================
# CROP PREDICTION API
# ===============================

@predict_bp.route("/predict", methods=["POST"])
def predict_crop():

    data = request.json

    lat = data["lat"]
    lon = data["lon"]

    # ================= WEATHER =================

    weather = get_weather_data_by_coords(lat, lon)

    temperature = weather["temperature"]
    humidity = weather["humidity"]
    rainfall = weather["rainfall"]

    # ================= SOIL =================

    soil = get_soil_data(lat, lon)

    nitrogen = soil["nitrogen"]
    phosphorus = soil["phosphorus"]
    potassium = soil["potassium"]
    ph = soil["ph"]

    # ================= ML INPUT =================

    input_data = [[
        nitrogen,
        phosphorus,
        potassium,
        temperature,
        humidity,
        ph,
        rainfall
    ]]

    # ================= PREDICTION =================

    proba = model.predict_proba(input_data)[0]
    classes = model.classes_

    top_indices = proba.argsort()[-3:][::-1]

    top_crops = []

    for i in top_indices:
        top_crops.append({
            "crop": classes[i],
            "confidence": round(proba[i] * 100, 2)
        })

    # ================= RESPONSE =================

    return jsonify({
        "recommended_crops": top_crops,
        "weather": weather,
        "soil": soil
    })
