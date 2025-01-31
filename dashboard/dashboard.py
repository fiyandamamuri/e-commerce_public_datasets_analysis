import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Configure Streamlit page layout
st.set_page_config(layout="wide", page_title="Business Insights Dashboard")


# Title and Description
st.title("📊 Business Insights Dashboard | Brazilian E-Commerce Public Dataset by Olist")
st.markdown("This dashboard presents visualizations of key business insights based on transactional data.")
st.image("dashboard\dataset-cover.png", use_container_width=True) 

# Load dataset
df = pd.read_csv("dashboard\datasets_cleaned.csv")

# Ensure timestamps are in datetime format
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])
df['shipping_limit_date'] = pd.to_datetime(df['shipping_limit_date'])

# Sidebar: Profil
with st.sidebar:
    st.header("My Profile")
    st.markdown("""
    **Name:** Fiyanda Ma'muri  
    **Email:** fiyandamamuri@gmail.com  
    **LinkedIn:** [Profil LinkedIn](https://id.linkedin.com/in/fiyandamamuri/)  
    **GitHub:** [Profil GitHub](https://github.com/fiyandamamuri)  
    """)

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

# Hitung KPI berdasarkan data yang sudah difilter
total_orders = df_filtered["order_id"].nunique()
total_revenue = df_filtered["payment_value"].sum()
avg_order_value = total_revenue / total_orders
total_customers = df_filtered["customer_unique_id"].nunique()
on_time_deliveries = df_filtered[df_filtered["order_delivered_customer_date"] <= df_filtered["order_estimated_delivery_date"]].shape[0]
on_time_delivery_rate = (on_time_deliveries / total_orders) * 100
best_selling_category = df_filtered["product_category_name_english"].value_counts().idxmax()

# Update metrics
st.markdown("<hr>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total Orders", value=f"{total_orders:,}")

with col2:
    st.metric(label="Total Revenue", value=f"${total_revenue:,.2f}")

with col3:
    st.metric(label="Avg Order Value", value=f"${avg_order_value:,.2f}")

col4, col5, col6 = st.columns(3)

with col4:
    st.metric(label="Total Customers", value=f"{total_customers:,}")

with col5:
    st.metric(label="On-Time Delivery Rate", value=f"{on_time_delivery_rate:.2f}%")

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

fig1, ax1 = plt.subplots(figsize=(10, 5))
bars = ax1.barh(top_cities["customer_city"], top_cities["unique_customers"], color='teal')

ax1.set_title("Top 5 Cities with Most Customers")
ax1.set_xlabel("Number of Customers")
ax1.set_ylabel("City")
ax1.invert_yaxis()  # Membalik sumbu agar kota dengan pelanggan terbanyak di atas

# Menambahkan label pada setiap bar
for bar, value in zip(bars, top_cities["unique_customers"]):
    ax1.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, f'{value:,}', va='center', fontsize=10)

st.pyplot(fig1)

# Menampilkan Kesimpulan
st.write("""
##### Conclusion for Question 1:
- Based on the visualization, Sao Paulo stands out as the city with the highest number of customers, totaling 14,761 customers, far surpassing other cities. 
- The second position is occupied by Rio de Janeiro with 6,545 customers, which also shows a significant number, but only about half of Sao Paulo's customer base. 
- The other three cities, Belo Horizonte with 2,641 customers, Brasilia with 2,051 customers, and Curitiba with 1,447 customers, contribute much smaller numbers compared to Sao Paulo and Rio de Janeiro.
""")

# Insight Section
st.write("""
##### Insights:
- Sao Paulo, as the city with the largest customer base, shows that it can be the focal point for marketing strategies or service development.
- Cities with smaller customer numbers, such as Curitiba, could be targeted for further market expansion.
""")

# Business Recommendation Section
st.write("""
##### Business Recommendations:
- The company should strengthen services and promotions in Sao Paulo to retain existing customers.
- A larger investment in Rio de Janeiro could be made to maximize the market potential there.
- More aggressive marketing strategies could be directed at cities with smaller customer bases to boost customer growth.
""")
st.markdown("<hr>", unsafe_allow_html=True)



