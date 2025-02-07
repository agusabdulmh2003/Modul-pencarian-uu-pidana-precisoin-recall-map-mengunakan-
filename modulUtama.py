import database
import textPreProcessing
import rocchioVSM
import re
import nltk

# Ambil data dari tabel laws
# %% 
query = "SELECT * FROM laws"

# Mengambil data dari database menggunakan query
data = database.getData(query)

# Pra-pemrosesan teks
corpus = textPreProcessing.textprocessing(data)

# Ambil dokumen untuk pencarian
# Menyusun list dokumen berdasarkan hasil pra-pemrosesan
documents = [isi for (_, _, isi) in corpus]

if __name__ == "__main__":
    # Pengguna menginputkan query pencarian
    query_input = input("Masukkan query: ")

    # Menghitung representasi vektor dokumen dan query
    # Fungsi 'calculate_document_weights' menghitung bobot vektor dokumen dan query
    document_vectors, query_vector, vocabulary = rocchioVSM.calculate_document_weights(query_input, documents)

    # Menampilkan hasil pencarian awal (tanpa feedback)
    top_documents = rocchioVSM.retrieve_documents(query_vector, document_vectors,700)

    print("\n7 Peringkat Dokumen Teratas:")
    for doc_idx, score in top_documents:
        # Menampilkan 7 dokumen teratas berdasarkan skor relevansi
        print(f"No. index {doc_idx + 1}: Score {score:.2f}. {data[doc_idx]}")

    # Pengguna menginputkan dokumen yang relevan dan tidak relevan untuk feedback
    try:
        # Mengambil input dari pengguna berupa nomor indeks dokumen relevan dan tidak relevan
        relevant_indices = [int(idx) - 1 for idx in input("Masukkan nomor index dokumen relevan (pisahkan dengan spasi): ").split()]
        non_relevant_indices = [int(idx) - 1 for idx in input("Masukkan nomor index dokumen tidak relevan (pisahkan dengan spasi): ").split()]
    except ValueError:
        # Menangani kesalahan jika input bukan angka
        print("Input tidak valid. Masukkan nomor dokumen yang valid.")
        exit()

    # Feedback menggunakan Rocchio
    # Mengambil vektor dari dokumen relevan dan tidak relevan
    relevant_vectors = [document_vectors[idx] for idx in relevant_indices]
    non_relevant_vectors = [document_vectors[idx] for idx in non_relevant_indices]

    # Menyesuaikan vektor query menggunakan feedback Rocchio
    updated_query_vector = rocchioVSM.rocchio_feedback(query_vector, relevant_vectors, non_relevant_vectors)

    print("\nPencarian setelah feedback Rocchio:")
    # Melakukan pencarian kembali menggunakan query yang sudah diperbarui
    updated_top_documents = rocchioVSM.retrieve_documents(updated_query_vector, document_vectors, 7)

    for doc_idx, score in updated_top_documents:
        # Menampilkan 7 dokumen teratas setelah feedback
        print(f"No. index {doc_idx + 1}: Score {score:.2f}. {data[doc_idx]}")
