import numpy as np


# Membuat fungsi hard limit
def hard_limit(x):
    if x >= 0:
        return 1
    else:
        return -1


# Inisialisasikan bobot awal
bobot = np.zeros((3, 3), dtype=int)


# Set data training
data_training = [
    (np.array([[1, -1, 1], [-1, 1, -1], [1, -1, 1]]), 1, "X"),
    (np.array([[1, -1, -1], [1, -1, -1], [1, 1, 1]]), -1, "L"),
]


# Perhitungan nilai bobot baru
for x, t, c in data_training:
    bobot += x * t


# Memasukkan inputan baru
input_baru = np.zeros((3, 3), dtype=int)
for i in range(3):
    for j in range(3):
        input_baru[i][j] = int(input(f"Masukkan nilai baris {i + 1}, kolom {j + 1}: "))

print("Bobot : ")
print(bobot)

# Perhitungan aktivasi dan output
aktivasi = np.sum(input_baru * bobot)
output = hard_limit(aktivasi)

# Penentuan label
label = ""
if output >= 0:
    label = data_training[0][2]
else:
    label = data_training[1][2]


# Menampilkan output
print("\nInput baru :")
print(input_baru)
print(f"\nPerhitungan aktivasi = {aktivasi}")
print(f"y = {output}, dikenali sebagai {label}")
