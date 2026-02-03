import pandas as pd
import joblib
from sklearn.metrics import accuracy_score

data = pd.read_csv("dataset/Crop_recommendation.csv")

X = data.drop("label", axis=1)
y = data["label"]

model = joblib.load("model/crop_model.pkl")

predictions = model.predict(X)

accuracy = accuracy_score(y, predictions)

print("Model Accuracy:", accuracy)
