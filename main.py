#====================================
# INI CUMA TEMPLATE, MUNGKIN NANTI ADA YANG DIGANTI
# DATA BERITA MINIMAL 50, MUNGKIN NANTI KITA TAMBAH KE 55 BERITA, JUDUL SAJA
# STRUKTUR PROGRAMNYA ADA DATA BERITA, CASE FOLDING, TOKENIZATION, STOPWORDS, MATCHING, SCORING
#====================================

# =====================================
# DATABASE BERITA
# =====================================

database_berita = [
    {"id": 1, "judul": "Perkembangan Teknologi Indonesia"},
    {"id": 2, "judul": "Dampak Perubahan Iklim"},
    {"id": 3, "judul": "Pendidikan dan Teknologi Modern"},
    {"id": 4, "judul": "Ekonomi Digital Indonesia"},
    {"id": 5, "judul": "Kesehatan Masyarakat di Era Digital"},
    {"id": 6, "judul": "Ekonomi Digital Indonesia Diproyeksikan Tembus Rp2,1 Kuadriliun pada 2026, E-Commerce Jadi Motor Utama"},
    {"id": 7, "judul": "AI Mulai Mengubah Wajah Ekonomi Digital Indonesia, UMKM Diminta Siap Beradaptasi"},
    {"id": 8, "judul": "E-Commerce Tetap Jadi Penopang Terbesar Ekonomi Digital RI, Nilai Transaksi Capai US$85 Miliar"},
    {"id": 9, "judul": "Indonesia Percepat Pembangunan Data Center untuk Dukung Ekonomi Berbasis AI"},
    {"id": 10, "judul": "Pemerintah Targetkan Kapasitas Data Center Indonesia Naik ke 11 GW pada 2030"},
    {"id": 11, "judul": "Teknologi dan Lingkungan Hidup"},
    {"id": 12, "judul": "Perkembangan Startup di Indonesia"},
    {"id": 13, "judul": "Kebijakan Pemerintah dalam Sektor Energi"},
    {"id": 14, "judul": "Infrastruktur dan Pembangunan Nasional"},
    {"id": 15, "judul": "Peran Teknologi dalam Kesehatan Mental"},
    {"id": 16, "judul": "Pendidikan Karakter di Sekolah"},
    {"id": 17, "judul": "Dampak Globalisasi terhadap Budaya Lokal"},
    {"id": 18, "judul": "Inovasi Teknologi untuk Transportasi Publik"},
    {"id": 19, "judul": "Perkembangan E-commerce di Indonesia"},
    {"id": 20, "judul": "Kebijakan Lingkungan dan Perubahan Iklim"},
]
#====================================

# =====================================
# CASE FOLDING
# =====================================

def case_folding(teks):
    huruf_besar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    huruf_kecil = "abcdefghijklmnopqrstuvwxyz"

    hasil = ""

    for karakter in teks:
        ditemukan = False

        for i in range(26):
            if karakter == huruf_besar[i]:
                hasil = hasil + huruf_kecil[i]
                ditemukan = True
                break

        if ditemukan == False:
            hasil = hasil + karakter

    return hasil

#Perulangan for di bawah, untuk testing saja, nanti dihapus kalau sudah fix
#for berita in database_berita:
    berita["judul_lower"] = case_folding(berita["judul"])
    print(f"Judul Berita: {berita['judul']} -> Case Folding: {berita['judul_lower']}")
#====================================


# =====================================
# TOKENIZATION
# =====================================

def tokenization(teks):
    hasil = []
    kata = ""

    for karakter in teks:
        if karakter != " ":
            kata = kata + karakter
        else:
            if kata != "":
                hasil = hasil + [kata]
                kata = ""

    if kata != "":
        hasil = hasil + [kata]

    return hasil

#Perulangan for di bawah, untuk testing saja, nanti dihapus kalau sudah fix
#for berita in database_berita:
    berita["judul_lower"] = case_folding(berita["judul"])
    berita["judul_tokens"] = tokenization(berita["judul_lower"])
    print(f"Judul Berita: {berita['judul']} -> Case Folding: {berita['judul_lower']} -> Tokens: {berita['judul_tokens']}")
#====================================


# =====================================
# STOPWORDS
# =====================================

