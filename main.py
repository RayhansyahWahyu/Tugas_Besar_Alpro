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

# Struktur Data Di copy Dari Template
    database = TEMPLATE.copy()
    database["nama_obat"] = nama_obat + TEMPLATE["nama_obat"][len(nama_obat):]
    database["jumlah_stok"] = jumlah_stok + TEMPLATE["jumlah_stok"][len(jumlah_stok):]

    data = f"{database['nama_obat']},{database['jumlah_stok']}\n"

    with open("gudang.txt", "a",encoding="utf-8") as file:
        file.write(data)

def cek_stok_obat_tersedia():
    os.system("clear")

    # Bagian Atas Tabel
    nama_obat = input("Masukkan Nama Obat\t: ")

    print("========================================")
    with open("gudang.txt","r") as file:
        data = file.readlines()
        for content in data:
            content = content.split(",")
            jml_stok = content[1].replace('\n', '')
            if content[0].replace(" ", "") == nama_obat:
                print(f"Nama Obat   : {content[0]}")
                print(f"Jumlah Stok : {jml_stok}")
                break
    print("========================================")
    x = input()

# Fungsi Untuk Edit Nama Atau Stok Obat
def edit_obat():
    cek_stok()
    index = int(input("Masukkan Nomor Obat\t: ")) - 1

    os.system("clear")
    with open("gudang.txt","r+") as file:
        data = file.readlines()
        for no,content in enumerate(data):
            content = content.split(",")
            if no == index:
                break

    nama_obat = content[0]
    jumlah_stok = content[1].replace("\n", "")
    print("===========================")
    print(f"Nama Obat   : {nama_obat}")
    print(f"Jumlah Stok : {jumlah_stok}")
    print("===========================\n")
    x = input()

    os.system("clear")
    print("1. Edit Nama Obat\n2. Edit Jumlah Stok\n")
    opsi = input("Masukkan Opsi Yang Ingin Di Edit [1,2]\t: ")
    match opsi:
        case "1": nama_obat = input("Masukkan Nama Baru\t: ")
        case "2": jumlah_stok = input("Masukkan Jumlah Stok Baru\t: ")

    # Struktur Data Di copy Dari Template
    database = TEMPLATE.copy()
    database["nama_obat"] = nama_obat + TEMPLATE["nama_obat"][len(nama_obat):]
    database["jumlah_stok"] = jumlah_stok + TEMPLATE["jumlah_stok"][len(jumlah_stok):]

    data = f"{database['nama_obat']},{database['jumlah_stok']}\n"

    with open("gudang.txt","r+") as file:
        file.seek(index * len(data))
        file.write(data)

    print("=========Data Baru===========")
    print(f"Nama Obat   : {nama_obat}")
    print(f"Jumlah Stok : {jumlah_stok}")
    print("===========================\n")
    x = input()

# Hapus Stok Obat
def hapus_obat():
    cek_stok()
    index = int(input("Masukkan Nomor Obat\t: ")) - 1

    os.system("clear")
    with open("gudang.txt","r+") as file:
        data = file.readlines()
        for no,content in enumerate(data):
            content = content.split(",")
            if no == index:
                break

    nama_obat = content[0]
    jumlah_stok = content[1].replace("\n", "")
    print("===========================")
    print(f"Nama Obat   : {nama_obat}")
    print(f"Jumlah Stok : {jumlah_stok}")
    print("===========================\n")
    yakin = input("Yakin Ingin Di Hapus (y/t)\t: ")
    
    if yakin == "y":
        with open("gudang.txt","r") as file:
            data = file.readlines()

            with open("gudang.txt","w") as file_baru:
                for no,content in enumerate(data):
                    if no != index:
                        file_baru.write(content)
                    
# Program Dimulai
while True:
    os.system("clear")
    menu()
    opsi = input("Masukkan Opsi\t: ")
    match opsi:
        case "1": cek_stok()
        case "2": tambah_stok()
        case "3": cek_stok_obat_tersedia()
        case "4": edit_obat()
        case "5": hapus_obat()
        case "6": break