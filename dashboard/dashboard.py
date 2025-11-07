import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------------------------
# 🧭 1️⃣ CONFIGURASI DASAR
# ----------------------------------------------------
st.set_page_config(
    page_title="E-Commerce Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🛍️ E-Commerce Data Analysis Dashboard")
st.markdown("Visualisasi interaktif hasil eksplorasi data e-commerce (2016–2018)")

# ----------------------------------------------------
# 📂 2️⃣ LOAD DATA
# ----------------------------------------------------
@st.cache_data
def load_data():
    merged_data = pd.read_csv("dashboard/cleaned_merged_data.csv", parse_dates=["order_purchase_timestamp"])
    rfm = pd.read_csv("dashboard/rfm.csv")
    return merged_data, rfm

merged_data, rfm = load_data()

# ----------------------------------------------------
# 🎛️ 3️⃣ SIDEBAR FILTER
# ----------------------------------------------------
st.sidebar.header("🔍 Filter Data")

years = sorted(merged_data["order_purchase_timestamp"].dt.year.unique())
selected_year = st.sidebar.multiselect("Pilih Tahun:", years, default=years)

states = sorted(merged_data["customer_state"].dropna().unique())
selected_states = st.sidebar.multiselect("Pilih Negara Bagian:", states, default=states)

categories = sorted(merged_data["product_category_name_english"].dropna().unique())
selected_categories = st.sidebar.multiselect("Pilih Kategori Produk:", categories)

payment_types = sorted(merged_data["payment_type"].dropna().unique())
selected_payment = st.sidebar.multiselect("Pilih Metode Pembayaran:", payment_types)

# Filter dataset berdasarkan input
filtered_data = merged_data[
    merged_data["order_purchase_timestamp"].dt.year.isin(selected_year)
    & merged_data["customer_state"].isin(selected_states)
].copy()

if selected_categories:
    filtered_data = filtered_data[filtered_data["product_category_name_english"].isin(selected_categories)]
if selected_payment:
    filtered_data = filtered_data[filtered_data["payment_type"].isin(selected_payment)]

# ✅ Pastikan kolom tanggal tetap datetime (hindari TypeError)
date_cols = [
    "order_purchase_timestamp",
    "order_delivered_customer_date",
    "order_approved_at",
    "order_estimated_delivery_date"
]
for col in date_cols:
    if col in filtered_data.columns:
        filtered_data[col] = pd.to_datetime(filtered_data[col], errors="coerce")


# ----------------------------------------------------
# 🧱 4️⃣ STRUKTUR TAB DASHBOARD
# ----------------------------------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Overview",
    "👥 Customer",
    "💳 Payment",
    "📦 Product & Seller",
    "⭐ Review & Delivery"
])

# ----------------------------------------------------
# 📊 5️⃣ TAB 1: OVERVIEW
# ----------------------------------------------------
with tab1:
    st.subheader("📈 Business Overview")

    col1, col2, col3, col4 = st.columns(4)
    total_revenue = filtered_data["payment_value"].sum()
    total_orders = filtered_data["order_id"].nunique()
    avg_order = filtered_data["payment_value"].mean()
    avg_delivery = (filtered_data["order_delivered_customer_date"] - filtered_data["order_purchase_timestamp"]).dt.days.mean()

    col1.metric("💰 Total Revenue (BRL)", f"{total_revenue:,.0f}")
    col2.metric("📦 Total Orders", f"{total_orders:,}")
    col3.metric("💳 Avg. Order Value", f"{avg_order:,.0f}")
    col4.metric("⏱️ Avg. Delivery (Days)", f"{avg_delivery:.1f}")

    # Tren jumlah pesanan per bulan
    filtered_data["month"] = filtered_data["order_purchase_timestamp"].dt.to_period("M").astype(str)
    orders_per_month = filtered_data.groupby("month")["order_id"].nunique().reset_index()
    fig_monthly = px.line(orders_per_month, x="month", y="order_id", title="📅 Tren Jumlah Pesanan per Bulan")
    st.plotly_chart(fig_monthly, use_container_width=True)

    # Pendapatan per negara bagian
    revenue_state = filtered_data.groupby("customer_state")["payment_value"].sum().sort_values(ascending=False).reset_index()
    fig_state = px.bar(revenue_state, x="customer_state", y="payment_value", title="💵 Total Pendapatan per Negara Bagian")
    st.plotly_chart(fig_state, use_container_width=True)