#Variable stopwords, type list, berisikan kata-kata yang akan dihapus, karena tidak begitu penting, pada program ini.
#Kalo kurang, bisa kita tambah nanti.
stopwords = [
    "di", "ke", "dari", "dan", "yang",
    "untuk", "pada", "dengan", "dalam",
    "atau", "adalah", "itu", "ini", "sebagai",
    "oleh", "karena", "agar", "juga", "akan",
    "telah", "sudah", "belum", "tidak", "bukan",
    #Di bawah ada tanda baca, mungkin ga begitu penting?
    ",", ".", "!", "?", ":", ";", "-", "_", "(",
    ")", "[", "]", "{", "}", "'", '"', "/", "\\"
]


# =====================================
# STOPWORDS REMOVAL
# =====================================

#Nah, kalo ini fungsi yang nanti dipanggil untuk ngehapus kata-kata yang ada di variable stopwords tadi.
def stopwords_removal(daftar_token):
    hasil = []

    for kata in daftar_token:
        ditemukan = False

        for stopword in stopwords:
            if kata == stopword:
                ditemukan = True
                break

        if ditemukan == False:
            hasil = hasil + [kata]

    return hasil

#Perulangan for di bawah, untuk testing saja, nanti dihapus kalau sudah fix
#for berita in database_berita:
    berita["judul_lower"] = case_folding(berita["judul"])
    berita["judul_tokens"] = tokenization(berita["judul_lower"])
    berita["judul_tokens_no_stopwords"] = stopwords_removal(berita["judul_tokens"])
    print(f"Judul Berita: {berita['judul']}\n -> Case Folding: {berita['judul_lower']}\n -> Tokens: {berita['judul_tokens']}\n -> Tokens No Stopwords: {berita['judul_tokens_no_stopwords']}")
#====================================

#SEBELUM MEMASUKI MATCHING KITA SEDIAKAN DULU 50 JUDUL UNTUK DATABASE BERITA, KALAU SUDAH, BARU KITA LANJUTKAN KE MATCHING DAN SCORING

# =====================================
# MATCHING
# =====================================

#MENCOCOKKAN QUERY DENGAN DATABASE BERITA, KALO ADA YANG COCOK, MAKA BERITA TERSEBUT AKAN DIMASUKKAN KE DALAM LIST HASIL MATCHING
def matching(query_token, database):
    hasil_matching = []

    for berita in database:
        judul = berita["judul"]

        judul_lower = case_folding(judul)
        judul_token = tokenization(judul_lower)
        judul_bersih = stopwords_removal(judul_token)

        cocok = False

        for kata_query in query_token:
            for kata_judul in judul_bersih:
                if kata_query == kata_judul:
                    cocok = True
                    break

            if cocok:
                break

        if cocok:
            hasil_matching = hasil_matching + [berita]

    return hasil_matching

#Di bawah ini untuk testing, nanti dihapus aja kalo udah fix
query = "Teknologi di Indonesia" #Query

query_lower = case_folding(query) #Mengubah query menjadi huruf kecil
query_token = tokenization(query_lower) #Memecah query menjadi token-token
query_bersih = stopwords_removal(query_token) #Menghapus kata/tanda baca pada query, yang ada di dalam stopwords

hasil = matching(query_bersih, database_berita) #Variable yang memanggil fungsi matching, untuk mengeluarkan berita-berita yang cocok dengan query yang telah di proses. Lalu, hasilnya disimpan di variable hasil.

print("Hasil Pencarian:")

for berita in hasil: #mengecek setiap berita yang ada di dalam variable hasil, lalu menampilkan judul berita yang cocok dengan query.
    print(berita["judul"]) #mencetak judul berita yang cocok dengan query, dari hasil pengecekan dari perulangan for di atas.
#====================================


# =====================================
# SCORING
# =====================================
# UNTUK SCORING DI SINI, KITA PAKE 2 METODE, PERTAMA ADALAH COSINE SIMILARITY TF-IDF, KEDUA BM25, KITA PAKAI SEMUA DARI 2 METODE TERSEBUT. YANG DI MANA NANTI ADA 2 OUTPUT, SATU UNTUK COSINE SIMILARITY TF-IDF, DAN SATU LAGI UNTUK BM25.

#Cosine Similarity TF-IDF
# Pertama, menghitung TF-IDF:
# TFIDF(t,d) = TF(t,d) * IDF(t)
# dengan: IDF(t) = log(N +1 / DF(t) + 1) + 1
# Kedua, menghitung Cosine Similarity:
# CosineSim(Q,D) = Q.D / |Q| * |D|
# Keterangan: 
# N = jumlah judul berita, 
# DF(t) = jumlah judul berita yang mengandung token t, 
# TF(t,d) = frekuensi kata dalam judul berita, 
# Q = vektor query, 
# D = vektor judul berita.
def cosine_sim(query_token, database):
    pass