import numpy as np


def calculate_document_weights(query, documents):
    """
    Menghitung bobot vektor dokumen dan query berdasarkan frekuensi kata dalam kamus (vocabulary).

    Parameter:
    - query: Kalimat atau kata kunci pencarian yang digunakan oleh pengguna.
    - documents: Daftar dokumen dalam bentuk string yang akan diproses.

    Mengembalikan:
    - document_vectors: Vektor representasi dari setiap dokumen.
    - query_vector: Vektor representasi dari query.
    - vocabulary: Daftar semua kata yang ada dalam dokumen dan query (kamus).
    """
    # Membuat set vocabulary yang berisi kata-kata unik dari query
    vocabulary = set(query.split())
    
    # Menambahkan kata-kata dari setiap dokumen ke dalam vocabulary
    for doc in documents:
        vocabulary.update(doc.split())

    document_vectors = []
    # Membuat vektor untuk setiap dokumen berdasarkan frekuensi kata dalam vocabulary
    for doc in documents:
        vector = [doc.count(term) for term in vocabulary]
        document_vectors.append(vector)

    # Membuat vektor untuk query berdasarkan frekuensi kata dalam vocabulary
    query_vector = [query.count(term) for term in vocabulary]

    return np.array(document_vectors), np.array(query_vector), list(vocabulary)
