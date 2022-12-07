"""
FUNDAMENTAL PYTHON
"""

# Sekuensial adalah kode yang dikerjakan secara urutan

print("Budi membeli susu")
print("susunya gaada")
print("budi langsung balik")

# percabangan

jumlah_botol_susu = 173
jumlah_telur = 1200
print(f"Jumlah botol susu {jumlah_botol_susu} btl")
print(f"Jumlah telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 6 botol susu")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang kerumah")
print("Menyampaikan hasilnya kepada ibu")

# perulangan

## perulangan dengan for

jumlah_bukuu = 10
print("Ibu berkata, 'Baca semua bukumu' ")

jumlah_buku_yang_dibaca = 0

for jumlah_buku_yang_dibaca in range(1, jumlah_bukuu+1):
    print(f"Buku ke {jumlah_buku_yang_dibaca} sudah dibaca")

print(f"Jumlah buku yang sudah dibaca {jumlah_buku_yang_dibaca}")

### perulangan dengan while

jumlah_bukU_yang_dibaca_dan_dipahami = 10
print("Ibu berkata, 'Baca semua bukumu' ")

jumlah_buku_yang_dibacaa = 0
print(f"Jumlah buku yang sudah dibaca {jumlah_buku_yang_dibaca}")

while jumlah_buku_yang_dibacaa < jumlah_bukU_yang_dibaca_dan_dipahami:
    jumlah_buku_yang_dibacaa += 1
    print("Baca 1 buku yang belum dibaca")



