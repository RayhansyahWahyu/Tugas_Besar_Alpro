import os

# Struktur Dari Database
TEMPLATE = {
    "nama_obat": " "*50,
    "jumlah_stok": " "*50
}

# Tampilan Menu Awal
def  menu():
    print("Selamat Datang Di Program".center(60))
    print("       Stok Obat         ".center(60))
    print("1. Cek Stok Obat")
    print("2. Tambah Stok Obat")
    print("3. Cek Nama Obat")
    print("4. Edit Nama/Stok Obat")
    print("5. Hapus Stok Obat")
    print("6. Keluar\n")

# Cek Stok Obat
def cek_stok():
    os.system("clear")
    with open("gudang.txt","r") as file:
        data = file.readlines()
    
    # Bagian Atas Tabel
    print("========================================")
    print("No | Nama Obat       | Jumlah Stok     |")
    print("========================================")
    # Bagian Tengah Tabel 
    for index,content in enumerate(data): 
        content = content.split(",")
        nama_obat = content[0]
        jumlah_stok = content[1]
        print(f"{index+1:2} | {nama_obat:.15} | {jumlah_stok:.15} |")
    # Bagian Bawah Tabel 
    print("========================================")
    
    x = input()

# Fungsi Untuk Menambah Stok Obat
def tambah_stok():
    os.system("clear")
    print("Masukkan Nama Obat".center(60))
    nama_obat = input()
    print("Masukkan Jumlah Stok".center(60))
    jumlah_stok = input()

# Program Dimulai
while True:
    os.system("clear")
    menu()
    opsi = input("Masukkan Opsi\t: ")
    match opsi:
        case "1": cek_stok()
        case "2": tambah_stok() 
        case "6": break