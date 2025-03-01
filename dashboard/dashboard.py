import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# Configure Streamlit
st.set_page_config(layout="wide", page_title="Business Insights Dashboard")

# Sidebar Navigation
st.sidebar.title("📍 Navigation")
page = st.sidebar.selectbox("Select a Page:", ["Dashboard", "RFM Analysis"])

# Load dataset
df = pd.read_csv("dashboard/datasets_cleaned.csv")

# Pastikan timestamp dalam format datetime
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])
df['shipping_limit_date'] = pd.to_datetime(df['shipping_limit_date'])

# ===========================
# HALAMAN 1: DASHBOARD UTAMA
# ===========================
if page == "Dashboard":
    st.title("📊 Business Insights Dashboard | Brazilian E-Commerce Public Dataset by Olist")
    
    st.write("Dashboard utama berisi insight bisnis berdasarkan data transaksi.")
    st.image("dashboard/dataset-cover.png", use_container_width=True) 

    # Sidebar: Profil
    with st.sidebar:

    # Filter Options
        st.subheader("Filters")
        
        # Filter berdasarkan Tanggal
        start_date = st.date_input("Start Date", df['order_purchase_timestamp'].min())
        end_date = st.date_input("End Date", df['order_purchase_timestamp'].max())
        
        df_filtered = df[(df['order_purchase_timestamp'] >= pd.to_datetime(start_date)) & 
                        (df['order_purchase_timestamp'] <= pd.to_datetime(end_date))]
        
        # Filter berdasarkan Kategori Produk
        product_categories = df_filtered['product_category_name_english'].unique()
        selected_category = st.selectbox("Select Product Category", options=["All"] + list(product_categories))
        if selected_category != "All":
            df_filtered = df_filtered[df_filtered['product_category_name_english'] == selected_category]

        # Filter berdasarkan State
        states = df_filtered['customer_state'].unique()
        selected_state = st.selectbox("Select State", options=["All"] + list(states))
        if selected_state != "All":
            df_filtered = df_filtered[df_filtered['customer_state'] == selected_state]

        st.subheader("My Profile")
        st.markdown("""
        **Name:** Fiyanda Ma'muri  
        **Email:** fiyandamamuri@gmail.com  
        **LinkedIn:** [Profil LinkedIn](https://id.linkedin.com/in/fiyandamamuri/)  
        **GitHub:** [Profil GitHub](https://github.com/fiyandamamuri)  
        """)

    # Hitung KPI berdasarkan data yang sudah difilter
    total_orders = df_filtered["order_id"].nunique()
    total_revenue = df_filtered["payment_value"].sum()
    avg_order_value = total_revenue / total_orders
    total_customers = df_filtered["customer_unique_id"].nunique()

    # Update metrics
    st.markdown("<hr>", unsafe_allow_html=True)
    col1, col2, col3, col4= st.columns(4)

    with col1:
        st.metric(label="Total Orders", value=f"{total_orders:,}")

    with col2:
        st.metric(label="Total Revenue", value=f"${total_revenue:,.2f}")

    with col3:
        st.metric(label="Avg Order Value", value=f"${avg_order_value:,.2f}")

    with col4:
        st.metric(label="Total Customers", value=f"{total_customers:,}")

    st.markdown("<hr>", unsafe_allow_html=True)



    # Top 5 Cities with Most Customers (Filtered)
    top_cities = (
        df_filtered.groupby("customer_city")["customer_unique_id"]
        .nunique()
        .sort_values(ascending=False)
        .reset_index()
        .rename(columns={"customer_unique_id": "unique_customers"})
        .head(5)
    )

    st.subheader("Top 5 Cities with Most Customers")

    fig1, ax1 = plt.subplots(figsize=(14, 5))
    bars = ax1.barh(top_cities["customer_city"], top_cities["unique_customers"], color='teal')

    ax1.set_title("Top 5 Cities with Most Customers")
    ax1.set_xlabel("Number of Customers")
    ax1.set_ylabel("City")
    ax1.invert_yaxis()  # Membalik sumbu agar kota dengan pelanggan terbanyak di atas

    # Menambahkan label pada setiap bar
    for bar, value in zip(bars, top_cities["unique_customers"]):
        ax1.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, f'{value:,}', va='center', fontsize=10)

    st.pyplot(fig1)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)



    # Menampilkan subjudul
    st.subheader("Payment Type Distribution")
    payment_type_counts = df_filtered['payment_type'].value_counts()

    # Membuat layout kolom agar pie chart tidak memenuhi layar
    col1, col2, col3 = st.columns([1, 2, 1])  # Tengah lebih lebar

    with col2:  # Menempatkan di tengah agar lebih kecil
        fig, ax = plt.subplots(figsize=(2, 2), dpi=100, constrained_layout=True)  # Ukuran lebih kecil dan layout terkontrol
        colors = plt.cm.tab10(np.linspace(0, 1, len(payment_type_counts)))
        
        wedges, texts, autotexts = ax.pie(payment_type_counts.values, 
                                        labels=payment_type_counts.index, 
                                        autopct='%1.1f%%', 
                                        colors=colors, 
                                        startangle=120, 
                                        wedgeprops={'edgecolor': 'white'})

        
        # Mengatur ukuran font
        for text in texts:  
            text.set_fontsize(4)  # Ukuran label lebih kecil
        for autotext in autotexts:  
            autotext.set_fontsize(4)  # Ukuran persentase lebih kecil

        ax.axis('equal')  # Agar tetap berbentuk lingkaran
        ax.set_title('Payment Type Distribution', fontsize=4)

        # Menampilkan plot di Streamlit
        st.pyplot(fig)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)


    # Trend of Orders per Month
    orders_by_month = (
        df_filtered['order_purchase_timestamp']
        .dt.to_period('M')
        .value_counts()
        .sort_index()
    )
    orders_by_month_df = orders_by_month.reset_index()
    orders_by_month_df.columns = ['Month', 'Order Count']
    orders_by_month_df['Month'] = orders_by_month_df['Month'].dt.to_timestamp()

    st.subheader("Trend of Orders per Month")
    fig3, ax3 = plt.subplots(figsize=(12, 5))
    ax3.plot(orders_by_month_df['Month'], orders_by_month_df['Order Count'], marker='o', linestyle='-', color='teal')
    ax3.set_title("Trend of Orders per Month")
    ax3.set_xlabel("Month")
    ax3.set_ylabel("Order Count")
    ax3.grid(True, linestyle='--', alpha=0.6)
    for i, row in orders_by_month_df.iterrows():
        ax3.text(row['Month'], row['Order Count'] + 10, f"{row['Order Count']:,}", ha='center', fontsize=8  )
    st.pyplot(fig3)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)



    # Top 5 Product Categories
    top_categories = df_filtered['product_category_name_english'].value_counts().head(5)
    st.subheader("Top 5 Product Categories")
    fig4, ax4 = plt.subplots(figsize=(12, 5))
    bars = ax4.barh(top_categories.index, top_categories.values, color='royalblue')
    ax4.set_title("Top 5 Product Categories")
    ax4.set_xlabel("Number of Products Sold")
    ax4.set_ylabel("Product Category")
    ax4.invert_yaxis()
    for bar in bars:
        ax4.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, f'{bar.get_width():,}', va='center', fontsize=8)
    st.pyplot(fig4)

    st.markdown("<hr>", unsafe_allow_html=True)

