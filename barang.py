barang = []

def tambah_barang():
    nama_barang = str(input("Masukkan nama barang: "))
    jumlah = int(input("Masukkan jumlah stok barang: "))

    stok_baru = {"nama": nama_barang, "stok": jumlah}
    barang.append(stok_baru)
    print("Data barang telah ditambahkan.")

def edit_data(indeks, nama=None, jumlah=None):
    if 0 <= indeks < len(barang):
        if nama is not None:
            barang[indeks]['nama'] = nama
        if jumlah is not None:
            barang[indeks]['stok'] = jumlah
        print(f"Data pada indeks {indeks} telah diperbarui.")
    else:
        print(f"Indeks {indeks} tidak valid.")

def hapus_barang():
    tampilkan_data()
    index = int(input("Masukkan nomor barang yang ingin dihapus: ")) - 1
    if 0 <= index < len(barang):
        barang_terhapus = barang.pop(index)
        print(f"Barang '{barang_terhapus['nama']}' telah dihapus.")
    else:
        print("Nomor barang tidak valid.")

def cari_barang(nama):
    hasil_pencarian = [brg for brg in barang if brg['nama'].lower() == nama.lower()]
    if hasil_pencarian:
        for brg in hasil_pencarian:
            print(f"{brg['nama']}, Stok: {brg['stok']}")
    else:
        print(f"Barang dengan nama '{nama}' tidak ditemukan.")

def tampilkan_data():
    if not barang:
        print("==== TOKO ELEKTRONIK ====")
        print("----Data Barang Kosong----")
    else:
        for i, brg in enumerate(barang, 1):
            print(f"{i}. {brg['nama']} : {brg['stok']}")

def tampilkan_jumlah_data():
    print(f"Jumlah Data Tersimpan: {len(barang)} Barang")
