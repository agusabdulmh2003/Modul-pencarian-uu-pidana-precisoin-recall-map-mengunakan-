import re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def textprocessing(data):
    """
    Fungsi untuk memproses teks yang mencakup penghapusan stopword, stemming, 
    dan pembersihan teks dari karakter non-huruf.

    Parameter:
    - data: Daftar data yang berisi index, pasal, dan teks dokumen yang akan diproses.

    Mengembalikan:
    - corpus: Daftar tuple yang berisi index, pasal, dan teks yang telah diproses.
    """

    # Membuat objek stopword remover menggunakan Sastrawi
    factory = StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()

    # Membuat objek stemmer menggunakan Sastrawi
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    # List untuk menyimpan hasil teks yang telah diproses
    corpus = []

    # Memproses setiap dokumen dalam data
    for (index, pasal, text) in data:
        # Menghapus karakter selain huruf (mengganti dengan spasi)
        review = re.sub('[^a-zA-Z]', ' ', text)
        
        # Mengubah teks menjadi lowercase
        review = review.lower()

        # Menghapus stopwords dari teks
        review = stopword.remove(review)

        # Menghapus stopwords berulang kali hingga tidak ada perubahan
        while True:
            previous_length = len(review.split())  # Menghitung jumlah kata sebelum penghapusan stopwords
            review = stopword.remove(review)  # Menghapus stopwords
            current_length = len(review.split())  # Menghitung jumlah kata setelah penghapusan stopwords
            # Jika jumlah kata tidak berubah, berarti tidak ada stopword yang terhapus lagi
            if previous_length == current_length:
                break

        # Melakukan stemming untuk mengubah kata ke bentuk dasarnya
        review = stemmer.stem(review)

        # Menyimpan hasil ke dalam corpus
        corpus.append((index, pasal, review))

    # Mengembalikan corpus yang berisi dokumen yang telah diproses
    return corpus
