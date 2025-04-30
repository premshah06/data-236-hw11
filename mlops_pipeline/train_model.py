import os
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Train on Iris and save artifact into this folder
data = load_iris()
model = RandomForestClassifier()
model.fit(data.data, data.target)

# Build the path to this file’s directory
path = os.path.join(os.path.dirname(__file__), "model.pkl")
joblib.dump(model, path)
print(f"✔ Model saved to {path}")