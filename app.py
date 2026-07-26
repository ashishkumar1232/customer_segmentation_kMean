import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="🛍️",
    layout="wide"
)

# ----------------------------
# Load Model
# ----------------------------
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

# ----------------------------
# Load Dataset
# ----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("Mall_Customers.csv")

df = load_data()

# ----------------------------
# Title
# ----------------------------
st.title("🛍️ Customer Segmentation using K-Means Clustering")
st.write(
    "This application groups customers based on **Annual Income** and **Spending Score**."
)

# ----------------------------
# Dataset Preview
# ----------------------------
if st.checkbox("Show Dataset"):
    st.subheader("Mall Customers Dataset")
    st.dataframe(df)

# ----------------------------
# Features for Clustering
# ----------------------------
X = df.iloc[:, [3, 4]]

# Predict Clusters
clusters = model.predict(X)

# Add cluster column
df["Cluster"] = clusters

# ----------------------------
# Cluster Visualization
# ----------------------------
st.subheader("Customer Segments")

fig, ax = plt.subplots(figsize=(8, 6))

colors = ["red", "blue", "green", "orange", "purple"]

for i in range(5):
    ax.scatter(
        X.iloc[clusters == i, 0],
        X.iloc[clusters == i, 1],
        s=60,
        color=colors[i],
        label=f"Cluster {i+1}"
    )

# Plot centroids
centers = model.cluster_centers_

ax.scatter(
    centers[:, 0],
    centers[:, 1],
    s=250,
    color="black",
    marker="X",
    label="Centroids"
)

ax.set_xlabel("Annual Income (k$)")
ax.set_ylabel("Spending Score (1-100)")
ax.set_title("Customer Segmentation")
ax.legend()

st.pyplot(fig)

# ----------------------------
# Cluster Statistics
# ----------------------------
st.subheader("Cluster Summary")

summary = (
    df.groupby("Cluster")[["Annual Income (k$)", "Spending Score (1-100)"]]
    .mean()
    .round(2)
)

st.dataframe(summary)

# ----------------------------
# Download Dataset
# ----------------------------
csv = df.to_csv(index=False)

st.download_button(
    label="📥 Download Clustered Dataset",
    data=csv,
    file_name="customer_segments.csv",
    mime="text/csv"
)

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.markdown(
    "**Developed by Ashish Kumar**  |  Machine Learning Project using K-Means Clustering"
)
