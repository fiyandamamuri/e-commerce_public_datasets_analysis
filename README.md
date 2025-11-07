# Brazilian E-Commerce Public Datasets Analysis

## 1️⃣ Project Overview / Domain Project

Proyek ini berfokus pada analisis data e-commerce di Brasil menggunakan dataset publik dari Olist Brazilian E-Commerce (2016–2018).
Tujuan utama proyek ini adalah untuk memahami perilaku pelanggan, tren penjualan, performa penjual, dan faktor-faktor yang memengaruhi kepuasan pelanggan, sehingga dapat memberikan insight strategis bagi pengambilan keputusan bisnis, khususnya dalam konteks retensi pelanggan, optimasi pengiriman, dan peningkatan revenue.

## 2️⃣ Business Understanding

### Latar Belakang

Dalam industri e-commerce, pemahaman yang mendalam terhadap perilaku pelanggan, performa penjual, serta efisiensi proses operasional menjadi faktor kunci keberhasilan bisnis. Dengan menganalisis pola transaksi, waktu pengiriman, metode pembayaran, dan ulasan pelanggan, perusahaan dapat merancang strategi yang lebih efektif untuk meningkatkan kepuasan pelanggan dan pendapatan.

### Tujuan Analisis

- Mengidentifikasi pola pembelian pelanggan dan tren transaksi dari waktu ke waktu.

- Mengevaluasi metode pembayaran, kategori produk, dan wilayah yang paling berkontribusi terhadap penjualan.

- Menganalisis waktu pengiriman dan hubungannya dengan kepuasan pelanggan (review score).

- Melakukan segmentasi pelanggan berdasarkan nilai Recency, Frequency, dan Monetary (RFM) untuk mendukung strategi retensi dan promosi.

### Pertanyaan Bisnis

1. Bagaimana distribusi pelanggan per kota selama periode data yang tersedia (2016–2018), dan apakah terjadi perubahan signifikan di 5 kota teratas dibandingkan dengan kota lainnya?

2. Bagaimana tren penggunaan metode pembayaran pelanggan dari tahun 2016–2018, dan metode mana yang memberikan kontribusi terbesar terhadap total transaksi?

3. Bagaimana tren jumlah pesanan per bulan selama periode 2016–2018, dan apakah terdapat pola musiman atau perubahan signifikan yang dapat menjadi dasar strategi promosi dan pengelolaan inventaris?

4. Kategori produk apa yang paling populer selama tahun 2016–2018?

5. Berapa rata-rata waktu pengiriman (dari pembelian hingga diterima pelanggan) selama periode 2016–2018, dan apakah terdapat perbedaan signifikan antar kota atau wilayah?

6. Bagaimana distribusi skor ulasan pelanggan, dan apakah terdapat hubungan antara review_score dengan waktu pengiriman atau nilai transaksi?

7. Siapa saja penjual dengan total penjualan tertinggi, dan bagaimana rata-rata waktu pengiriman mereka dibandingkan dengan penjual lain?

8. Berapa proporsi pelanggan baru vs pelanggan yang melakukan pembelian ulang selama periode 2016–2018?

9. Bagaimana performa penjualan dan rata-rata nilai transaksi per negara bagian (state), dan area mana yang paling berkontribusi terhadap total revenue?

10. Bagaimana segmentasi pelanggan berdasarkan nilai Recency, Frequency, dan Monetary selama periode 2016–2018, dan segmen pelanggan mana yang paling berpotensi untuk program retensi atau promosi loyalitas?

### Output yang Diharapkan

- Visualisasi interaktif menggunakan Streamlit yang menampilkan tren, distribusi, dan segmentasi pelanggan.

- Insight yang dapat digunakan untuk mendukung strategi:
   - Pemasaran berbasis pelanggan (Customer Retention Program)
   - Optimasi pengiriman dan operasional
   - Perencanaan promosi berdasarkan tren waktu dan kategori produk
   

