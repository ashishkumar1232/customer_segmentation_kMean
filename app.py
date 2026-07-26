import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib

# Load model
model = joblib.load("model.pkl")

st.set_page_config(page_title="Customer Segmentation", page_icon="🛍")

st.title("🛍 Customer Segmentation using K-Means")

uploaded_file = st.file_uploader(
    "Upload Mall_Customers.csv",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    X = df.iloc[:, [3, 4]]

    clusters = model.predict(X)

    df["Cluster"] = clusters

    st.subheader("Dataset")

    st.dataframe(df)

    fig, ax = plt.subplots(figsize=(8,6))

    scatter = ax.scatter(
        X.iloc[:,0],
        X.iloc[:,1],
        c=clusters
    )

    ax.scatter(
        model.cluster_centers_[:,0],
        model.cluster_centers_[:,1],
        s=300,
        marker="X"
    )

    ax.set_xlabel("Annual Income")

    ax.set_ylabel("Spending Score")

    st.pyplot(fig)