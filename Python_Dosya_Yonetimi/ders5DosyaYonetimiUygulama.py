def notlariOku():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        for satir in file:
         print(satir)

def notGir():
    isim=input('ogrenci adi: ')
    soyisim=input('ogrenci soyadi: ')
    not1=input('1.notu giriniz: ')
    not2=input('1.notu giriniz: ')
    with open("sinav_notlari.txt","a",encoding="utf-8") as file:
     file.write(isim+' '+soyisim+':'+not1+','+not2+'\n')


def notlariKayitEt():
    with open("sinav_notlari.txt","r",encoding="utf-8") as file:
        liste=[]
        for i in liste:
            liste.append(file.readlines())
            with open("sonuclar.txt","a",encoding="utf-8"):
                file.writelines(liste[i])



while True:
    kullaniciGirisi=input('1-Notlari Oku\n2-Not Gir\n3-Notlari Kayit Et\n4-Cikis Yap\n')

    if (kullaniciGirisi=='1'):
        notlariOku()
    elif (kullaniciGirisi=='2'):
        notGir()
    elif (kullaniciGirisi=='3'):    
        notlariKayitEt()
    elif(kullaniciGirisi=='4'):
        break
    else:
        print('Hatali giris yaptiniz!')