# Proyek Analisis Data: E-Commerce Public Dataset

## Datasets 
[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

##  📂 Structure Files
```
📦https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
 ┣ 📂dashboard
 ┃ ┣ 📜dataset-cover.png
 ┃ ┗ 📜dashboard.py
 ┃ ┗ 📜datasets_cleaned.csv
 ┣ 📂datasets
 ┃ ┣ 📜customers_dataset.csv
 ┃ ┣ 📜geolocation_dataset.csv
 ┃ ┣ 📜order_items_dataset.csv
 ┃ ┣ 📜order_payments_dataset.csv
 ┃ ┣ 📜order_reviews_dataset.csv
 ┃ ┣ 📜product_category_name_translation.csv
 ┃ ┣ 📜products_dataset.csv
 ┃ ┗ 📜sellers_dataset.csv
 ┃ ┗ 📜df_orders_cleaned.csv
 ┃ ┗ 📜df_products_cleaned.csv
 ┃ ┗ 📜df_reviews_cleaned.csv
 ┣ 📜README.md
 ┣ 📜requirements.txt
 ┗ 📜notebook.ipynb
```


### Install semua dependensi dari requirements.txt
```
pip install -r requirements.txt
```
### Cara Menjalankan streamlit App
```
streamlit run dashboard/dashboard.py
```
### Access The Dashboard Link Below
https://e-commerce-public-datasets-analysis.streamlit.app/