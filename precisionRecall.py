def calculate_precision_recall(relevant_indices, non_relevant_indices, document_vectors):
    """
    Menghitung Precision dan Recall berdasarkan dokumen relevan dan tidak relevan.

    Parameter:
    - relevant_indices: Daftar indeks dokumen yang relevan.
    - non_relevant_indices: Daftar indeks dokumen yang tidak relevan.
    - document_vectors: Daftar vektor dokumen yang digunakan dalam pencarian.

    Mengembalikan:
    - precision: Nilai precision untuk pencarian.
    - recall: Nilai recall untuk pencarian.
    """
    
    # True Positives: jumlah dokumen relevan yang ditemukan dalam dokumen hasil pencarian
    true_positives = len(set(relevant_indices).intersection(set(document_vectors)))
    
    # False Positives: jumlah dokumen tidak relevan yang ditemukan dalam dokumen hasil pencarian
    false_positives = len(set(non_relevant_indices).intersection(set(document_vectors)))
    
    # False Negatives: jumlah dokumen relevan yang tidak ditemukan dalam dokumen hasil pencarian
    false_negatives = len(set(relevant_indices).difference(set(document_vectors)))

    # Precision: rasio dokumen relevan yang ditemukan terhadap semua dokumen yang ditemukan
    # Precision dihitung sebagai true positives dibagi dengan jumlah total dokumen yang dikembalikan (true positives + false positives)
    precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 0
    
    # Recall: rasio dokumen relevan yang ditemukan terhadap semua dokumen relevan yang ada
    # Recall dihitung sebagai true positives dibagi dengan jumlah total dokumen relevan yang ada (true positives + false negatives)
    recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 0

    # Mengembalikan nilai precision dan recall
    return precision, recall
