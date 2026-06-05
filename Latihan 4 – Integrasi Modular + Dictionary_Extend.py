# Sony Iman Kurnia
# 552010125017
# 30 - Mei - 2026

import os

# Membersihkan terminal
os.system('cls' if os.name == 'nt' else 'clear')


def tambah_data(data):
    nim = input("Masukkan NIM: ")

    try:
        nilai = float(input("Masukkan nilai: "))
        data[nim] = nilai
        print("Data berhasil ditambahkan.")
    except ValueError:
        print("Nilai harus berupa angka.")


def tampilkan_data(data):
    if data:
        print("\n=== DICTIONARY DATA MAHASISWA ===")
        for nim, nilai in data.items():
            print(f"NIM: {nim} | Nilai: {nilai}")
    else:
        print("Belum ada data.")


def cari_data(data):
    nim = input("Cari NIM: ")

    if nim in data:
        print("Nilai:", data[nim])
    else:
        print("Tidak ditemukan.")


def jumlah_unik(data):
    nilai_unik = set(data.values())
    print("Nilai unik:", nilai_unik)
    print("Jumlah nilai unik:", len(nilai_unik))


def info_dictionary(data):
    print("\n=== INFORMASI DICTIONARY ===")
    print("Jumlah data:", len(data))
    print("Key (NIM):", list(data.keys()))
    print("Value (Nilai):", list(data.values()))


def menu():
    data = {}

    while True:
        print("\n=== MENU ===")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Cari Data")
        print("4. Jumlah Nilai Unik (Set)")
        print("5. Informasi Dictionary")
        print("6. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tambah_data(data)

        elif pilih == "2":
            tampilkan_data(data)

        elif pilih == "3":
            cari_data(data)

        elif pilih == "4":
            jumlah_unik(data)

        elif pilih == "5":
            info_dictionary(data)

        elif pilih == "6":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


menu()