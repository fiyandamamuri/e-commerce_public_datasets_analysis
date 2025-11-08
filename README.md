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
Distribusi pelanggan e-commerce selama periode 2016–2018 menunjukkan konsentrasi geografis yang sangat tinggi di kota-kota besar Brasil. São Paulo mendominasi dengan 18.267 pelanggan (hampir 20% dari total), diikuti Rio de Janeiro dengan 8.022 pelanggan—menciptakan gap signifikan dibandingkan kota-kota lainnya. Dari perspektif negara bagian, SP (São Paulo state) mencakup lebih dari 52% total pelanggan dengan 48.797 pelanggan, mengonfirmasi dominasi wilayah Tenggara sebagai pusat aktivitas e-commerce. Lima kota teratas (São Paulo, Rio de Janeiro, Belo Horizonte, Brasília, dan Curitiba) tetap konsisten selama periode analisis tanpa perubahan signifikan dalam ranking, menunjukkan stabilitas pola konsumsi geografis yang kuat.

#### **Rekomendasi Bisnis:**
Kesenjangan besar antara kota-kota tier-1 dan tier-2 mengindikasikan perlunya strategi penetrasi pasar yang disesuaikan: mempertahankan dominasi di kota besar melalui program loyalitas dan peningkatan customer experience, sambil mengeksplorasi peluang pertumbuhan di kota-kota sekunder yang masih underserved melalui kampanye marketing lokal dan partnership dengan influencer regional. Konsentrasi pelanggan yang tinggi di beberapa kota juga memberikan peluang untuk optimalisasi logistik—mengembangkan distribution center atau warehouse di hub utama (SP, RJ, MG) untuk mengurangi biaya pengiriman dan waktu delivery, serta mempertimbangkan model fulfillment yang lebih fleksibel untuk menjangkau wilayah geografis yang lebih luas dengan efisien.

---

#### Pertanyaan 2: Bagaimana tren penggunaan metode pembayaran pelanggan dari tahun 2016–2018, dan metode mana yang memberikan kontribusi terbesar terhadap total nilai transaksi?

#### **Insight:**
Selama periode 2016–2018, metode pembayaran kartu kredit mendominasi secara absolut dengan proporsi 73,8% dari total transaksi dan rata-rata nilai transaksi tertinggi sebesar R$179, mengonfirmasi preferensi pelanggan terhadap kemudahan, fleksibilitas, dan keamanan pembayaran digital. Boleto (metode transfer bank lokal Brasil) menempati posisi kedua dengan 19,5% proporsi dan rata-rata nilai transaksi R$177—hampir setara dengan kartu kredit—menunjukkan bahwa segmen pelanggan tertentu masih memilih metode pembayaran tradisional, kemungkinan karena tidak memiliki akses ke kartu kredit atau lebih percaya pada sistem pembayaran lokal. Voucher dan debit card memiliki kontribusi minimal (5,3% dan 1,4%), dengan voucher mencatat nilai transaksi terendah (R$64), mengindikasikan penggunaan terbatas pada pembelian bernilai kecil atau dalam konteks program promosi dan diskon.

#### **Rekomendasi Bisnis:**
Mengingat dominasi kartu kredit, platform harus memastikan integrasi payment gateway yang optimal dengan proses checkout yang seamless, serta mempertimbangkan kerjasama dengan penyedia kartu kredit untuk program cashback atau cicilan 0% guna meningkatkan conversion rate dan average order value. Untuk boleto yang masih signifikan (hampir 20% transaksi), penting untuk mempertahankan metode ini sebagai opsi pembayaran mengingat penetrasi kartu kredit yang belum merata di seluruh Brasil, sambil mengoptimalkan proses verifikasi pembayaran boleto untuk mengurangi fraud dan mempercepat fulfillment. Voucher dapat dimanfaatkan lebih strategis sebagai tool untuk akuisisi pelanggan baru atau reaktivasi pelanggan dorman melalui targeted campaign, sementara rendahnya penggunaan debit card (1,4%) mengindikasikan perlunya evaluasi apakah metode ini perlu dipertahankan atau digantikan dengan alternatif pembayaran digital lain yang lebih populer seperti digital wallet atau BNPL (Buy Now Pay Later) untuk mengakomodasi evolusi preferensi pembayaran pelanggan.

---

