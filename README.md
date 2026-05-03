# Customer Segmentation Web App

A full-stack web application for **Customer Segmentation** using Machine Learning.  
This app allows you to classify customers into clusters based on their features and perform real-time predictions through a web interface built with **Streamlit**.

---

## 🚀 Features

- **Exploratory Data Analysis (EDA):** Understand customer data with visualizations.
- **Feature Selection:** Choose the most relevant features for clustering.
- **Clustering:** Segment customers using ML algorithms (like KMeans).
- **Real-Time Prediction:** Predict customer segments directly on the web app.
- **Sample profile presets:** Load example customer profiles for faster testing.
- **Prediction confidence score:** See how closely the customer matches the predicted cluster.
- **Interactive Dashboard:** Visualize clusters and key metrics.

---

## 🛠 Tech Stack

- **Python 3.10+**
- **Machine Learning:** scikit-learn, joblib
- **Data Handling:** pandas, numpy
- **Visualization:** matplotlib, seaborn
- **Web Framework:** Streamlit
- **Environment Management:** python-dotenv

---

Project Structure

customer-segmentation-app/
│
├── app.py                   # Streamlit main app
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── notebooks/
│   ├── artifacts/
│   |── data_1   └── customer_segmentation_pipeline.pkl/           # ML models and clustering logic
          └──clustered_data
├── pipelines
│   └── train and prediction pipelines
├── data/
│   └── marketing_campaign.csv      # Example dataset
└── models/
    └── ustomer_segmentation_pipeline.pkl   # Saved ML model




