# Proyek Analisis Data: E-Commerce Public Dataset

## Deskripsi Proyek

Proyek ini merupakan analisis data terhadap Brazilian E-Commerce Public Dataset yang disediakan oleh Olist. Dataset ini berisi informasi transaksi e-commerce dari tahun 2016 hingga 2018, mencakup berbagai aspek seperti pesanan, pembayaran, produk, pelanggan, penjual, dan ulasan.

Tujuan dari proyek ini adalah untuk memberikan wawasan bisnis berdasarkan data transaksi e-commerce, serta mengelompokkan pelanggan berdasarkan perilaku mereka menggunakan teknik RFM Analysis (Recency, Frequency, Monetary).

## Dataset

### Dataset Utama
[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

Dataset ini berisi informasi dari hampir 100 ribu pesanan dari tahun 2016 hingga 2018 yang dibuat di beberapa marketplace di Brasil. Dataset ini mencakup berbagai tabel yang saling terkait:
- Orders
- Products
- Customers
- Payments
- Reviews
- Sellers
- Geolocation

### Dataset yang Telah Diproses
[Datasets Cleaned](dashboard\datasets_cleaned.csv)

Dataset yang telah dibersihkan dan digabungkan untuk keperluan analisis.

## Struktur Proyek

```
├── dashboard/
│   ├── dashboard.py          # Aplikasi dashboard Streamlit
│   ├── datasets_cleaned.csv  # Dataset yang telah dibersihkan
│   └── dataset-cover.png     # Gambar sampul dataset
├── datasets/                 # Dataset asli dalam bentuk CSV
├── notebook.ipynb            # Notebook untuk eksplorasi data dan analisis awal
├── requirements.txt          # Daftar dependensi Python
└── README.md                 # Dokumen ini
```

## Analisis yang Dilakukan

### 1. Eksplorasi Data Awal (notebook.ipynb)
Notebook ini berisi eksplorasi awal terhadap dataset untuk memahami struktur data, mengidentifikasi missing values, dan melakukan analisis statistik dasar. Beberapa hal yang dianalisis dalam notebook ini meliputi:
- Memahami struktur dan hubungan antar tabel
- Mengidentifikasi dan menangani missing values
- Melakukan analisis statistik deskriptif terhadap data
- Membuat visualisasi awal untuk memahami pola data

### 2. Dashboard Interaktif (dashboard/dashboard.py)
Dashboard ini dibangun menggunakan Streamlit untuk menyajikan hasil analisis secara interaktif dengan dua halaman utama:

#### Halaman Dashboard Utama
Menampilkan berbagai insight bisnis berdasarkan data transaksi, antara lain:
- **KPI Metrics**: Total pesanan, total pendapatan, rata-rata nilai pesanan, dan total pelanggan
- **Top 5 Kota dengan Pelanggan Terbanyak**: Visualisasi horizontal bar chart
- **Distribusi Tipe Pembayaran**: Pie chart distribusi metode pembayaran
- **Tren Pesanan per Bulan**: Line chart tren pesanan dari waktu ke waktu
- **Top 5 Kategori Produk**: Horizontal bar chart kategori produk terlaris

Fitur filter yang tersedia:
- Rentang tanggal
- Kategori produk
- Negara bagian pelanggan

#### Halaman RFM Analysis
RFM Analysis adalah teknik segmentasi pelanggan berdasarkan:
- **Recency (R)**: Seberapa baru pelanggan melakukan transaksi
- **Frequency (F)**: Seberapa sering pelanggan melakukan transaksi
- **Monetary (M)**: Seberapa besar nilai transaksi pelanggan

Dalam halaman ini, pelanggan dikelompokkan menjadi 4 segmen:
1. **Top Customer** (RFM_Score > 4)
2. **High Value Customer** (4 ≥ RFM_Score > 3)
3. **Medium Value Customer** (3 ≥ RFM_Score > 2)
4. **Low Value Customer** (RFM_Score ≤ 2)

Fitur:
- Tabel RFM lengkap dengan skor dan segmentasi
- Filter berdasarkan segmen pelanggan
- Penjelasan kolom dan skor RFM

## Teknologi yang Digunakan

- **Python**: Bahasa pemrograman utama
- **Pandas & NumPy**: Untuk manipulasi dan analisis data
- **Matplotlib & Seaborn**: Untuk visualisasi data
- **Streamlit**: Untuk membuat dashboard interaktif