# ===========================
# HALAMAN 2: RFM ANALYSIS
# ===========================
elif page == "RFM Analysis":
    st.title("📈 RFM Analysis Dashboard")

    # Menentukan tanggal referensi untuk analisis RFM
    reference_date = df['order_purchase_timestamp'].max() + pd.Timedelta(days=1)

    # Menghitung RFM Metrics
    rfm = df.groupby('customer_unique_id').agg({
        'order_purchase_timestamp': lambda x: (reference_date - x.max()).days,  # Recency
        'order_id': 'count',  # Frequency
        'payment_value': 'sum'  # Monetary
    }).reset_index()

    # Ubah nama kolom agar lebih mudah dibaca
    rfm.columns = ['customer_unique_id', 'Recency', 'Frequency', 'Monetary']

    # Skoring RFM dengan kuartil
    rfm['R_Score'] = pd.qcut(rfm['Recency'], q=4, labels=[4, 3, 2, 1])
    rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method="first"), q=4, labels=[1, 2, 3, 4])
    rfm['M_Score'] = pd.qcut(rfm['Monetary'].rank(method="first"), q=4, labels=[1, 2, 3, 4])

    # Konversi skor ke tipe numerik
    rfm[['R_Score', 'F_Score', 'M_Score']] = rfm[['R_Score', 'F_Score', 'M_Score']].astype(int)

    # Menghitung RFM Score sebagai rata-rata dari ketiga skor
    rfm['RFM_Score'] = rfm[['R_Score', 'F_Score', 'M_Score']].mean(axis=1)

    # Segmentasi pelanggan berdasarkan RFM Score
    conditions = [
        (rfm['RFM_Score'] > 4),
        (rfm['RFM_Score'] > 3) & (rfm['RFM_Score'] <= 4),
        (rfm['RFM_Score'] > 2) & (rfm['RFM_Score'] <= 3),
        (rfm['RFM_Score'] <= 2)
    ]
    labels = ["Top Customer", "High Value Customer", "Medium Value Customer", "Low Customer"]
    rfm["customer_segment"] = np.select(conditions, labels, default="Unknown")

    # Pilihan filter berdasarkan segmen pelanggan
    segment_options = ["All"] + list(rfm["customer_segment"].unique())
    selected_segment = st.selectbox("Filter by Customer Segment:", segment_options)

    # Filter data berdasarkan segmen yang dipilih, lalu urutkan dari terbesar ke terkecil
    if selected_segment != "All":
        filtered_rfm = rfm[rfm["customer_segment"] == selected_segment].sort_values(by="RFM_Score", ascending=False)
    else:
        filtered_rfm = rfm.sort_values(by="RFM_Score", ascending=False)

    # Tampilkan tabel RFM
    st.dataframe(filtered_rfm)

    st.write("""
    RFM Analysis bertujuan untuk mengelompokkan pelanggan berdasarkan perilaku mereka dalam transaksi e-commerce menggunakan Recency (R), Frequency (F), dan Monetary (M).
    """)

    st.subheader("Penjelasan Kolom:")
    st.markdown("""
    - **customer_unique_id** → ID unik dari pelanggan.
    - **Recency** → Seberapa lama sejak pelanggan terakhir bertransaksi (dalam hari).
    - **Frequency** → Berapa kali pelanggan telah bertransaksi dalam periode tertentu.
    - **Monetary** → Total uang yang telah dibelanjakan oleh pelanggan.
    - **R_Score** → Skor Recency (1-4), 4 berarti baru aktif, 1 berarti lama tidak aktif.
    - **F_Score** → Skor Frequency (1-4), 4 berarti sering transaksi, 1 berarti jarang.
    - **M_Score** → Skor Monetary (1-4), 4 berarti pengeluaran besar, 1 berarti kecil.
    - **RFM_Score** → Skor rata-rata R, F, dan M (1.0 - 4.0).
    - **customer_segment** → Segmen pelanggan berdasarkan RFM Score:
        - **Top Customer** → RFM_Score > 4  
        - **High Value Customer** → 4 ≥ RFM_Score > 3  
        - **Medium Value Customer** → 3 ≥ RFM_Score > 2  
        - **Low Value Customer** → ≤ 2  
    """)


