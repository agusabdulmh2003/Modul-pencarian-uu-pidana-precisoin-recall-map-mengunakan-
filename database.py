import mysql.connector
from mysql.connector import errorcode

# Konfigurasi untuk koneksi ke database MySQL
config = {
    'user': 'root',
    'database': 'uupidana'  # Pastikan nama database benar
}

class DatabaseConnection:
    def __init__(self):
        """
        Inisialisasi kelas untuk koneksi ke database MySQL.
        Coba melakukan koneksi ke database dengan parameter yang ada dalam 'config'.
        Jika terjadi kesalahan, error akan ditangani sesuai dengan tipe kesalahan yang muncul.
        """
        try:
            # Membuat koneksi ke database menggunakan konfigurasi
            self.db_connect = mysql.connector.connect(**config)
            self.cursor = self.db_connect.cursor()  # Membuat objek cursor untuk mengeksekusi query
        except mysql.connector.Error as err:
            # Menangani kesalahan koneksi dan memberikan pesan error sesuai jenis kesalahannya
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(f"Error: {err}")

    def Select(self, query):
        """
        Menjalankan query SELECT pada database dan mengembalikan hasilnya.
        
        Parameter:
        - query: string, query SQL yang akan dijalankan
        
        Return:
        - Hasil dari query dalam bentuk list
        """
        self.cursor.execute(query)  # Menjalankan query
        return self.cursor.fetchall()  # Mengembalikan semua hasil query dalam bentuk list

    def __del__(self):
        """
        Destructor untuk kelas DatabaseConnection.
        Menutup objek cursor dan koneksi ke database saat objek ini dihapus.
        """
        self.cursor.close()  # Menutup objek cursor setelah selesai digunakan
        self.db_connect.close()  # Menutup koneksi ke database

def getData(sql_query):
    """
    Fungsi untuk mengambil data dari database berdasarkan query yang diberikan.
    
    Parameter:
    - sql_query: string, query SQL untuk mengeksekusi pencarian data
    
    Return:
    - Mengembalikan hasil query dalam bentuk list
    """
    db = DatabaseConnection()  # Membuat objek koneksi database
    return db.Select(sql_query)  # Menjalankan fungsi Select dan mengembalikan hasilnya
