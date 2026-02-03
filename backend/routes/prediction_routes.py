# from flask import Blueprint, request, jsonify
# from backend.services.geocode_service import search_city
# from backend.services.weather_service import get_weather_data_by_coords
# from backend.services.soil_service import get_soil_data
# import joblib

# predict_bp = Blueprint("predict", __name__)

# # Load ML model
# model = joblib.load("model/crop_model.pkl")


# # ===============================
# # LOCATION SEARCH API
# # ===============================

# @predict_bp.route("/search/<query>")
# def search_location(query):
#     return jsonify(search_city(query))


# # ===============================
# # CROP PREDICTION API
# # ===============================

# @predict_bp.route("/predict", methods=["POST"])
# def predict_crop():

#     data = request.json

#     lat = data["lat"]
#     lon = data["lon"]

#     # ================= WEATHER =================

#     weather = get_weather_data_by_coords(lat, lon)

#     temperature = weather["temperature"]
#     humidity = weather["humidity"]
#     rainfall = weather["rainfall"]

#     # ================= SOIL =================

#     soil = get_soil_data(lat, lon)

#     nitrogen = soil["nitrogen"]
#     phosphorus = soil["phosphorus"]
#     potassium = soil["potassium"]
#     ph = soil["ph"]

#     # ================= ML INPUT =================

#     input_data = [[
#         nitrogen,
#         phosphorus,
#         potassium,
#         temperature,
#         humidity,
#         ph,
#         rainfall
#     ]]

#     # ================= PREDICTION =================

#     proba = model.predict_proba(input_data)[0]
#     classes = model.classes_

#     top_indices = proba.argsort()[-3:][::-1]

#     top_crops = []

#     for i in top_indices:
#         top_crops.append({
#             "crop": classes[i],
#             "confidence": round(proba[i] * 100, 2)
#         })

#     # ================= RESPONSE =================

#     return jsonify({
#         "recommended_crops": top_crops,
#         "weather": weather,
#         "soil": soil
#     })
from flask import Blueprint, request, jsonify
import numpy as np
import joblib

from backend.services.geocode_service import search_city
from backend.services.weather_service import get_weather_data_by_coords
from backend.services.soil_service import get_soil_data

# ================================
# CREATE BLUEPRINT (VERY IMPORTANT)
# ================================

predict_bp = Blueprint("predict", __name__)

# ================================
# LOAD MODELS
# ================================

rf_model = joblib.load("model/rf_model.pkl")
kmeans = joblib.load("model/kmeans.pkl")
cluster_map = joblib.load("model/cluster_map.pkl")
scaler = joblib.load("model/scaler.pkl")


# ================================
# LOCATION SEARCH API
# ================================

@predict_bp.route("/search/<query>")
def search_location(query):
    return jsonify(search_city(query))


# ================================
# CROP PREDICTION API
# ================================

@predict_bp.route("/predict", methods=["POST"])
def predict_crop():

    data = request.json

    lat = data["lat"]
    lon = data["lon"]

    # ---------------- WEATHER ----------------

    weather = get_weather_data_by_coords(lat, lon)

    # ---------------- SOIL ----------------

    soil = get_soil_data(lat, lon)

    # ---------------- INPUT FEATURES ----------------

    input_features = [[
        soil["nitrogen"],
        soil["phosphorus"],
        soil["potassium"],
        weather["temperature"],
        weather["humidity"],
        soil["ph"],
        weather["rainfall"]
    ]]

    # Normalize
    input_scaled = scaler.transform(input_features)

    # ---------------- RF PROBABILITIES ----------------

    rf_probs = rf_model.predict_proba(input_scaled)[0]
    rf_classes = rf_model.classes_

    # ---------------- KMEANS MEMBERSHIP ----------------

    distances = kmeans.transform(input_scaled)[0]

    inv_dist = 1 / (distances + 0.0001)
    membership = inv_dist / np.sum(inv_dist)

    final_scores = {}

    for cluster_id, weight in enumerate(membership):

        label_probs = cluster_map[cluster_id]

        for label, prob in label_probs.items():
            final_scores[label] = final_scores.get(label, 0) + (weight * prob)

    # ---------------- COMBINE SCORES ----------------

    combined_scores = {}

    for i, label in enumerate(rf_classes):

        rf_score = rf_probs[i]
        cluster_score = final_scores.get(label, 0)

        combined_scores[label] = (0.6 * rf_score) + (0.4 * cluster_score)

    # ---------------- TOP 3 RESULTS ----------------

    sorted_results = sorted(
        combined_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    top3 = []

    for crop, score in sorted_results[:3]:
        top3.append({
            "crop": crop,
            "confidence": round(score * 100, 2)
        })

    return jsonify({
        "recommended_crops": top3,
        "weather": weather,
        "soil": soil,
        "method": "Hybrid RF + KMeans Membership"
    })
