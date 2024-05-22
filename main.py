import barang

def main():
    while True:
        print("\nSelamat datang di program Manajemen Stok Barang!")
        print("Pilihan:")
        print("1. Tambah Data Barang")
        print("2. Edit Data Barang")
        print("3. Hapus Data Barang")
        print("4. Cari Data Barang")
        print("5. Tampilkan Data Barang")
        print("6. Tampilkan Jumlah Data Barang")
        print("7. Keluar")

        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            barang.tambah_barang()
        elif pilihan == '2':
            index = int(input("Hapus data indeks ke : ")) - 1
            nama = input("Masukkan Nama : ")
            jumlah = int(input("Masukkan stok : "))
            barang.edit_data(index, nama, jumlah)
        elif pilihan == '3':
            barang.hapus_barang()
        elif pilihan == '4':
            nama = input("Masukkan Nama Barang yang ingin dicari: ")
            barang.cari_barang(nama)
        elif pilihan == '5':
            barang.tampilkan_data()
        elif pilihan == '6':
            barang.tampilkan_jumlah_data()
        elif pilihan == '7':
            print("Terima kasih telah menggunakan program Manajemen Stok Barang!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

if __name__ == "__main__":
    main()