#### Pertanyaan 3: Bagaimana tren jumlah pesanan per bulan selama periode 2016–2018, dan apakah terdapat pola musiman atau perubahan signifikan yang dapat menjadi dasar strategi promosi dan pengelolaan inventaris?

#### **Insight:**
Tren jumlah pesanan selama periode 2016–2018 menunjukkan pertumbuhan yang konsisten dan berkelanjutan, dengan lonjakan signifikan mulai awal 2017 yang mengindikasikan ekspansi bisnis atau peningkatan adopsi platform e-commerce. Pola musiman yang paling mencolok terjadi pada November 2017 dengan puncak 7.284 pesanan—hampir 50% lebih tinggi dari bulan sebelumnya—yang kemungkinan besar dipicu oleh event Black Friday dan promosi akhir tahun. Setelah lonjakan November, volume pesanan tetap stabil tinggi di rentang 6.000-7.000 pesanan per bulan sepanjang 2018, menunjukkan bahwa pertumbuhan bukan hanya bersifat seasonal spike tetapi mencerminkan peningkatan organic demand yang sustainable. Tidak terlihat pola musiman kuat di bulan-bulan lain selain periode Oktober-November, mengindikasikan bahwa mayoritas transaksi didorong oleh kebutuhan konsumen sehari-hari daripada seasonal events, dengan data 2016 dan akhir 2018 yang tidak lengkap sehingga analisis tren lebih valid untuk periode 2017-2018.

#### **Rekomendasi Bisnis:**
Platform harus memaksimalkan momentum periode Oktober-November dengan merencanakan kampanye promosi agresif (flash sale, bundle deals, voucher eksklusif) minimal 2-3 minggu sebelum Black Friday untuk membangun awareness dan anticipation pelanggan. Manajemen inventaris perlu diperkuat dengan forecasting yang lebih akurat untuk periode peak season—meningkatkan stok produk best-seller 30-40% lebih tinggi dari bulan biasa dan berkoordinasi erat dengan supplier untuk memastikan tidak terjadi stockout yang dapat mengecewakan pelanggan. Mengingat volume pesanan yang stabil tinggi sepanjang 2018, investasi dalam infrastruktur logistik dan warehouse capacity menjadi krusial untuk menghindari bottleneck operasional, termasuk penambahan tenaga kerja temporer selama peak season dan optimalisasi sistem order fulfillment. Selain itu, perusahaan dapat mengeksplorasi strategi untuk menciptakan "mini peak seasons" di bulan-bulan lain (seperti mid-year sale atau back-to-school campaign) guna mendistribusikan demand lebih merata sepanjang tahun dan mengurangi tekanan operasional yang terkonsentrasi di akhir tahun, sekaligus meningkatkan total annual revenue.

---

#### Pertanyaan 4: Kategori produk apa yang paling populer selama periode 2016–2018?

#### **Insight:**
Selama periode 2016–2018, kategori bed_bath_table mendominasi sebagai produk terpopuler dengan 11.847 unit terjual—mengungguli kategori kedua (health_beauty dengan 9.944 unit) sebesar 19%, mengonfirmasi bahwa produk rumah tangga dan dekorasi merupakan kebutuhan primer pelanggan e-commerce. Tiga kategori teratas (bed_bath_table, health_beauty, sports_leisure) secara kolektif mencerminkan tren konsumen modern yang fokus pada improvement kualitas hidup di rumah, perawatan diri, dan gaya hidup aktif. Dominasi kategori home & living (bed_bath_table, furniture_decor, housewares) yang menguasai 3 dari 10 posisi teratas dengan total lebih dari 27.000 unit menunjukkan bahwa platform ini telah berhasil memposisikan diri sebagai destination utama untuk kebutuhan rumah tangga. Kategori teknologi seperti computers_accessories (8.105 unit) dan telephony (4.692 unit) menunjukkan permintaan yang stabil namun tidak sebesar kategori home & lifestyle, mengindikasikan bahwa pelanggan cenderung membeli produk tech di channel lain atau memiliki frekuensi pembelian yang lebih rendah.

