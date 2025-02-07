from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore
from sklearn.metrics.pairwise import cosine_similarity # type: ignore
from nltk.tokenize import word_tokenize

# Fungsi untuk tokenisasi dan pembuatan vocabulary
def tokenize_and_create_vocabulary(documents):
    """
    Fungsi ini melakukan tokenisasi pada setiap dokumen dan membuat vocabulary yang berisi semua kata yang muncul
    dalam corpus.

    Parameter:
    - documents: Daftar dokumen dalam bentuk tuple (index, sura, aya, review).

    Mengembalikan:
    - tokenized_documents: Daftar dokumen yang sudah melalui tokenisasi dan hanya berisi kata-kata yang terdiri
      dari karakter huruf.
    - vocabulary: Daftar unik kata-kata yang ada di semua dokumen.
    """
    vocabulary = set()  # Menyimpan kata-kata unik
    tokenized_documents = []  # Menyimpan dokumen yang telah ditokenisasi

    # Tokenisasi setiap dokumen dan memperbarui vocabulary
    for (index, sura, aya, review) in documents:
        tokens = word_tokenize(review)  # Tokenisasi dokumen
        tokens = [word.lower() for word in tokens if word.isalpha()]  # Menghilangkan token non-huruf
        tokenized_documents.append(" ".join(tokens))  # Menambahkan dokumen yang sudah ditokenisasi
        vocabulary.update(tokens)  # Menambahkan kata ke vocabulary

    return tokenized_documents, list(vocabulary)  # Mengembalikan tokenized documents dan vocabulary

def calculate_vsm(query, corpus):
    """
    Fungsi ini menghitung vector space model (VSM) untuk query dan corpus menggunakan TF-IDF dan cosine similarity.

    Parameter:
    - query: Query yang ingin dicari kesamaan dengan dokumen dalam corpus.
    - corpus: Daftar dokumen dalam bentuk tuple (index, sura, aya, review).

    Mengembalikan:
    - top_documents: Daftar 7 dokumen teratas yang memiliki nilai cosine similarity tertinggi dengan query.
    """
    # Memanggil fungsi untuk tokenisasi dan pembuatan vocabulary
    tokenized_docs, vocabulary = tokenize_and_create_vocabulary(corpus)

    # Pembobotan term menggunakan Term Frequency - Inverse Document Frequency (TF-IDF)
    vectorizer = TfidfVectorizer(vocabulary=vocabulary)  # Membuat objek TfidfVectorizer dengan vocabulary yang telah dibuat
    tfidf_matrix = vectorizer.fit_transform(tokenized_docs)  # Membuat matriks TF-IDF untuk dokumen-dokumen

    # Tokenisasi dan pembobotan term untuk query
    query_tokens = word_tokenize(query)  # Tokenisasi query
    query_tokens = [word.lower() for word in query_tokens if word.isalpha()]  # Menghilangkan token non-huruf
    query_vector = vectorizer.transform([" ".join(query_tokens)])  # Membuat vektor TF-IDF untuk query

    # Menghitung kemiripan cosine antara query dan dokumen
    cosine_similarities = cosine_similarity(tfidf_matrix, query_vector)  # Menghitung cosine similarity

    # Menyusun dokumen berdasarkan skor kemiripan cosine
    ranked_documents = sorted(enumerate(cosine_similarities), key=lambda x: x[1], reverse=True)

    # Mengambil 7 dokumen teratas dengan kemiripan tertinggi
    top_documents = ranked_documents[:7]
    return top_documents  # Mengembalikan 7 dokumen teratas yang relevan dengan query