# Payment Type Distribution
payment_type_counts = df_filtered['payment_type'].value_counts()
st.subheader("Payment Type Distribution")
fig2, ax2 = plt.subplots(figsize=(10, 5))
bars = ax2.bar(payment_type_counts.index, payment_type_counts.values, color=plt.cm.viridis(range(len(payment_type_counts))))
ax2.set_title("Payment Type Distribution")
ax2.set_xlabel("Payment Type")
ax2.set_ylabel("Count")
for bar in bars:
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(bar.get_height()), ha='center', va='bottom', fontsize=10, color='black', weight='bold')
st.pyplot(fig2)

# Menampilkan Kesimpulan
st.write("""
##### Conclusion for Question 2:
- Credit Card is the most popular payment method, contributing to the majority of transactions.
- Boleto is the second most used payment method, with a significant contribution.
- Voucher and Debit Card are used by only a small number of customers.
""")

# Insight Section
st.write("""
##### Insights:
- Customers tend to prefer faster and more practical methods like Credit Card.
- Other payment methods have potential but need to offer additional conveniences to attract more users.
""")

# Business Recommendation Section
st.write("""
##### Business Recommendations:
- Optimize Credit Card usage by speeding up the authorization process and enhancing security.
- Simplify the Boleto payment process, such as shortening the payment steps.
- Promote minor payment methods like Voucher and Debit Card to diversify customers' payment preferences.
""")
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
fig3, ax3 = plt.subplots(figsize=(10, 5))
ax3.plot(orders_by_month_df['Month'], orders_by_month_df['Order Count'], marker='o', linestyle='-', color='teal')
ax3.set_title("Trend of Orders per Month")
ax3.set_xlabel("Month")
ax3.set_ylabel("Order Count")
ax3.grid(True, linestyle='--', alpha=0.6)
for i, row in orders_by_month_df.iterrows():
    ax3.text(row['Month'], row['Order Count'] + 10, f"{row['Order Count']:,}", ha='center', fontsize=9)
st.pyplot(fig3)

# Menampilkan Kesimpulan
st.write("""
##### Conclusion for Question 3:
- The number of orders showed a significant increase from 2016 to early 2018, indicating a positive growth trend.
- A sharp decline occurred after mid-2018.
""")

# Insight Section
st.write("""
##### Insights:
- No clear seasonal patterns are observed, but the order growth was stable until its peak in early 2018.
- The sharp decline after mid-2018 may indicate external factors such as policy changes, competitors, or market changes.
""")

# Business Recommendation Section
st.write("""
##### Business Recommendations:
- Analyze the cause of the decline after mid-2018 for corrective actions.
- Increase promotions to maintain growth, especially in months with high orders previously.
- Optimize inventory management to support the increasing order trend in early periods.
""")
st.markdown("<hr>", unsafe_allow_html=True)



# Top 5 Product Categories
top_categories = df_filtered['product_category_name_english'].value_counts().head(5)
st.subheader("Top 5 Product Categories")
fig4, ax4 = plt.subplots(figsize=(10, 5))
bars = ax4.barh(top_categories.index, top_categories.values, color='royalblue')
ax4.set_title("Top 5 Product Categories")
ax4.set_xlabel("Number of Products Sold")
ax4.set_ylabel("Product Category")
ax4.invert_yaxis()
for bar in bars:
    ax4.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2, f'{bar.get_width():,}', va='center', fontsize=10)
st.pyplot(fig4)
# Menampilkan Kesimpulan
st.write("""
##### Conclusion for questions 4:
- The "bed_bath_table" category is the most popular with the highest sales, followed by "health_beauty", "sports_leisure", "furniture_decor", and "computers_accessories".
""")

# Insight Section
st.write("""
##### Insights:
- Demand for "bed_bath_table" products is significantly higher than other categories, indicating great potential in this segment.
- Sales differences between categories show customer preference variations that can be leveraged in marketing strategies.
""")

# Business Recommendation Section
st.write("""
##### Business Recommendations:
- **Stock Optimization** → Ensure sufficient stock availability for high-selling categories to prevent stockouts.
- **Marketing Strategy** → Focus advertising and promotional campaigns on best-selling categories to further boost sales.
- **Product Expansion** → Conduct further analysis to add product variations in popular categories to remain competitive.
- **Customer Segmentation** → Use this data to understand customer preferences and target more specific promotions.
""")

st.sidebar.caption('Copyright © Fiyanda Mamuri - 2025')
