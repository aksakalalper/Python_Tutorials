#1 kullanicidan isim, yas ve egitim durumu bilgilerini alip ehliyet alma durumunu kontrol ediniz. 
# 18 yasindan buyuk olmali ve lise yada universite mezunu olmali

'''
isim=input('isim giriniz: ')
yas=int(input('yas bilgisini giriiniz: '))
egitim=input('egitim bilgisini giriniz: ')

if ((yas>=18) and (egitim=="lise"or"universite")):
    print(f'{isim} kisisi ehliyet alabilr')
else:
    print(f'{isim} kisisi ehliyet alamaz')

#2 bir ogrencinin 2 yazili notunu alip hesaplayin. Ortalama karsiliklari:
#0-24->0
#25-44->1
#45-54->2
#55-69->3
#70-84->4
#85-100->5

yazili1=float(input('1.yaziliyi giriniz: '))
yazili2=float(input('2.yaziliyi girininz: '))
ortalama=(yazili1*0.5)+(yazili2*0.5)

if (0<=ortalama<=24):
    print('sonuc:0 ')
elif (25<=ortalama<=44):
    print('sonuc:1 ')
elif (45<=ortalama<=54):
    print('sonuc:2 ')
elif (55<=ortalama<=69):
    print('sonuc:0 ')
elif (70<=ortalama<=84):
    print('sonuc:0 ')
elif (85<=ortalama<=100):
    print('sonuc:100 ')
else:
    print('yanlis bilgi girildi.')
        '''
#3 trafikteki gun sayisi girilen aracin bakim zamanini hesaplayin.
#1.bakim->1.yil
#2.bakim->2.yil

#datetime modülünü kullanin.

import datetime #datetime modulu yuklenir
tarih=input('trafige cikis tarihini giriniz: yil/ay/gun ')
tarih=tarih.split('/') #nokta karakterinden ayrilir
suan=datetime.datetime.now() #simdinin tarih bilgisi
trafigeCikisTarihi=datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
fark=suan-trafigeCikisTarihi
print(fark)

if (fark.days<=365):  #gun sayimi yapilir.
    print('"1.bakim yili geldi"')
elif (365<fark.days<=730):
    print('2.bakim yili geldi')
else:
    print('hatali giris yapildi')












