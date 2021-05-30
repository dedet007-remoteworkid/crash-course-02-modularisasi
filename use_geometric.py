from geometric.segitiga import luas_segitiga, info as ins
from geometric.persegipanjang import luas_persegipanjang, info as inp
# import geometric.segitiga
# import geometric.segitiga as gs

alas = 20
tinggi = 6

print(ins())
print(f'luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas_segitiga(alas, tinggi)}')
#print(f'luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {geometric.segitiga.luas_segitiga(20,6)}')
#print(f'luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {gs.luas_segitiga(20,6)}')

panjang = 20
lebar = 10
print(inp())
print(f'luas persegi panjang dengan panjang {panjang} dan lebar {lebar} adalah {luas_persegipanjang(panjang, lebar)}')