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
[Link](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

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



**geolocation_dataset : data geolokasi**

| Kolom                         | Deskripsi                     |
| ----------------------------- | ----------------------------- |
| `geolocation_zip_code_prefix` | Kode pos wilayah              |
| `geolocation_lat`             | Koordinat lintang (latitude)  |
| `geolocation_lng`             | Koordinat bujur (longitude)   |
| `geolocation_city`            | Nama kota                     |
| `geolocation_state`           | Kode negara bagian (provinsi) |



**sellers_dataset : informasi penjual**

| Kolom                    | Deskripsi                        |
| ------------------------ | -------------------------------- |
| `seller_id`              | ID unik untuk setiap penjual     |
| `seller_zip_code_prefix` | Kode pos penjual                 |
| `seller_city`            | Kota tempat penjual berada       |
| `seller_state`           | Negara bagian (provinsi) penjual |



**order_payments : detail pembayaran**

| Kolom                  | Deskripsi                                             |
| ---------------------- | ----------------------------------------------------- |
| `order_id`             | ID pesanan (relasi ke `orders`)                       |
| `payment_sequential`   | Urutan pembayaran untuk satu pesanan                  |
| `payment_type`         | Jenis pembayaran (credit_card, boleto, voucher, dll.) |
| `payment_installments` | Jumlah cicilan pembayaran                             |
| `payment_value`        | Total nilai pembayaran (termasuk biaya tambahan)      |



**customers_dataset : informasi pelanggan**

| Kolom                      | Deskripsi                                                                              |
| -------------------------- | -------------------------------------------------------------------------------------- |
| `customer_id`              | ID pelanggan (relasi ke tabel `orders`)                                                |
| `customer_unique_id`       | ID unik untuk pelanggan di seluruh pesanan (pelanggan bisa punya banyak `customer_id`) |
| `customer_zip_code_prefix` | Kode pos pelanggan                                                                     |
| `customer_city`            | Kota tempat pelanggan tinggal                                                          |
| `customer_state`           | Negara bagian (provinsi) pelanggan                                                     |



**product_category_name_translation : terjemahan nama kategori produk**

| Kolom                           | Deskripsi                              |
| ------------------------------- | -------------------------------------- |
| `product_category_name`         | Nama kategori produk (bahasa Portugis) |
| `product_category_name_english` | Nama kategori produk (bahasa Inggris)  |




## 4️⃣ Data Preparation

### 2. Penggabungan (Merge) Antar Tabel

Seluruh tabel dari Olist Brazilian E-Commerce Public Dataset digabung menggunakan key relasional seperti order_id, customer_id, product_id, dan seller_id.
Tujuannya untuk membentuk satu dataset komprehensif yang merepresentasikan seluruh proses transaksi — mulai dari pemesanan, pembayaran, pengiriman, hingga ulasan pelanggan.

<image src="images\merge_before_cleaning.png">

### 2. Pemeriksaan Duplikasi Data

Langkah awal adalah memastikan tidak ada baris duplikat yang dapat menyebabkan bias pada hasil analisis.

<image src="images\duplicates.png">


### 3. Standarisasi Tipe Data

Tipe data setiap kolom disesuaikan dengan makna sebenarnya agar analisis lebih akurat dan efisien.

Langkah-langkah yang dilakukan:

- Mengonversi kolom bertipe waktu menjadi datetime

- Mengonversi kolom kategorikal menjadi category

- Menyesuaikan kolom numerik menjadi int atau float

- Memastikan seluruh kolom ID bertipe string

<image src="images\ubah_tipe_data.png">

### 4. Penanganan Missing Values

Langkah ini dilakukan untuk memastikan hanya data yang relevan dan lengkap yang digunakan dalam analisis.
Pendekatan yang digunakan bersifat selektif:

Menghapus baris dengan missing value pada kolom penting seperti:
- review_score

- Dimensi produk (product_weight_g, product_length_cm, product_height_cm, product_width_cm)

- Detail produk (product_category_name, product_name_lenght, product_description_lenght, product_photos_qty)

- Informasi pembayaran (payment_type, payment_installments, payment_value)

- Mempertahankan nilai kosong pada kolom tanggal pengiriman (order_delivered_customer_date, order_delivered_carrier_date) karena mewakili pesanan yang dibatalkan atau belum dikirim.

<image src="images\remove_missing_values.png">


### 5. Menghapus Kolom yang Tidak Relevan

Beberapa kolom dihapus karena memiliki nilai hilang sangat besar atau tidak memberikan informasi berarti bagi analisis.

<image src="images\column_not_use.png">

### 6. Pemeriksaan Akhir Data

Setelah proses cleaning, dataset diperiksa kembali untuk memastikan struktur dan tipe data sudah sesuai.

<image src="images\data_final_cleaning.png">

Output ringkas:
- Jumlah baris: 115.608
- Jumlah kolom: 36
- Tipe data: 7 kategorikal, 8 datetime, 13 numerik, 5 string, dan 3 integer
- Hanya beberapa kolom waktu seperti order_approved_at, order_delivered_carrier_date, dan order_delivered_customer_date masih memiliki sedikit nilai kosong (1–2%) — yang sengaja dipertahankan karena bisa menggambarkan pesanan yang belum terkirim atau dibatalkan.


## 5️⃣ Exploratory Data Analysis (EDA)

### Distribusi pelanggan per kota & negara bagian

<image src="images\EDA1.png">

**Insight :**
- Sebaran pelanggan tidak merata, terkonsentrasi di wilayah perkotaan besar.
- Kota São Paulo memiliki jumlah pelanggan tertinggi (18.267 pelanggan), jauh di atas kota lainnya.
- Top 3 kota (São Paulo, Rio de Janeiro, Belo Horizonte) menyumbang lebih dari 30% total pelanggan.
- Sebagian besar pelanggan berasal dari negara bagian SP (São Paulo) dengan 48.797 pelanggan, diikuti RJ (Rio de Janeiro) dan MG (Minas Gerais).
- Wilayah bagian selatan dan tenggara Brasil (SP, RJ, MG, RS, PR, SC) menjadi pasar utama platform e-commerce ini.
- Negara bagian bagian utara seperti Roraima, Amapá, dan Acre memiliki pelanggan sangat sedikit → potensi ekspansi pasar masih terbuka.

### Tren metode pembayaran & kontribusi

<image src="images\EDA2.png">

**Insight :**
- Credit card menjadi metode pembayaran paling dominan dengan proporsi 73,8% dari total transaksi, menandakan preferensi pelanggan terhadap kemudahan dan fleksibilitas pembayaran.
- Boleto (transfer bank lokal Brasil) masih cukup populer (19,5%), menunjukkan masih adanya segmen pelanggan yang memilih metode pembayaran tradisional.
- Voucher dan debit card memiliki proporsi kecil (masing-masing 5,3% dan 1,4%), kemungkinan digunakan dalam promo atau segmen pelanggan tertentu.
- Rata-rata nilai transaksi tertinggi juga berasal dari credit card (≈179 BRL) dan boleto (≈177 BRL) → menandakan metode ini umum digunakan untuk pembelian dengan nilai tinggi.
- Voucher memiliki nilai transaksi terendah (≈64 BRL) → cenderung digunakan untuk pembelian kecil atau diskon promosi.

### Tren jumlah pesanan per bulan

<image src="images\EDA3.png">

**Insight :**
- Aktivitas transaksi mulai meningkat signifikan sejak awal 2017, menunjukkan ekspansi atau peningkatan adopsi platform e-commerce.
- Puncak pesanan terjadi pada November 2017 (7.284 pesanan) — kemungkinan besar dipengaruhi oleh promosi besar seperti Black Friday.
- Setelah puncak tersebut, volume pesanan tetap stabil tinggi sepanjang 2018, rata-rata 6.000–7.000 pesanan per bulan, menunjukkan pertumbuhan yang berkelanjutan.
- Data tahun 2016 dan akhir 2018 tidak lengkap, sehingga analisis tren utama lebih relevan difokuskan pada tahun 2017–2018.
- Tidak terlihat pola musiman yang sangat kuat selain lonjakan di akhir tahun, mengindikasikan potensi peningkatan permintaan pada periode promosi akhir tahun.

### Kategori produk paling populer

<image src="images\EDA4.png">

**Insight :**
- Kategori “bed_bath_table” menjadi yang paling banyak dibeli, menunjukkan tingginya permintaan untuk produk rumah tangga dan dekorasi.
- Kategori “health_beauty” dan “sports_leisure” juga menempati posisi teratas, mengindikasikan tren konsumen terhadap gaya hidup sehat dan perawatan diri.
- Dominasi kategori furniture_decor dan housewares memperkuat bahwa segmen rumah tangga adalah pasar utama platform ini.
- Produk seperti computers_accessories dan telephony menunjukkan adanya permintaan stabil untuk barang elektronik dan gadget.

### Rata-rata waktu pengiriman

<image src="images\EDA5.png">

**Insight :**
- Rata-rata waktu pengiriman keseluruhan adalah sekitar 12 hari, menunjukkan proses logistik yang cukup efisien mengingat cakupan wilayah nasional.
- Kota dengan waktu pengiriman tercepat seperti Iomere dan Contenda hanya memerlukan 2–3 hari, kemungkinan karena lokasi dekat dengan pusat distribusi utama.
- Negara bagian São Paulo (SP) memiliki waktu pengiriman tercepat (~8 hari), mendukung hipotesis bahwa wilayah ini adalah pusat logistik dan ekonomi utama.
- Wilayah seperti Goiás (GO), Mato Grosso do Sul (MS), dan Espírito Santo (ES) memiliki waktu pengiriman lebih lama (sekitar 15 hari), kemungkinan akibat jarak geografis atau keterbatasan infrastruktur logistik.

### Distribusi skor ulasan & korelasi dengan waktu pengiriman

<image src="images\EDA6.png">

**Insight :**
- Mayoritas pelanggan memberikan skor tinggi (4–5 bintang), dengan lebih dari 85% ulasan berada pada rentang tersebut. Ini menunjukkan kepuasan pelanggan secara umum cukup baik.
- Skor 5 bintang mendominasi dengan >65 ribu ulasan, sedangkan skor rendah (1–2 bintang) hanya sebagian kecil dari total.
- Korelasi negatif sebesar -0.30 antara review_score dan delivery_time menunjukkan bahwa semakin lama waktu pengiriman, semakin rendah skor ulasan yang diberikan pelanggan.
- Artinya, kecepatan pengiriman memiliki pengaruh nyata terhadap kepuasan pelanggan dan menjadi faktor penting untuk diprioritaskan.

### Penjual dengan total penjualan tertinggi dan rata" waktu pengirimannya

<image src="images\EDA7.png">

**Insight :**
- Penjual dengan ID 7c67e1448b00f6e969d365cea6b010ab mendominasi dengan total penjualan sebesar ±R$509.474, jauh lebih tinggi dibandingkan penjual lain di daftar.
- Terdapat gap yang cukup besar antara penjual pertama dan posisi kedua (selisih hampir R$200.000), menandakan adanya ketimpangan kontribusi pendapatan antar penjual.
- Rata-rata waktu pengiriman penjual teratas adalah 22 hari, termasuk yang paling lama dibandingkan penjual lain di 10 besar — ini menunjukkan bahwa volume tinggi tidak selalu diikuti efisiensi pengiriman.
- Sebaliknya, beberapa penjual dengan penjualan menengah (misalnya da8622b14eb17ae2831f4ac5b9dab84a dan 955fee9216a65b617aa5c0531780ce60) memiliki rata-rata waktu pengiriman cepat (≈10–11 hari), menandakan potensi keunggulan operasional meski volume penjualan belum setinggi penjual top.

### Proporsi pelanggan baru vs repeat

<image src="images\EDA8.png">

**Insight :**
- Sekitar 97% dari seluruh transaksi berasal dari pelanggan baru, sedangkan hanya 3% berasal dari pelanggan repeat (pembelian ulang).
- Hal ini menunjukkan bahwa akuisisi pelanggan baru berjalan sangat baik, tetapi tingkat retensi pelanggan masih rendah.
- Rendahnya proporsi pelanggan repeat bisa menjadi indikasi kurangnya loyalitas pelanggan atau belum adanya program retensi dan promosi berkelanjutan.
- Peluang besar untuk bisnis: mengembangkan strategi retensi seperti program loyalitas, diskon pembelian kedua, atau personalisasi penawaran untuk meningkatkan repeat purchase rate.

### Penjualan per negara bagian

<image src="images\EDA9.png">

**Insight :**
- Negara bagian São Paulo (SP) mendominasi total pendapatan dengan > 7,5 juta, jauh di atas wilayah lain.
- Disusul oleh Rio de Janeiro (RJ) dan Minas Gerais (MG), masing-masing sekitar 2,7 juta dan 2,3 juta, menunjukkan bahwa wilayah tenggara Brasil menjadi pusat utama aktivitas e-commerce.
- Wilayah selatan seperti Rio Grande do Sul (RS) dan Paraná (PR) juga berkontribusi signifikan, masing-masing di atas 1 juta.
- Negara bagian di wilayah utara dan timur laut seperti Roraima (RR), Amapá (AP), dan Acre (AC) memiliki kontribusi pendapatan yang sangat kecil (< 30 ribu), menandakan potensi pasar yang belum tergarap.
- Secara keseluruhan, distribusi penjualan sangat terpusat di kota-kota besar dan wilayah ekonomi maju, sehingga strategi ekspansi atau promosi bisa difokuskan ke wilayah dengan penetrasi rendah namun populasi berkembang.

## 6️⃣ Customer Segmentation / Advanced Analysis

### Tujuan analisis lanjut

Mengidentifikasi segmen pelanggan bernilai tinggi untuk strategi retensi dan pemasaran yang lebih efektif.

### Metode yang dipakai

Analisis RFM (Recency, Frequency, Monetary) dengan pendekatan quantile untuk menentukan skor:
- Recency: Waktu terakhir pembelian (dihitung dari tanggal analisis)
- Frequency: Jumlah pembelian
- Monetary: Total pendapatan per pelanggan

### Insight yang ditemukan

<image src="images\EDA10.png">

<image src="images\EDA11.png">

<image src="images\EDA12.png">

**Insight :**
- Segmen **Medium Value** mendominasi dengan proporsi hampir 49% dari total pelanggan, diikuti oleh **Low Value** sebesar 42,6%, dan **High Value** hanya 8,6%.
- Pelanggan **High Value** memiliki frekuensi pembelian tinggi dan nilai transaksi besar (hingga R$27.935), berkontribusi signifikan terhadap total pendapatan.
- Mayoritas pelanggan masih tergolong **Medium dan Low Value**, menunjukkan potensi besar untuk peningkatan loyalitas dan nilai transaksi.
- Strategi retensi perlu difokuskan pada **High Value** untuk menjaga kontribusi pendapatan, sementara **Medium Value** dapat ditingkatkan melalui program loyalitas atau promosi personalisasi.
- Segmen **Low Value** perlu strategi reaktivasi seperti penawaran diskon atau kampanye retargeting untuk meningkatkan engagement dan konversi ulang.

## 7️⃣ Insight & Business Recommendation

#### Pertanyaan 1: Bagaimana distribusi pelanggan per kota selama periode 2016–2018, dan apakah terdapat perubahan signifikan di 5 kota teratas dibandingkan kota lainnya?

#### **Insight:**
- Distribusi pelanggan sangat tidak merata — terkonsentrasi kuat di wilayah perkotaan besar.
- Kota São Paulo mendominasi dengan 18 ribu+ pelanggan, jauh di atas kota lain.
- Top 3 kota (São Paulo, Rio de Janeiro, Belo Horizonte) menyumbang >30% total pelanggan.
- Sebagian besar pelanggan berasal dari wilayah Selatan & Tenggara (SP, RJ, MG, RS, PR, SC).
- Wilayah Utara & Timur Laut masih memiliki penetrasi pelanggan sangat rendah.

#### **Rekomendasi Bisnis:**
- Fokuskan strategi retensi & personalisasi promosi di kota besar untuk memperkuat loyalitas pelanggan utama.
- Jalankan ekspansi pasar & optimasi logistik di wilayah utara (seperti Roraima, Amapá, Acre) untuk menjangkau area dengan potensi pertumbuhan baru.
- Gunakan analisis demografis & segmentasi geografis untuk menyesuaikan kampanye marketing dan penawaran produk sesuai karakteristik regional.

---

#### Pertanyaan 2: Bagaimana tren penggunaan metode pembayaran pelanggan dari tahun 2016–2018, dan metode mana yang memberikan kontribusi terbesar terhadap total nilai transaksi?

#### **Insight:**
- Kartu kredit mendominasi dengan kontribusi ~74% dari total transaksi dan nilai transaksi rata-rata tertinggi (R$179).
- Boleto (transfer bank lokal) menempati posisi kedua (~19%) dengan nilai transaksi hampir setara dengan kartu kredit.
- Voucher (5%) digunakan untuk pembelian bernilai kecil (R$64) — kemungkinan terkait promo atau diskon.
- Debit card (1,4%) memiliki pangsa pasar paling rendah dan tidak signifikan terhadap total transaksi.

#### **Rekomendasi Bisnis:**
- Optimalkan pengalaman pembayaran digital dengan memastikan integrasi payment gateway yang lancar untuk kartu kredit.
- Pertimbangkan kerja sama dengan bank/kartu kredit untuk program cashback atau cicilan 0% guna meningkatkan conversion rate dan average order value (AOV).
- Tetap sediakan opsi boleto untuk menjangkau pelanggan yang belum memiliki akses kartu kredit, sambil mempercepat proses verifikasinya.
- Gunakan voucher sebagai strategi promosi atau reaktivasi pelanggan dorman, dan evaluasi efektivitas debit card dibanding alternatif baru seperti e-wallet atau BNPL.

---

#### Pertanyaan 3: Bagaimana tren jumlah pesanan per bulan selama periode 2016–2018, dan apakah terdapat pola musiman atau perubahan signifikan yang dapat menjadi dasar strategi promosi dan pengelolaan inventaris?

#### **Insight:**
- Jumlah pesanan meningkat tajam dari tahun 2016 hingga puncaknya di akhir 2017 dan awal 2018.
- Terjadi lonjakan signifikan pada November 2017 (7.284 pesanan) — kemungkinan besar dipicu oleh event Black Friday dan promosi akhir tahun.
- Aktivitas penjualan tetap tinggi hingga Desember 2017 dan Januari–Maret 2018, menunjukkan efek berkelanjutan dari momentum promosi.
- Setelah pertengahan 2018, tren mulai stabil dengan sedikit penurunan di bulan Juni–Agustus, menandakan periode penjualan normal (off-peak).
- Secara umum, pola menunjukkan musim belanja meningkat di Q4 setiap tahun, cocok untuk strategi promosi tahunan.

#### **Rekomendasi Bisnis:**
- Gunakan data tren musiman ini untuk merencanakan stok dan kampanye promosi besar di Q4 (Oktober–Desember).
- Tingkatkan kapasitas logistik dan persediaan menjelang Black Friday untuk menghindari keterlambatan pengiriman.
- Manfaatkan periode off-peak (Mei–Agustus) untuk campaign reaktivasi pelanggan atau bundling promo guna menjaga stabilitas penjualan.
- Lakukan forecasting permintaan tahunan berbasis pola historis agar strategi inventory dan marketing lebih presisi.

---

#### Pertanyaan 4: Kategori produk apa yang paling populer selama periode 2016–2018?

#### **Insight:**
- Kategori bed_bath_table menjadi yang paling populer dengan 11.847 transaksi, menandakan tingginya permintaan untuk kebutuhan rumah tangga.
- Health_beauty (9.944) dan sports_leisure (8.942) juga menempati posisi atas, mencerminkan tren konsumen yang semakin fokus pada gaya hidup sehat dan perawatan diri
- Furniture_decor dan computers_accessories masuk 5 besar, menunjukkan keseimbangan antara kebutuhan fungsional (perabot rumah) dan digital (teknologi).
- Pola ini menggambarkan bahwa platform e-commerce memiliki basis pelanggan luas dengan dominasi produk-produk consumer goods dan lifestyle.

#### **Rekomendasi Bisnis:**
- Fokuskan strategi pemasaran dan stok pada kategori home living dan personal care, terutama menjelang musim promosi besar.
- Buat cross-selling campaign antara kategori saling terkait, seperti bed_bath_table dengan furniture_decor, atau health_beauty dengan sports_leisure.
- Perkuat manajemen inventaris dan suplai untuk produk dengan volume tinggi agar menghindari kekosongan stok saat puncak permintaan.
- Untuk kategori dengan transaksi sedang seperti telephony dan auto, pertimbangkan promosi bundling atau diskon targeted untuk meningkatkan penetrasi pasar.

---

#### Pertanyaan 5: Berapa rata-rata waktu pengiriman dari pembelian hingga diterima pelanggan selama periode 2016–2018, dan apakah terdapat perbedaan signifikan antar kota atau wilayah?

#### **Insight:**
- Rata-rata waktu pengiriman keseluruhan adalah ±12 hari sejak pembelian hingga pesanan diterima pelanggan.
- Pengiriman tercepat terjadi di kota-kota kecil seperti Iomere (2 hari) dan Contenda (3 hari), kemungkinan karena kedekatan geografis dengan pusat distribusi.
- Berdasarkan wilayah, negara bagian São Paulo (SP) memiliki waktu pengiriman tercepat (8,26 hari) dibandingkan wilayah lain seperti Rio de Janeiro (14,72 hari) dan Espírito Santo (15,07 hari).
- Hal ini menunjukkan adanya kesenjangan efisiensi logistik antar wilayah, dengan wilayah Tenggara (terutama SP) lebih unggul dalam infrastruktur distribusi.

#### **Rekomendasi Bisnis:**
- Perkuat kemitraan logistik di luar SP, terutama di wilayah timur dan selatan, untuk menekan waktu pengiriman di atas rata-rata.
- Evaluasi lokasi gudang dan rute distribusi agar lebih dekat dengan area konsentrasi pelanggan, seperti RJ dan MG.
- Terapkan analisis SLA (Service Level Agreement) untuk memonitor performa pengiriman per wilayah dan mitra logistik.
- Komunikasikan estimasi pengiriman yang realistis kepada pelanggan untuk meningkatkan kepuasan dan kepercayaan terhadap platform.

---

#### Pertanyaan 6: Bagaimana distribusi skor ulasan pelanggan, dan apakah terdapat hubungan antara review_score dengan waktu pengiriman atau nilai transaksi?

#### **Insight:**
- Skor ulasan pelanggan didominasi oleh rating 5 (56%) dan rating 4 (19%), menunjukkan tingkat kepuasan pelanggan yang tinggi secara umum.
- Namun, rating 1 dan 2 masih menyumbang sekitar 16% dari total ulasan, menandakan adanya pengalaman negatif yang perlu dievaluasi.
- Ditemukan korelasi negatif moderat antara review_score dan delivery_time (r = -0.30) — semakin lama pengiriman, semakin rendah skor ulasan yang diberikan pelanggan.
- Tidak ditemukan korelasi kuat antara skor ulasan dan nilai transaksi, mengindikasikan kepuasan pelanggan lebih dipengaruhi oleh kecepatan dan ketepatan pengiriman dibanding nilai pembelian.

#### **Rekomendasi Bisnis:**
- Fokus pada optimalisasi waktu pengiriman sebagai faktor utama peningkatan kepuasan pelanggan.
- Gunakan SLA tracking dan notifikasi real-time untuk mengurangi ketidakpastian pelanggan selama pengiriman.
- Evaluasi ulang mitra logistik dengan performa di bawah standar, terutama di wilayah dengan waktu pengiriman tinggi.
- Lakukan analisis teks review lebih lanjut untuk mengidentifikasi penyebab utama keluhan, lalu tindaklanjuti dengan customer experience improvement plan.

---

#### Pertanyaan 7: Siapa penjual dengan total penjualan tertinggi selama periode 2016–2018, dan bagaimana rata-rata waktu pengiriman mereka dibandingkan penjual lainnya?

#### **Insight:**
- Seller ID `7c67e1448b00f6e969d365cea6b010ab` menempati posisi penjual dengan total penjualan tertinggi sebesar R$509.474, namun memiliki rata-rata waktu pengiriman paling lama (22 hari) di antara 10 besar penjual.
- Sebaliknya, beberapa penjual dengan penjualan tinggi seperti `da8622b14eb17ae2831f4ac5b9dab84a` dan `955fee9216a65b617aa5c0531780ce60` menunjukkan kinerja logistik jauh lebih cepat (≈10–11 hari) sambil tetap mencatat nilai penjualan besar (>R$230.000).
- Pola ini menunjukkan bahwa tinggi rendahnya penjualan tidak selalu sejalan dengan efisiensi pengiriman — kemungkinan karena perbedaan jenis produk, lokasi gudang, atau volume pesanan besar yang memperpanjang waktu pemrosesan.
- Secara keseluruhan, top seller berperan besar dalam pendapatan platform dan menjadi kunci untuk menjaga kualitas pengalaman pelanggan.

#### **Rekomendasi Bisnis:**
- Lakukan benchmark waktu pengiriman antar top seller untuk mengidentifikasi hambatan operasional pada penjual dengan durasi pengiriman tinggi.
- Berikan insentif logistik (prioritas pengiriman, dukungan fulfillment) bagi penjual berpenjualan tinggi namun lambat dalam pengiriman.
- Gunakan seller performance dashboard yang menampilkan delivery time vs sales volume sebagai indikator utama untuk pemantauan rutin.
- Evaluasi apakah integrasi gudang regional atau dropship system dapat membantu menurunkan waktu pengiriman tanpa mengorbankan volume penjualan.

---

#### Pertanyaan 8: Berapa proporsi pelanggan baru dibanding pelanggan yang melakukan pembelian ulang selama periode 2016–2018?

#### **Insight:**
- Pelanggan baru mendominasi transaksi dengan proporsi ≈97%, sedangkan pelanggan repeat hanya menyumbang sekitar 3% dari total pembelian selama 2016–2018.
- Angka ini menunjukkan bahwa mayoritas pendapatan masih berasal dari akuisisi pelanggan baru, bukan dari retensi pelanggan lama.
- Rendahnya repeat purchase dapat menandakan kurangnya program loyalitas, personalisasi rekomendasi produk, atau strategi retensi yang efektif.

#### **Rekomendasi Bisnis:**
- Fokus pada retensi pelanggan — bangun program loyalty points, voucher re-purchase, atau diskon pembelian berikutnya untuk mendorong pelanggan melakukan pembelian ulang.
- Implementasikan email marketing berbasis histori pembelian dan rekomendasi produk personal agar pelanggan terdorong kembali bertransaksi.
- Lakukan analisis cohort untuk memahami kapan pelanggan cenderung berhenti membeli, sehingga dapat diintervensi lebih awal dengan promosi atau kampanye retensi.
- Jaga keseimbangan strategi antara akuisisi pelanggan baru dan peningkatan Customer Lifetime Value (CLV) dari pelanggan yang sudah ada.

---

#### Pertanyaan 9: Bagaimana performa penjualan dan rata-rata nilai transaksi per negara bagian (state), dan wilayah mana yang berkontribusi paling besar terhadap total pendapatan?

#### **Insight:**
- Negara bagian São Paulo (SP) menjadi kontributor utama pendapatan dengan total R$ 7,5 juta, jauh melampaui provinsi lainnya.
- Diikuti oleh Rio de Janeiro (R$ 2,7 juta) dan Minas Gerais (R$ 2,3 juta) — tiga wilayah ini secara kolektif menyumbang lebih dari 50% total pendapatan nasional.
- Secara geografis, wilayah tenggara Brasil menjadi pusat aktivitas ekonomi e-commerce terbesar, mencerminkan konsentrasi populasi urban dan daya beli yang tinggi.
- Sementara itu, wilayah utara dan timur laut (seperti Roraima, Amapá, Acre) memiliki kontribusi yang sangat kecil (<1%), menunjukkan potensi pasar yang belum tergarap secara optimal.

#### **Rekomendasi Bisnis:**
- Fokus retensi & upselling di wilayah performa tinggi seperti SP, RJ, dan MG untuk memaksimalkan pendapatan dari pelanggan loyal.
- Perluas penetrasi pasar ke wilayah berkontribusi rendah (utara & timur laut) melalui:
   - Ekspansi logistik (mitra pengiriman lokal & warehouse regional)
   - Promosi spesifik wilayah & kampanye edukasi e-commerce
   - Penawaran gratis ongkir atau cicilan ringan untuk mengatasi hambatan pembelian
- Gunakan insight ini untuk alokasi anggaran iklan dan stok produk secara regional, agar supply dan permintaan lebih seimbang serta biaya operasional lebih efisien.


---

### **Segmentasi Pelanggan (RFM)**

#### **Insight:**
- Mayoritas pelanggan (>90%) termasuk kategori Low & Medium Value, menunjukkan potensi besar untuk aktivasi ulang dan retensi.
- Segmen High Value meskipun kecil (8.6%), berperan penting dalam profitabilitas jangka panjang dan layak menjadi target utama program loyalitas premium.
- Pelanggan Low Value dapat diarahkan ke strategi edukasi atau promosi khusus untuk meningkatkan frekuensi pembelian.

#### **Rekomendasi Bisnis:**
- High Value Customers (Top 8.6%)
   - Program Loyalty Membership / VIP Tier : Akses eksklusif, early sale access, cashback khusus.
   - Personalized marketing: rekomendasi produk berdasarkan histori pembelian.
   - Jaga retensi dengan thank-you campaign & feedback loop.

- Medium Value Customers (~49%)
   - Program upselling dan cross-selling produk relevan.
   - Dorong menjadi pelanggan aktif dengan voucher frekuensi pembelian (contoh: diskon pembelian ke-3).
   - Kirim reminder berbasis waktu (“You haven’t shopped in a while!”).

- Low Value Customers (~43%)
   - Gunakan email reactivation atau promosi onboarding untuk menarik kembali.
   - Analisis lebih lanjut untuk mengetahui apakah mereka baru atau churn.

---

## 8️⃣ Dashboard / Visualization

### Tampilan Dashboard

<img src="images\dashboard-viz.png">

### Fungsi Tab dan Filter

1. **Tab Overview**: Menampilkan Total Revenue, Jumlah Pesanan, Rata-rata Nilai Order, Rata-rata Waktu Pengiriman, Trend Penjualan Bulanan, Penjualan per Negara Bagian
2. **Tab Customer**: Menampilkan Top 10 Kota dengan Pelanggan Terbanyak, Proporsi Pelanggan Baru vs Repeat, Pemetaan Pelanggan Berdasarkan Frequency & Monetary, RFM Heatmap, Table RFM Pelanggan
3. **Tab Payment**: Menampilkan Distribusi Metode Pembayaran, Rata-rata Nilai Transaksi per Metode
4. **Tab Product & Seller**: Menampilkan Top 10 Kategori Produk Paling Populer, Top 10 Penjual dengan Penjualan Tertinggi
5. **Tab Review & Delivery**: Menampilkan Distribusi skor ulasan, Korelasi antara waktu pengiriman dan skor ulasan

### Filter

- **Date Range**: Filter data berdasarkan rentang tanggal
- **Negara Bagian**: Filter data berdasarkan negara bagian
- **Kategori Produk**: Filter data berdasarkan kategori produk
- **Metode Pembayaran**: Filter data berdasarkan metode pembayaran

### Tautan Dashboard Online

Dashboard dapat diakses secara online di: [https://e-commerce-public-datasets-analysis.streamlit.app/](https://e-commerce-public-datasets-analysis.streamlit.app/)

## 9️⃣ Tools & Libraries

- **Python**: Bahasa pemrograman utama untuk analisis data dan visualisasi
- **Pandas**: Manipulasi dan analisis data
- **NumPy**: Operasi numerik
- **Matplotlib & Seaborn**: Visualisasi data
- **Streamlit**: Membangun dashboard interaktif
- **Jupyter Notebook**: Eksplorasi awal data dan analisis eksploratif

## 1️⃣0️⃣ Project Structure

```
├── dashboard/
│   ├── cleaned_merged_data.csv
│   └── dashboard.py
├── datasets/
├── images/
├── Dockerfile
├── README.md
├── requirements.txt
└── notebook.ipynb

```

## 1️⃣1️⃣ How to Run the Project

1. Instal dependensi:
```bash
pip install -r requirements.txt
```

2. Jalankan dashboard:
```bash
streamlit run dashboard/dashboard.py
```