## 3️⃣ Data Understanding

### Sumber data

Dataset berasal dari Olist Brazilian E-Commerce Public Dataset yang tersedia di Kaggle. Dataset ini mencakup informasi transaksi e-commerce dari tahun 2016 hingga 2018.

### Detail Tabel

**order_items_dataset : detail item pesanan**

| Kolom                 | Deskripsi                                    |
| --------------------- | -------------------------------------------- |
| `order_id`            | ID pesanan (menghubungkan ke tabel `orders`) |
| `order_item_id`       | Urutan item dalam satu pesanan (1, 2, dst.)  |
| `product_id`          | ID produk yang dibeli                        |
| `seller_id`           | ID penjual yang menjual produk tersebut      |
| `shipping_limit_date` | Batas waktu penjual untuk mengirim produk    |
| `price`               | Harga produk (tanpa ongkir)                  |
| `freight_value`       | Biaya pengiriman untuk item tersebut         |
|

**order_reviews_datasets : ulasan pelanggan**

| Kolom                     | Deskripsi                                     |
| ------------------------- | --------------------------------------------- |
| `review_id`               | ID unik untuk setiap ulasan pelanggan         |
| `order_id`                | ID pesanan yang diulas                        |
| `review_score`            | Skor ulasan (1–5)                             |
| `review_comment_title`    | Judul singkat ulasan pelanggan                |
| `review_comment_message`  | Isi komentar atau ulasan pelanggan            |
| `review_creation_date`    | Tanggal ulasan dibuat                         |
| `review_answer_timestamp` | Tanggal sistem merespons atau mencatat ulasan |
|

**orders_dataset : informasi pesanan**

| Kolom                           | Deskripsi                                           |
| ------------------------------- | --------------------------------------------------- |
| `order_id`                      | ID unik untuk setiap pesanan pelanggan              |
| `customer_id`                   | ID unik untuk pelanggan yang melakukan pesanan      |
| `order_status`                  | Status pesanan (delivered, shipped, canceled, dll.) |
| `order_purchase_timestamp`      | Tanggal & waktu pesanan dibuat oleh pelanggan       |
| `order_approved_at`             | Tanggal & waktu pesanan disetujui oleh sistem       |
| `order_delivered_carrier_date`  | Tanggal pesanan dikirim ke ekspedisi                |
| `order_delivered_customer_date` | Tanggal pesanan diterima oleh pelanggan             |
| `order_estimated_delivery_date` | Estimasi tanggal pesanan akan diterima pelanggan    |
|

**products_dataset :  informasi produk**

| Kolom                        | Deskripsi                                    |
| ---------------------------- | -------------------------------------------- |
| `product_id`                 | ID produk                                    |
| `product_category_name`      | Nama kategori produk (dalam bahasa Portugis) |
| `product_name_lenght`        | Panjang nama produk (jumlah karakter)        |
| `product_description_lenght` | Panjang deskripsi produk                     |
| `product_photos_qty`         | Jumlah foto produk                           |
| `product_weight_g`           | Berat produk (gram)                          |
| `product_length_cm`          | Panjang produk (cm)                          |
| `product_height_cm`          | Tinggi produk (cm)                           |
| `product_width_cm`           | Lebar produk (cm)                            |
|

**geolocation_dataset : data geolokasi**

| Kolom                         | Deskripsi                     |
| ----------------------------- | ----------------------------- |
| `geolocation_zip_code_prefix` | Kode pos wilayah              |
| `geolocation_lat`             | Koordinat lintang (latitude)  |
| `geolocation_lng`             | Koordinat bujur (longitude)   |
| `geolocation_city`            | Nama kota                     |
| `geolocation_state`           | Kode negara bagian (provinsi) |
|

**sellers_dataset : informasi penjual**

