import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_data(path):

    data = pd.read_csv(path)

    # Check imbalance (for reporting)
    class_counts = data["label"].value_counts()

    X = data.drop("label", axis=1)
    y = data["label"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler, class_counts
