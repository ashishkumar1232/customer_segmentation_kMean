import pandas as pd
import joblib
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("Mall_Customers.csv")

# Select features
X = df.iloc[:, [3, 4]]

# Train model
model = KMeans(
    n_clusters=5,
    init="k-means++",
    random_state=42
)

model.fit(X)

# Save model
joblib.dump(model, "model.pkl")

print("Model saved successfully!")