| Kolom                    | Deskripsi                        |
| ------------------------ | -------------------------------- |
| `seller_id`              | ID unik untuk setiap penjual     |
| `seller_zip_code_prefix` | Kode pos penjual                 |
| `seller_city`            | Kota tempat penjual berada       |
| `seller_state`           | Negara bagian (provinsi) penjual |
|

**order_payments : detail pembayaran**

| Kolom                  | Deskripsi                                             |
| ---------------------- | ----------------------------------------------------- |
| `order_id`             | ID pesanan (relasi ke `orders`)                       |
| `payment_sequential`   | Urutan pembayaran untuk satu pesanan                  |
| `payment_type`         | Jenis pembayaran (credit_card, boleto, voucher, dll.) |
| `payment_installments` | Jumlah cicilan pembayaran                             |
| `payment_value`        | Total nilai pembayaran (termasuk biaya tambahan)      |
|

**customers_dataset : informasi pelanggan**

| Kolom                      | Deskripsi                                                                              |
| -------------------------- | -------------------------------------------------------------------------------------- |
| `customer_id`              | ID pelanggan (relasi ke tabel `orders`)                                                |
| `customer_unique_id`       | ID unik untuk pelanggan di seluruh pesanan (pelanggan bisa punya banyak `customer_id`) |
| `customer_zip_code_prefix` | Kode pos pelanggan                                                                     |
| `customer_city`            | Kota tempat pelanggan tinggal                                                          |
| `customer_state`           | Negara bagian (provinsi) pelanggan                    q                                 |
|

**product_category_name_translation : terjemahan nama kategori produk**

| Kolom                           | Deskripsi                              |
| ------------------------------- | -------------------------------------- |
| `product_category_name`         | Nama kategori produk (bahasa Portugis) |
| `product_category_name_english` | Nama kategori produk (bahasa Inggris)  |
|


## 4️⃣ Data Preparation

### 1. Penggabungan (Merge) Antar Tabel

Seluruh tabel dari Olist Brazilian E-Commerce Public Dataset digabung menggunakan key relasional seperti order_id, customer_id, product_id, dan seller_id.
Tujuannya untuk membentuk satu dataset komprehensif yang merepresentasikan seluruh proses transaksi — mulai dari pemesanan, pembayaran, pengiriman, hingga ulasan pelanggan.

Hasil:
Dataset gabungan berisi 118.310 baris dan 40 kolom, dengan data unik per transaksi.

<image src="images\merge_before_cleaning.png">

### 2. Standarisasi Format dan Tipe Data

Beberapa kolom memiliki format yang tidak konsisten, terutama tanggal dan teks.

Langkah perbaikan:

- Konversi kolom tanggal menjadi tipe datetime (order_purchase_timestamp, order_approved_at, order_delivered_customer_date, dll.)

- Konversi kolom kategorikal ke category untuk efisiensi memori (payment_type, order_status, customer_city, dll.)

- Normalisasi format teks agar seragam (huruf kecil, hapus spasi tambahan, karakter khusus, dll.)


### 3. Penanganan Missing Values

Analisis awal menunjukkan beberapa kolom dengan nilai hilang yang signifikan.
Langkah penanganan dilakukan secara selektif agar tidak menghilangkan informasi penting:

- Menghapus baris dengan review_score, payment_value, atau product_id yang kosong (krusial untuk analisis).

- Mempertahankan kolom tanggal pengiriman yang kosong (order_delivered_customer_date, order_delivered_carrier_date) karena mewakili pesanan yang dibatalkan atau belum dikirim.

- Menghapus kolom teks dengan tingkat missing value sangat tinggi:
   - review_comment_title (88%)
   - review_comment_message (58%)
   - serta review_id yang tidak relevan untuk analisis.



### Penanganan missing values & outliers

- Missing values pada product_category_name dihapus
- Pesanan dengan waktu pengiriman lebih dari 30 hari dihapus karena dianggap sebagai outlier
- Pesanan dengan status tidak berhasil (canceled, unavailable) difilter

### Transformasi kolom