#### **Rekomendasi Bisnis:**
Platform harus memperkuat posisi dominan di kategori bed_bath_table dengan memperluas product assortment, menambah exclusive brands atau private label untuk meningkatkan margin, dan mengoptimalkan product discovery melalui personalized recommendation engine yang lebih canggih. Mengingat performa kuat kategori health_beauty dan sports_leisure, investasi dalam content marketing (tutorial makeup, workout guides, product reviews) dan influencer collaboration dapat meningkatkan engagement dan conversion rate di kedua kategori ini. Strategi cross-selling dan bundling antar kategori home & living (misalnya "complete your bedroom set" atau "bathroom essentials bundle") dapat meningkatkan average order value dan mendorong pelanggan untuk berbelanja multiple items sekaligus. Untuk kategori dengan performa lebih rendah seperti telephony dan auto, perlu dilakukan evaluasi apakah ini karena kurang kompetitif dalam pricing, limited selection, atau memang bukan core market—jika memang kurang profitable, resources bisa dialokasikan ke kategori dengan higher growth potential, atau sebaliknya melakukan strategic push dengan targeted promotion untuk meningkatkan market share di kategori tersebut.

---

#### Pertanyaan 5: Berapa rata-rata waktu pengiriman dari pembelian hingga diterima pelanggan selama periode 2016–2018, dan apakah terdapat perbedaan signifikan antar kota atau wilayah?

#### **Insight:**
Selama periode 2016–2018, rata-rata waktu pengiriman nasional adalah 12,0 hari dengan distribusi yang terkonsentrasi di rentang 10-15 hari untuk mayoritas pesanan, menunjukkan konsistensi operasional logistik yang cukup baik. Namun, terdapat disparitas geografis yang signifikan: São Paulo mencatat waktu pengiriman tercepat (8,3 hari)—hampir 45% lebih cepat dari rata-rata nasional—mengonfirmasi keunggulan infrastruktur logistik dan proximity ke distribution center di pusat ekonomi utama. Sebaliknya, negara bagian seperti Espírito Santo dan Mato Grosso do Sul mengalami waktu pengiriman terlama (15,1 hari), hampir dua kali lipat dari SP, yang kemungkinan disebabkan oleh jarak geografis yang jauh, keterbatasan infrastruktur transportasi, atau kurangnya fulfillment center di wilayah tersebut. Menariknya, beberapa kota kecil seperti Iomere, Contenda, dan Siriji mencatat waktu pengiriman sangat cepat (2-3 hari), kemungkinan karena proximity ke hub logistik tertentu atau volume pesanan yang rendah sehingga mendapat prioritas processing. Adanya outlier dengan waktu pengiriman ekstrem (>200 hari) mengindikasikan masalah operasional seperti lost packages, alamat tidak valid, atau kendala logistik yang perlu investigasi lebih lanjut.

#### **Rekomendasi Bisnis:**
Platform harus memprioritaskan pembangunan atau partnership dengan regional fulfillment center di negara bagian dengan waktu pengiriman lambat (ES, MS, GO, RJ) untuk mengurangi last-mile delivery time dan meningkatkan customer satisfaction, dengan target mendekatkan rata-rata waktu pengiriman ke level SP (8-9 hari). Implementasi dynamic shipping rate berdasarkan lokasi geografis dapat membantu manage customer expectation—pelanggan di wilayah remote harus diberikan informasi transparan tentang estimasi pengiriman yang realistis saat checkout untuk mengurangi disappointment dan negative reviews. Investasi dalam teknologi tracking real-time dan proactive communication (SMS/email notification untuk setiap milestone pengiriman) akan meningkatkan trust dan mengurangi customer anxiety, terutama untuk wilayah dengan waktu pengiriman lebih lama. Untuk menangani outlier dengan delay ekstrem, perlu dibuat SOP ketat untuk escalation process—pesanan yang melewati threshold tertentu (misalnya 30 hari) harus otomatis di-flag untuk investigasi dan customer compensation (refund/voucher). Kerjasama strategis dengan multiple logistics provider (diversifikasi dari single courier) dapat memberikan fleksibilitas untuk memilih partner terbaik berdasarkan destination zone, meningkatkan reliability dan mengurangi dependency risk, sekaligus memberikan competitive advantage dalam delivery speed yang merupakan salah satu faktor krusial dalam e-commerce customer retention.

---

#### Pertanyaan 6: Bagaimana distribusi skor ulasan pelanggan, dan apakah terdapat hubungan antara review_score dengan waktu pengiriman atau nilai transaksi?

