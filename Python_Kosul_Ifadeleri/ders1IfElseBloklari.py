if 3>2:
    print("dongu basladi") #if önündeki ifade true ise donguye alir

if 3<2:
    print("hos geldiniz")

if True:
    print("aa bb cc")

kullaniciAdi='ahmet'
sifre='1234'

#kullanici adi ve sifre bilgileri alinarak giris yapilir.

kulllaniciAdiGiris=input("kullanici adi giriniz: ")
sifreGirisi=input("sifreyi giriniz")

kullaniciGirisi=(kulllaniciAdiGiris==kullaniciAdi) and (sifreGirisi==sifre)

if (kullaniciGirisi==True):
    print("giris basarili")
else:
    print("giris basarisiz")
