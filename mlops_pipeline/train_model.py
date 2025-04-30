from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data & train
data = load_iris()
model = RandomForestClassifier()
model.fit(data.data, data.target)

# Save model artifact
joblib.dump(model, "model.pkl")
print("Model saved to model.pkl")