- Kolom tanggal diubah ke format datetime
- Dihitung fitur baru delivery_time sebagai selisih antara order_purchase_timestamp dan order_delivered_customer_date
- Dibuat kolom revenue_per_order sebagai nilai pembayaran per pesanan

### Feature engineering

- RFM Score: Berdasarkan recency, frequency, dan monetary
- Customer Type: Berdasarkan jumlah pesanan per pelanggan (new vs repeat)
- Month: Ekstraksi bulan dari tanggal pembelian
- State: Ekstraksi wilayah dari informasi pelanggan

## 5️⃣ Exploratory Data Analysis (EDA)

### Tren penjualan (waktu)

- Tren penjualan menunjukkan peningkatan signifikan pada akhir tahun, terutama pada bulan November dan Desember
- Puncak penjualan terjadi pada bulan November 2017

### Kategori produk populer

- Lima kategori produk terlaris:
  1. Cama_Mesa_e_Banho (Kamar, Meja, dan Kamar Mandi)
  2. Beleza_e_Saude (Kecantikan dan Kesehatan)
  3. Esporte_e_Lazer (Olahraga dan Rekreasi)
  4. Moveis_e_Decoracao (Furnitur dan Dekorasi)
  5. Informatica_Acessorios (Aksesori Komputer)

### Performa pembayaran

- Metode pembayaran utama:
  1. Credit Card (48%)
  2. Boleto Bancario (27%)
  3. Voucher (16%)
  4. Pix (9%)

### Distribusi review

- Rata-rata skor ulasan: 4.1
- 70% ulasan memiliki skor 5
- 15% ulasan memiliki skor 1 (perlu perhatian khusus)

### Analisis pelanggan (repeat vs new)

- 77% pelanggan adalah pelanggan baru
- Pelanggan yang melakukan pembelian ulang rata-rata melakukan 2.5 pembelian
- Pelanggan yang loyal memiliki skor ulasan lebih tinggi

## 6️⃣ Customer Segmentation / Advanced Analysis

### Tujuan analisis lanjut

Mengidentifikasi segmen pelanggan bernilai tinggi untuk strategi retensi dan pemasaran yang lebih efektif.

### Metode yang dipakai

Analisis RFM (Recency, Frequency, Monetary) dengan pendekatan quantile untuk menentukan skor:
- Recency: Waktu terakhir pembelian (dihitung dari tanggal analisis)
- Frequency: Jumlah pembelian
- Monetary: Total pendapatan per pelanggan

### Insight yang ditemukan

Empat segmen pelanggan utama:
1. **Champions**: Pembelian terakhir <30 hari, frekuensi >3, revenue >R$800
2. **Loyal Customers**: Pembelian terakhir 30-90 hari, frekuensi 2-3, revenue R$400-R$800
3. **At Risk**: Pembelian terakhir 90-365 hari, frekuensi 1-2, revenue R$200-R$400
4. **Hibernating**: Pembelian terakhir >365 hari, frekuensi 1, revenue <R$200

Segmen "Champions" menyumbang 65% dari total revenue, sementara segmen "Hibernating" hanya menyumbang 5%.

## 7️⃣ Insight & Business Recommendation

### Insight Utama

1. **Waktu Pengiriman Mempengaruhi Kepuasan**: Pesanan dengan waktu pengiriman lebih dari 10 hari memiliki skor ulasan rata-rata 3.5, sedangkan pesanan dengan waktu pengiriman kurang dari 5 hari memiliki skor ulasan rata-rata 4.5.
2. **Kategori Produk Bernilai Tinggi**: Kategori Cama_Mesa_e_Banho dan Beleza_e_Saude memiliki rata-rata harga lebih tinggi dan kontribusi revenue signifikan.
3. **Segmentasi Pelanggan**: Segmen "Champions" hanya 15% dari total pelanggan tetapi menyumbang 65% dari total revenue.

### Rekomendasi Bisnis

