# Sony Iman Kurnia
# 552010125017
# 30 - Mei - 2026

import os

# Membersihkan terminal 
os.system('cls' if os.name == 'nt' else 'clear')

data = {
    "A001": 80,
    "A002": 75,
    "A003": 90,
    "A004": 85
}

ulang = "y"

while ulang.lower() == "y":
    target = input("Masukkan NIM yang dicari: ")

    if target in data:
        print("Nilai:", data[target])
    else:
        print("Tidak ditemukan")

    ulang = input("\nCari data lagi? (y/t): ")

print("Program selesai.")