#### **Insight:**
Distribusi skor ulasan pelanggan menunjukkan sentiment yang sangat positif dengan dominasi rating tinggi: 75% ulasan berada di skor 4-5 bintang (87.324 dari 115.608 ulasan), dengan skor 5 bintang sendiri mencakup 56,5% dari total ulasan, mengindikasikan tingkat kepuasan pelanggan yang tinggi secara keseluruhan. Ulasan negatif (skor 1-2) hanya mencakup 16% dari total, menunjukkan bahwa mayoritas transaksi berjalan dengan baik. Analisis korelasi mengungkapkan hubungan negatif yang moderat antara waktu pengiriman dan review score (r = -0.30), mengonfirmasi bahwa delivery speed memiliki dampak signifikan terhadap kepuasan pelanggan—setiap penundaan pengiriman berpotensi menurunkan rating yang diberikan. Boxplot menunjukkan bahwa meskipun median delivery time relatif konsisten di semua kategori skor (10-15 hari), ulasan dengan skor 1-2 memiliki jauh lebih banyak outlier dengan waktu pengiriman ekstrem (>30 hari), menunjukkan bahwa keterlambatan pengiriman yang parah menjadi trigger utama untuk negative reviews. Tidak terlihat korelasi kuat antara nilai transaksi dan review score, mengindikasikan bahwa kepuasan pelanggan lebih didorong oleh service quality (delivery speed, product quality, customer service) daripada seberapa besar nilai pembelian mereka.

#### **Rekomendasi Bisnis:**
Platform harus menjadikan delivery speed optimization sebagai top priority untuk mempertahankan dan meningkatkan customer satisfaction score, dengan fokus khusus pada eliminasi extreme delays (>30 hari) yang menjadi penyebab utama 1-2 star reviews—implementasi alert system otomatis untuk pesanan yang berisiko terlambat dan proactive customer communication dapat mengurangi frustration dan mencegah negative reviews. Mengingat 75% pelanggan sudah satisfied (skor 4-5), strategi untuk move them dari "satisfied" ke "delighted" dapat dilakukan melalui surprise & delight tactics seperti faster-than-promised delivery, personalized thank you notes, atau small freebies untuk repeat customers—ini dapat meningkatkan word-of-mouth marketing dan brand loyalty. Untuk segmen dengan ulasan negatif (16%), implementasi systematic recovery process sangat penting: segera identify root cause (delay, wrong item, damaged goods), offer immediate resolution (refund, replacement, compensation voucher), dan follow-up untuk ensure satisfaction—converting detractors menjadi promoters melalui exceptional service recovery dapat mengubah negative experience menjadi positive brand story. Platform juga harus leverage high rating (56,5% five-star reviews) dalam marketing materials dan product pages untuk social proof, sambil secara aktif encourage satisfied customers untuk leave reviews melalui post-purchase email campaign dengan incentive (discount voucher untuk next purchase), karena positive reviews terbukti meningkatkan conversion rate hingga 270% menurut research e-commerce industry, yang pada akhirnya akan meningkatkan trust dan sales velocity.

---

#### Pertanyaan 7: Siapa penjual dengan total penjualan tertinggi selama periode 2016–2018, dan bagaimana rata-rata waktu pengiriman mereka dibandingkan penjual lainnya?

#### **Insight:**
Selama periode 2016–2018, penjual dengan Seller ID 7c67e1448b00f6e969d365cea6b010ab adalah penjual terbesar dengan total penjualan R$509.474—jauh lebih tinggi 64% dibanding penjual kedua (R$310.579). Namun ada masalah besar: penjual ini memiliki waktu pengiriman paling lambat (22 hari), hampir 2 kali lebih lama dari rata-rata platform (12 hari). Di sisi lain, beberapa penjual lain yang lebih cepat mengirim barang (10-11 hari) justru penjualannya lebih rendah. Ini menunjukkan bahwa penjualan tinggi tidak selalu berarti pelayanan bagus, dan kecepatan pengiriman belum tentu membuat penjualan meningkat—mungkin ada faktor lain seperti harga murah atau produk unik yang lebih berpengaruh.

#### **Rekomendasi Bisnis:**
Platform harus segera berbicara dengan penjual terbesar ini untuk memperbaiki masalah pengiriman yang lambat. Caranya bisa dengan membantu mereka mendapat akses ke jasa pengiriman yang lebih baik, atau bahkan membantu biaya untuk menyewa gudang yang lebih dekat dengan pelanggan. Ini penting karena jika pelanggan terus complain tentang pengiriman lambat, penjual ini bisa kehilangan reputasi dan akhirnya pindah ke platform lain—yang berarti platform kehilangan sumber pendapatan terbesar.

