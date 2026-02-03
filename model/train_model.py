# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# import joblib

# # Load dataset
# data = pd.read_csv("dataset/Crop_recommendation.csv")

# X = data.drop("label", axis=1)
# y = data["label"]

# # Train test split
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=42
# )

# # Train model
# model = RandomForestClassifier()
# model.fit(X_train, y_train)

# # Save model
# joblib.dump(model, "model/crop_model.pkl")

# print("✅ Model trained and saved successfully")
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from preprocess import preprocess_data

# Load + preprocess
X, y, scaler, class_counts = preprocess_data("dataset/Crop_recommendation.csv")

# -------------------------------
# Random Forest (Supervised)
# -------------------------------

rf_model = RandomForestClassifier(n_estimators=200)
rf_model.fit(X, y)

# -------------------------------
# KMeans Clustering
# -------------------------------

num_clusters = len(y.unique())

kmeans = KMeans(n_clusters=num_clusters, random_state=42)
clusters = kmeans.fit_predict(X)

# -------------------------------
# Cluster Label Proportions
# -------------------------------

cluster_label_map = {}

for c in range(num_clusters):

    indices = np.where(clusters == c)
    labels = y.iloc[indices]

    proportions = labels.value_counts(normalize=True).to_dict()

    cluster_label_map[c] = proportions

# -------------------------------
# Save Everything
# -------------------------------

joblib.dump(rf_model, "model/rf_model.pkl")
joblib.dump(kmeans, "model/kmeans.pkl")
joblib.dump(cluster_label_map, "model/cluster_map.pkl")
joblib.dump(scaler, "model/scaler.pkl")

print("✅ Hybrid Model Training Completed")
