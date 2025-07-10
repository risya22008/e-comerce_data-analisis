# 📦 E-Commerce Customer Behavior Dashboard

An interactive Streamlit dashboard designed to analyze customer behavior from e-commerce sales data. This project provides visual insights into sales performance, product trends, and customer segmentation.

## 🔍 Features

- **Key Metrics**: Total transactions, number of unique customers, and total sales
- **Top Products**: Visualization of the 10 best-selling products
- **Sales Trends**: Monthly sales trend analysis
- **Customer Segmentation**: RFM (Recency, Frequency, Monetary) analysis with K-Means clustering

## 🛠 Tech Stack

- **Python** – Core programming language  
- **Pandas** – Data loading and manipulation  
- **Streamlit** – Interactive web-based dashboard  
- **Matplotlib & Seaborn** – Visualizations  
- **Scikit-learn** – Clustering with StandardScaler and K-Means  
- **GitHub** – Dataset hosting (via raw CSV link)

## 📊 Dataset

The dataset is an e-commerce transaction dataset containing:
- Invoice details
- Product descriptions
- Quantities and unit prices
- Customer IDs
- Timestamps of purchases

Cleaned and filtered to remove negative or zero values in quantity and price.

📁 **Source**: [data.csv](https://raw.githubusercontent.com/risya22008/e-comerce_data-analisis/main/data.csv)

## 🚀 How to Run

1. **Clone this repository**  
```bash
git clone [https://github.com/yourusername/ecommerce-dashboard.git](https://github.com/risya22008/e-comerce_data-analisis.git)
cd e-comerce_data-analisis
```

2. **Install dependencies** 
```bash
pip install -r requirements.txt
```

3. **Run the app** 
```bash
streamlit run app.py
```

## 📌 RFM Segmentation Overview
Recency: Days since the customer’s last purchase
Frequency: Number of transactions by the customer
Monetary: Total spending by the customer
Clustered into 4 groups using K-Means to identify behavior patterns.