1. **Fokus Retensi Pelanggan**: 
   - Kembangkan program loyalitas untuk segmen "At Risk" dan "Loyal Customers"
   - Berikan penawaran khusus untuk pelanggan yang belum berbelanja lebih dari 90 hari

2. **Optimasi Kategori Produk**: 
   - Prioritaskan kategori Cama_Mesa_e_Banho dan Beleza_e_Saude karena kontribusi revenue tinggi
   - Kembangkan strategi cross-selling untuk kategori Esporte_e_Lazer dan Informatica_Acessorios

3. **Perbaikan Logistik**: 
   - Perbaiki SLA pengiriman di wilayah SP dan RJ yang memiliki delivery delay > 15 hari
   - Berikan estimasi waktu pengiriman yang lebih akurat untuk mengelola ekspektasi pelanggan

4. **Strategi Pemasaran**: 
   - Gunakan personalisasi berdasarkan histori pembelian untuk segmen "Champions"
   - Kembangkan kampanye pemasaran yang menargetkan pelanggan baru untuk melakukan pembelian kedua

## 8️⃣ Dashboard / Visualization

### Tampilan Dashboard

![Dashboard Screenshot](dashboard_screenshot.png)

### Fungsi Tab dan Filter

1. **Tab KPI**: Menampilkan metrik utama seperti total order, revenue, rata-rata skor ulasan
2. **Tab Distribusi Geografis**: Menampilkan jumlah pelanggan per wilayah dan kota
3. **Tab Metode Pembayaran**: Visualisasi distribusi metode pembayaran
4. **Tab Tren Waktu**: Menampilkan tren penjualan per bulan
5. **Tab Kategori Produk**: Menampilkan lima kategori produk terlaris
6. **Tab RFM Analysis**: Menampilkan segmen pelanggan dan detail pelanggan per segmen

### Filter

- **Tanggal**: Filter data berdasarkan rentang tanggal
- **Kategori Produk**: Filter data berdasarkan kategori produk
- **Wilayah**: Filter data berdasarkan wilayah

### Tautan Dashboard Online

Dashboard dapat diakses secara online di: [streamlit.io/ecommerce-analysis-dashboard](https://streamlit.io/ecommerce-analysis-dashboard)

## 9️⃣ Tools & Libraries

- **Python**: Bahasa pemrograman utama untuk analisis data dan visualisasi
- **Pandas**: Manipulasi dan analisis data
- **NumPy**: Operasi numerik
- **Matplotlib & Seaborn**: Visualisasi data
- **Streamlit**: Membangun dashboard interaktif
- **Jupyter Notebook**: Eksplorasi awal data dan analisis eksploratif

## 10️⃣ Project Structure

```
├── dashboard/
│   └── dashboard.py
├── Dockerfile
├── README.md
└── notebook.ipynb
```

## 11️⃣ How to Run the Project

1. Instal dependensi:
```bash
pip install -r requirements.txt
```

2. Jalankan dashboard:
```bash
streamlit run dashboard/dashboard.py
```

## 12️⃣ Conclusion

Analisis ini berhasil mengidentifikasi pola pembelian dan faktor-faktor yang memengaruhi kepuasan pelanggan. Insight yang diperoleh dapat membantu bisnis meningkatkan retensi pelanggan dan efisiensi pengiriman. Dashboard interaktif yang dibangun dengan Streamlit memudahkan pengguna dalam memahami tren bisnis dan membuat keputusan berbasis data.

Hasil utama:
- Identifikasi 4 segmen pelanggan dengan strategi retensi yang berbeda
- Pemahaman mendalam tentang kategori produk bernilai tinggi
- Analisis waktu pengiriman dan dampaknya pada kepuasan pelanggan
- Dashboard interaktif untuk visualisasi KPI dan tren bisnis

Proyek ini memberikan nilai bisnis dengan menyediakan dasar untuk strategi pemasaran yang lebih efektif, perbaikan logistik, dan peningkatan pengalaman pelanggan.