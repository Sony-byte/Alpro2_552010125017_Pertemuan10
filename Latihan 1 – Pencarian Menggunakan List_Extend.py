# Sony Iman Kurnia
# 552010125017
# 30 - Mei - 2026

import os

# Membersihkan terminal 
os.system('cls' if os.name == 'nt' else 'clear')

data = ["A001", "A002", "A003", "A004"]

ulang = "y"

while ulang.lower() == "y":
    target = input("Masukkan NIM yang dicari: ")

    count = 0
    found = False

    for item in data:
        count += 1
        if item == target:
            found = True
            break

    print("Ditemukan:", found)
    print("Jumlah langkah:", count)

    ulang = input("\nCari data lagi? (y/t): ")

print("Program selesai.")