Platform juga perlu membuat sistem penilaian penjual yang tidak hanya melihat berapa banyak mereka jual, tapi juga seberapa cepat pengiriman dan seberapa puas pelanggan. Penjual yang bagus di semua aspek bisa diberi hadiah seperti ditampilkan di halaman utama atau dapat potongan biaya admin.

Selain itu, platform harus membantu penjual-penjual menengah yang sudah cepat dalam pengiriman tapi penjualannya belum maksimal. Berikan mereka bantuan seperti promosi gratis, tools untuk analisa data penjualan, atau pelatihan marketing. Dengan begitu, platform tidak terlalu bergantung pada satu penjual besar saja—lebih aman kalau ada banyak penjual yang sama-sama sukses.

Terakhir, cari tahu kenapa penjual yang cepat kirim barang belum laku banyak: apakah produknya kurang lengkap? Foto produk kurang menarik? Atau mungkin tidak muncul di hasil pencarian? Setelah tahu masalahnya, bantu mereka perbaiki supaya bisa tumbuh lebih besar.

---

#### Pertanyaan 8: Berapa proporsi pelanggan baru dibanding pelanggan yang melakukan pembelian ulang selama periode 2016–2018?

#### **Insight:**

Selama periode 2016–2018, sekitar **97% transaksi berasal dari pelanggan baru**, sementara **hanya 3% berasal dari pelanggan repeat**. Ini berarti sebagian besar pelanggan hanya melakukan pembelian satu kali dan tidak kembali berbelanja. Dari total 93.395 pelanggan, sebanyak 90.588 hanya melakukan satu transaksi, sementara hanya 2.807 pelanggan melakukan pembelian lebih dari sekali. Angka ini menunjukkan bahwa **tingkat retensi pelanggan masih sangat rendah**, meskipun strategi akuisisi pelanggan baru berjalan baik.

#### **Rekomendasi Bisnis:**

Fokus bisnis perlu bergeser dari sekadar akuisisi ke **strategi retensi pelanggan**. Platform dapat:

* Membangun **program loyalitas** atau **reward system** bagi pelanggan yang melakukan pembelian berulang.
* Mengirimkan **penawaran personal** atau **diskon pembelian berikutnya** untuk mendorong repeat order.
* Melakukan evaluasi terhadap **pengalaman pelanggan** (kecepatan pengiriman, kualitas produk, layanan purna jual) agar pelanggan lebih puas dan mau kembali.
* Menganalisis **alasan churn** pelanggan, misalnya melalui survei atau review, guna menemukan akar masalah dan memperbaikinya.

Dengan meningkatkan repeat purchase rate bahkan hanya 2–3%, bisnis dapat memperbesar **Customer Lifetime Value (CLV)** dan mencapai pertumbuhan yang lebih berkelanjutan tanpa bergantung sepenuhnya pada pelanggan baru.

---

#### Pertanyaan 9: Bagaimana performa penjualan dan rata-rata nilai transaksi per negara bagian (state), dan wilayah mana yang berkontribusi paling besar terhadap total pendapatan?

#### **Insight:**

Selama periode 2016–2018, **São Paulo (SP)** menjadi kontributor utama pendapatan dengan total penjualan mencapai **R$ 7,5 juta**, jauh melampaui **Rio de Janeiro (RJ)** sebesar **R$ 2,7 juta** dan **Minas Gerais (MG)** sebesar **R$ 2,3 juta**. Ketiga negara bagian ini menyumbang lebih dari **75% total pendapatan**, menegaskan dominasi wilayah **Tenggara Brasil** sebagai pusat aktivitas e-commerce.
Negara bagian di wilayah **Selatan** seperti **Rio Grande do Sul (RS)** dan **Paraná (PR)** juga berkontribusi cukup besar (di atas R$ 1 juta), sementara wilayah **Utara dan Timur Laut** seperti **Roraima (RR)**, **Amapá (AP)**, dan **Acre (AC)** memiliki kontribusi yang sangat kecil (< R$ 30 ribu).
Distribusi ini menunjukkan adanya **kesenjangan geografis** dalam performa penjualan, yang kemungkinan disebabkan oleh perbedaan infrastruktur logistik, tingkat urbanisasi, dan daya beli masyarakat.

#### **Rekomendasi Bisnis:**