# ----------------------------------------------------
# 👥 6️⃣ TAB 2: CUSTOMER
# ----------------------------------------------------
with tab2:
    st.subheader("👥 Customer Demographics & Behavior")

    # Distribusi pelanggan per kota
    top_cities = filtered_data["customer_city"].value_counts().head(10).reset_index()
    top_cities.columns = ["City", "Count"]
    top_cities = top_cities.sort_values("Count", ascending=True)
    fig_city = px.bar(top_cities, x="Count", y="City",
                     title="Top 10 Kota dengan Pelanggan Terbanyak",
                     labels={"City": "Kota", "Count": "Jumlah Pelanggan"})
    fig_city.update_layout(
        xaxis_tickangle=-45,
        showlegend=False
    )
    st.plotly_chart(fig_city, use_container_width=True)

    # Proporsi pelanggan baru vs repeat
    st.markdown("### 🔁 Proporsi Pelanggan Baru vs Repeat")
    purchase_count = filtered_data.groupby("customer_unique_id")["order_id"].nunique()
    new_vs_repeat = purchase_count.gt(1).value_counts().rename({True: "Repeat", False: "New"})
    fig_repeat = px.pie(values=new_vs_repeat.values, names=new_vs_repeat.index, hole=0.4, title="Proporsi Pelanggan Baru vs Repeat")
    st.plotly_chart(fig_repeat, use_container_width=True)

    # Segmentasi RFM
    st.markdown("### 💎 Segmentasi Pelanggan (RFM)")
    seg_counts = rfm["Customer_Segment"].value_counts().reset_index()
    seg_counts.columns = ["Segment", "Customers"]
    fig_rfm = px.bar(seg_counts, x="Segment", y="Customers", color="Segment", title="Distribusi Segmen Pelanggan (RFM)")
    st.plotly_chart(fig_rfm, use_container_width=True)

    # Pemetaan Pelanggan Berdasarkan Frequency & Monetary
    st.markdown("### 📍 Pemetaan Pelanggan Berdasarkan Frequency & Monetary")
    fig_rf = px.scatter(rfm, x="Frequency", y="Monetary", color="Customer_Segment", title="Pemetaan Pelanggan Berdasarkan Frequency & Monetary")
    st.plotly_chart(fig_rf, use_container_width=True)

    # RFM heatmap
    rfm_heatmap = rfm.groupby(['R_score','F_score']).size().unstack(fill_value=0)
    st.plotly_chart(px.imshow(rfm_heatmap, title="RFM Heatmap"), use_container_width=True)

    # RFM filter with query params
    st.markdown("### 📝 Table RFM Pelanggan")
    default_segments = st.query_params.get_all("segments") or []
    
    rfm_segments = list(rfm["Customer_Segment"].unique())
    selected_rfm = st.multiselect(
        "Pilih Segmen Pelanggan:",
        options=rfm_segments,
        default=default_segments if default_segments else None,
        key="rfm_segments"
    )

    # Update query params
    if selected_rfm:
        st.query_params["segments"] = selected_rfm
        filtered_rfm = rfm[rfm["Customer_Segment"].isin(selected_rfm)]
        st.dataframe(filtered_rfm)
    else:
        st.query_params.clear()
        st.info("Silakan pilih setidaknya satu segmen pelanggan untuk menampilkan data.")

# ----------------------------------------------------
# 💳 7️⃣ TAB 3: PAYMENT
# ----------------------------------------------------
with tab3:
    st.subheader("💳 Payment & Transaction Insights")

    # Distribusi metode pembayaran
    pay_dist = filtered_data["payment_type"].value_counts(normalize=True).mul(100).reset_index()
    pay_dist.columns = ["Payment Type", "Percentage"]
    fig_payment = px.pie(pay_dist, values="Percentage", names="Payment Type", hole=0.4, title="Distribusi Metode Pembayaran")
    st.plotly_chart(fig_payment, use_container_width=True)

    # Nilai transaksi rata-rata per metode
    avg_payment_value = filtered_data.groupby("payment_type")["payment_value"].mean().reset_index()
    fig_avg_payment = px.bar(avg_payment_value, x="payment_type", y="payment_value", title="Rata-rata Nilai Transaksi per Metode")
    st.plotly_chart(fig_avg_payment, use_container_width=True)

# ----------------------------------------------------
# 📦 8️⃣ TAB 4: PRODUCT & SELLER
# ----------------------------------------------------
with tab4:
    st.subheader("📦 Product & Seller Performance")

    # Top kategori produk
    top_categories = filtered_data["product_category_name_english"].value_counts().head(10).reset_index()
    top_categories.columns = ["Category", "Orders"]
    top_categories = top_categories.sort_values("Orders", ascending=True)
    fig_cat = px.bar(top_categories, x="Category", y="Category", orientation="h", title="Top 10 Kategori Produk Paling Populer")
    st.plotly_chart(fig_cat, use_container_width=True)

    # Top seller
    top_sellers = (
        filtered_data.groupby("seller_id")["payment_value"].sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    fig_seller = px.bar(top_sellers, x="seller_id", y="payment_value", title="Top 10 Penjual dengan Penjualan Tertinggi")
    st.plotly_chart(fig_seller, use_container_width=True)

# ----------------------------------------------------
# ⭐ 9️⃣ TAB 5: REVIEW & DELIVERY
# ----------------------------------------------------
with tab5:
    st.subheader("⭐ Review & Delivery Analysis")

    # Distribusi skor ulasan
    review_dist = filtered_data["review_score"].value_counts().sort_index().reset_index()
    review_dist.columns = ["Review Score", "Count"]
    fig_review = px.bar(review_dist, x="Review Score", y="Count", title="Distribusi Skor Ulasan")
    st.plotly_chart(fig_review, use_container_width=True)

    # Korelasi review vs waktu pengiriman
    filtered_data["delivery_time"] = (
        filtered_data["order_delivered_customer_date"] - filtered_data["order_purchase_timestamp"]
    ).dt.days
    fig_corr = px.scatter(filtered_data, x="delivery_time", y="review_score", trendline="ols",
                          title="Korelasi antara Waktu Pengiriman dan Skor Ulasan")
    st.plotly_chart(fig_corr, use_container_width=True)

    avg_delivery_time = filtered_data["delivery_time"].mean()
    st.metric("⏱️ Rata-rata Waktu Pengiriman (hari)", f"{avg_delivery_time:.1f}")

# ----------------------------------------------------
# 📝 10️⃣ CATATAN
# ----------------------------------------------------
st.sidebar.info("💡 Gunakan filter di kiri untuk menyesuaikan tampilan data sesuai kebutuhan analisis.")
