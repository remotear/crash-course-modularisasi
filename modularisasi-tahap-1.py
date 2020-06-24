"""
Program menghitung luas segitiga
Luas segitiga = alas * tinggi /2
"""
print(f'\nmenghitung luas segitiga')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas={alas} dan tinggi ={tinggi} memeiliki luas {luas_segitiga}')

alas = 20
tinggi = 2
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas={alas} dan tinggi ={tinggi} memeiliki luas {luas_segitiga}')

print('\nhitung_luas_segitiga')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print(f'menghitung luas segitiga dengan fungsi = {hitung_luas_segitiga(10, 6)}')
print(f'menghitung luas segitiga dengan fungsi = {hitung_luas_segitiga(20, 2)}')
print(f'menghitung luas segitiga dengan fungsi = {hitung_luas_segitiga(100, 2)}')

