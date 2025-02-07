import numpy as np

def calculate_average_precision(relevant_indices, retrieved_indices):
    """
    Calculate the average precision for a single query.

    Parameters:
    - relevant_indices: List of indices of relevant documents.
    - retrieved_indices: List of indices of retrieved documents.

    Returns:
    - Average precision score.
    """
    # Jika tidak ada dokumen yang diambil, return 0 karena tidak ada hasil pencarian
    if not retrieved_indices:
        return 0.0

    # Jika tidak ada dokumen relevan, return 0 karena tidak ada dokumen relevan yang bisa dihitung
    if not relevant_indices:
        return 0.0

    retrieved_relevant_count = 0  # Menyimpan jumlah dokumen relevan yang berhasil diambil
    precision_sum = 0.0  # Menyimpan total nilai precision yang dihitung

    # Iterasi melalui dokumen yang diambil dan hitung precision
    for i, idx in enumerate(retrieved_indices):
        if idx in relevant_indices:  # Jika dokumen yang diambil relevan
            retrieved_relevant_count += 1  # Tambah jumlah dokumen relevan yang diambil
            precision_sum += retrieved_relevant_count / (i + 1)  # Tambah precision pada posisi i

    # Jika tidak ada dokumen relevan yang ditemukan, return 0
    if retrieved_relevant_count == 0:
        return 0.0

    # Hitung average precision dengan membagi total precision dengan jumlah dokumen relevan
    average_precision = precision_sum / len(relevant_indices)
    return average_precision

def calculate_average_precision_for_query(query, corpus):
    """
    Calculate Average Precision (AP) for a given query and corpus.

    Parameters:
    - query: The search query input by the user.
    - corpus: List of documents in the corpus.

    Returns:
    - Average Precision score.
    """
    # Simulasikan pengambilan dokumen relevan berdasarkan query (menggunakan pencocokan substring)
    relevant_indices = [i for i, doc in enumerate(corpus) if query.lower() in doc.lower()]

    # Simulasikan pengambilan dokumen berdasarkan algoritma ranking (di sini hanya mengambil 10 dokumen pertama)
    retrieved_indices = list(range(min(10, len(corpus))))  # Ambil 10 dokumen pertama

    # Hitung average precision untuk query saat ini
    average_precision = calculate_average_precision(relevant_indices, retrieved_indices)

    return average_precision
