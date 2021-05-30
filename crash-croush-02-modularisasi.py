"""
Script Menghitung Luas Segitiga
Luas = alas * tinggi * 0.5
"""

# menghitung segitiga 1
alas = 10
tinggi = 8
luas_segitiga = alas * tinggi / 2

print(f'Segitiga dengan alas = {alas} cm dan tinggi = {tinggi} cm, luasnya adalah {luas_segitiga} cm-persegi')

# copy paste
alas = 40
tinggi = 6
luas_segitiga = alas * tinggi / 2

print(f'Segitiga dengan alas = {alas} cm dan tinggi = {tinggi} cm, luasnya adalah {luas_segitiga} cm-persegi')

def luas_segitiga(alas,tinggi):
    luas = alas * tinggi / 2
    return luas

print(f'\nMenghitung luas segitiga dengan fungi, hasilnya: { luas_segitiga(10,8)}' )
print(f'\nMenghitung luas segitiga dengan fungi, hasilnya: { luas_segitiga(40,6)}' )