* **Fokuskan strategi pemasaran dan promosi** di wilayah berkontribusi tinggi (SP, RJ, MG) untuk memaksimalkan pendapatan jangka pendek dan mempertahankan dominasi pasar.
* **Perluas penetrasi ke wilayah dengan kontribusi rendah** namun berpotensi tumbuh, seperti wilayah Utara dan Timur Laut, melalui strategi ekspansi bertahap (diskon pengiriman, kerja sama logistik lokal, atau kampanye digital lokal).
* **Analisis rata-rata nilai transaksi per wilayah** untuk memahami perilaku belanja dan potensi upselling di tiap state.
* **Tingkatkan efisiensi rantai pasok** di wilayah dengan logistik sulit agar biaya pengiriman lebih kompetitif dan dapat menarik lebih banyak pelanggan baru.

Dengan strategi ganda—**optimasi di wilayah utama dan ekspansi di pasar potensial**—platform dapat memperluas pangsa pasar sekaligus meningkatkan profitabilitas nasional secara berkelanjutan.

---

### **Segmentasi Pelanggan (RFM)**

#### **Insight:**
Hasil analisis RFM selama periode 2016–2018 menunjukkan bahwa pelanggan terbagi menjadi tiga kelompok utama: **Medium Value (48,8%)**, **Low Value (42,6%)**, dan **High Value (8,6%)**. Mayoritas pelanggan (lebih dari 91%) masih berada di kategori Medium dan Low Value, artinya mereka jarang belanja atau nilai belanjaannya masih kecil. Hanya sekitar 8,6% pelanggan yang termasuk High Value—mereka yang sering belanja dan menghabiskan uang banyak—tapi kelompok kecil ini memberikan kontribusi pendapatan yang sangat besar karena nilai transaksi mereka bisa mencapai puluhan ribu Real. 

Dari scatter plot terlihat bahwa pelanggan High Value memang berbeda: mereka belanja lebih sering (frequency tinggi) dan total pembeliannnya jauh lebih besar dibanding kelompok lain. Sementara pelanggan Low Value biasanya hanya belanja 1-2 kali dengan nilai kecil, lalu tidak kembali lagi. Heatmap RFM menunjukkan bahwa pelanggan dengan skor Recency dan Frequency tinggi (baru saja belanja dan sering belanja) adalah kelompok paling potensial karena mereka masih aktif dan loyal.

#### **Rekomendasi Bisnis:**
**Untuk pelanggan High Value (8,6%):** Ini adalah pelanggan paling penting yang harus dijaga dengan sangat baik. Berikan mereka perlakuan istimewa seperti program VIP dengan benefit eksklusif (gratis ongkir selamanya, akses early sale, customer service prioritas), diskon khusus di hari ulang tahun, atau hadiah surprise untuk berterima kasih atas loyalitas mereka. Jangan sampai kehilangan mereka karena mereka adalah sumber pendapatan terbesar.

**Untuk pelanggan Medium Value (48,8%):** Ini adalah kelompok terbesar yang punya potensi besar untuk naik level menjadi High Value. Dorong mereka untuk belanja lebih sering dengan program seperti: beli 3 kali dapat voucher gratis, cashback untuk pembelian rutin, atau rekomendasi produk personal berdasarkan belanjaan mereka sebelumnya. Kirim email atau notifikasi yang relevan dengan kebutuhan mereka supaya mereka ingat untuk belanja lagi.

**Untuk pelanggan Low Value (42,6%):** Kelompok ini perlu "dibangunkan" kembali karena mereka sudah hampir tidak aktif. Strategi yang bisa dipakai: kirim diskon besar-besaran (misalnya 30-50% off), promo flash sale eksklusif, atau voucher yang harus dipakai dalam waktu terbatas untuk create urgency. Coba juga kirim email yang mengingatkan produk yang pernah mereka lihat tapi belum dibeli, atau tawarkan produk baru yang sesuai dengan minat mereka.

**Strategi prioritas:** Fokuskan resource terbesar untuk menjaga High Value customers (karena kehilangan satu pelanggan ini sama dengan kehilangan ratusan pelanggan Low Value), alokasikan budget sedang untuk upgrade Medium Value customers (karena mereka jumlahnya banyak dan mudah di-convert), dan gunakan strategi low-cost untuk reaktivasi Low Value customers (seperti automated email marketing). Dengan cara ini, platform bisa maksimalkan return dari setiap rupiah yang dikeluarkan untuk program loyalitas.

---

## 8️⃣ Dashboard / Visualization

### Tampilan Dashboard

![images\dashboard-viz.png](images\dashboard-viz.png)

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

