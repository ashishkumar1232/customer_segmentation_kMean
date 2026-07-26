# 🛍️ Customer Segmentation using K-Means Clustering

## 🌐 Live Demo

🚀 **Try the application here:**

https://customersegmentationkmean.streamlit.app/

---

## 📌 Project Overview

This project uses the K-Means Clustering algorithm to segment customers based on their **Annual Income** and **Spending Score**. The application is built using **Python**, **Scikit-learn**, and **Streamlit**, allowing users to visualize customer clusters interactively.

# 🛍️ Customer Segmentation using K-Means Clustering

A Machine Learning web application that segments customers into different groups based on their **Annual Income** and **Spending Score** using the **K-Means Clustering** algorithm. The application is built with **Python**, **Scikit-learn**, and **Streamlit**, making it easy to visualize customer segments through an interactive interface.

---

## 📌 Project Overview

Customer segmentation helps businesses understand their customers by grouping them based on similar purchasing behaviour. These customer groups can be used for:

- Targeted marketing campaigns
- Personalized recommendations
- Customer retention strategies
- Business decision making

This project uses the **Mall Customers Dataset** and the **K-Means Clustering** algorithm to divide customers into meaningful clusters.

---

## 🚀 Features

- Upload customer dataset (.csv)
- Automatic customer segmentation using K-Means
- Interactive cluster visualization
- Displays cluster centroids
- Easy-to-use Streamlit interface
- Fast prediction using a pre-trained model

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib

---

## 📂 Project Structure

```
Customer-Segmentation/
│
├── app.py
├── train_model.py
├── model.pkl
├── requirements.txt
├── README.md
├── Mall_Customers.csv
└── .gitignore
```

---

## 📊 Dataset

The project uses the **Mall Customers Dataset** containing the following features:

- CustomerID
- Gender
- Age
- Annual Income (k£)
- Spending Score (1–100)

Only the following features are used for clustering:

- Annual Income
- Spending Score

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Customer-Segmentation.git
```

Move into the project folder:

```bash
cd Customer-Segmentation
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Model

Run:

```bash
python train_model.py
```

This generates:

- model.pkl

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📈 Algorithm Used

### K-Means Clustering

K-Means is an unsupervised machine learning algorithm that groups similar data points into clusters.

Steps:

1. Choose the number of clusters (K).
2. Randomly initialize centroids.
3. Assign each data point to the nearest centroid.
4. Update centroid positions.
5. Repeat until convergence.

---

## 📊 Output

The application displays:

- Customer clusters
- Cluster centroids
- Interactive scatter plot
- Clustered dataset

---

## 💡 Applications

- Customer Segmentation
- Market Basket Analysis
- Customer Behaviour Analysis
- Personalized Marketing
- Retail Analytics
- Business Intelligence

---

## 🔮 Future Improvements

- Automatic Elbow Method
- Silhouette Score Evaluation
- Plotly Interactive Visualizations
- Download Clustered Dataset
- Cluster Insights Dashboard
- Dark Mode UI

---

## 👨‍💻 Author

**Ashish Kumar**

Machine Learning | Data Science | Artificial Intelligence

---

## 📜 License

This project is developed for educational and learning purposes.
