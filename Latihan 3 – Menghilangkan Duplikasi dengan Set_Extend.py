# Sony Iman Kurnia
# 552010125017
# 30 - Mei - 2026

import os

# Membersihkan terminal hanya saat program dijalankan
os.system('cls' if os.name == 'nt' else 'clear')

data = [10, 20, 20, 30, 40, 40, 50]

while True:
    print("\n=== PROGRAM SET PYTHON ===")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Tampilkan Data Unik")
    print("4. Hitung Jumlah Data Unik")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        print("Data awal :", data)

    elif pilihan == "2":
        try:
            nilai = int(input("Masukkan nilai baru: "))
            data.append(nilai)
            print("Data berhasil ditambahkan.")
        except ValueError:
            print("Input harus berupa angka!")

    elif pilihan == "3":
        unik = set(data)
        print("Data unik :", unik)

    elif pilihan == "4":
        unik = set(data)
        print("Jumlah data unik :", len(unik))

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")