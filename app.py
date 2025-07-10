import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide")
st.title("📦 E-Commerce Customer Behavior Dashboard")

# Load data (pastikan file CSV sudah dibersihkan)
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/risya22008/e-comerce_data-analisis/main/data.csv"
    df = pd.read_csv(url, encoding='ISO-8859-1')
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['CustomerID'] = df['CustomerID'].astype(str)
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']
    return df

df = load_data()

# Sidebar filter
with st.sidebar:
    st.header("📊 Filter")
    min_date = df['InvoiceDate'].min()
    max_date = df['InvoiceDate'].max()
    date_range = st.date_input("Pilih rentang tanggal:", [min_date, max_date])

# Filter data berdasarkan tanggal
if len(date_range) == 2:
    df = df[(df['InvoiceDate'] >= pd.to_datetime(date_range[0])) & (df['InvoiceDate'] <= pd.to_datetime(date_range[1]))]

# --- KPI ---
st.subheader("🔢 Ringkasan Data")
total_transaksi = df['InvoiceNo'].nunique()
total_pelanggan = df['CustomerID'].nunique()
total_penjualan = df['TotalPrice'].sum()

col1, col2, col3 = st.columns(3)
col1.metric("🧾 Total Transaksi", f"{total_transaksi}")
col2.metric("👥 Total Pelanggan", f"{total_pelanggan}")
col3.metric("💰 Total Penjualan", f"£{total_penjualan:,.2f}")

# --- Visualisasi Produk Terlaris ---
st.subheader("🔥 Top 10 Produk Terlaris")
top_produk = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
fig1, ax1 = plt.subplots()
sns.barplot(x=top_produk.values, y=top_produk.index, ax=ax1, palette='viridis')
ax1.set_xlabel("Jumlah Terjual")
st.pyplot(fig1)

# --- Penjualan Bulanan ---
st.subheader("📅 Penjualan per Bulan")
df_bulanan = df.set_index('InvoiceDate').resample('M')['TotalPrice'].sum()
fig2, ax2 = plt.subplots()
df_bulanan.plot(ax=ax2, marker='o')
ax2.set_ylabel("Total Sales (£)")
ax2.set_title("Penjualan Bulanan")
st.pyplot(fig2)

# --- Segmentasi Pelanggan RFM ---
st.subheader("🧠 Segmentasi Pelanggan (RFM Clustering)")
ref_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (ref_date - x.max()).days,
    'InvoiceNo': 'nunique',
    'TotalPrice': 'sum'
})
rfm.columns = ['Recency', 'Frequency', 'Monetary']

scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)
kmeans = KMeans(n_clusters=4, random_state=42)
rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

fig3, ax3 = plt.subplots()
sns.scatterplot(data=rfm, x='Recency', y='Monetary', hue='Cluster', palette='Set2', ax=ax3)
ax3.set_title("Cluster Pelanggan: Recency vs Monetary")
st.pyplot(fig3)