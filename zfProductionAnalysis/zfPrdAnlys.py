import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import os

'''
komut satırından girilen veriseti adı ile işlemler gerçekleştirilir.
'''
class Production:
    def __init__(self):
        try:
            # database bağlantısı sağlanır
            self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="373737",  
            database="zfprodanalysis"  
            )
            print("Veritabanına başarıyla bağlanıldı.")
            self.cursor=self.conn.cursor()
        except mysql.connector.Error as err:
            # bağlantı hatası olursa çıkar.
            print(f"Veritabanı bağlantı hatası: {err}")
            exit()
    def readValues(self):
            # SQL sorgusunu tanımla
            query = "SELECT * FROM production"
            # Sorguyu çalıştır
            self.cursor.execute(query)
            # Sonuçları al
            results = self.cursor.fetchall()
            # Sonuçları yazdır
            for row in results:
                print(
                    f"id {row[0]}, Tarih {row[1]}, Vardiya {row[2]}, Makine {row[3]}, Operatör {row[4]}, "
                    f"Parça_Kodu {row[5]}, Başlangıç_Zamanı {row[6]}, Bitiş_Zamanı {row[7]}, "
                    f"Toplam_İş_Süresi {row[8]}, Toplam_Duruş_Süresi {row[9]}, Duruşsuz_Süre {row[10]}, "
                    f"Toplam_Duruş {row[10]}, İş_Yok_35 {row[11]}, Vardiya_Sonu_88 {row[11]}, "
                    f"Belirsiz_Duruş_0 {row[12]}, Yemek_Molası_80 {row[13]}, Çay_Molası_81 {row[14]}, "
                    f"Op_Tez_Müd_45 {row[15]}, Referans_Değişimi_6 {row[16]}, Proje_Çalışması_1111 {row[17]}, "
                    f"Günlük_Bak_Temiz_15 {row[18]}, Kesici_Değiştirme_18 {row[19]}, OP_AYAR_HATASI_63 {row[20]}, "
                    f"Kişisel_İhtiyaç_10 {row[21]}, Sıkma_Ringi_Mon_44 {row[22]}, "
                    f"İkinci_Tezgah_Çalış_25 {row[23]}, Malzeme_Aktarma_20 {row[24]}, "
                    f"MEKANİK_ARIZA_62 {row[25]}, Ekip_Lider_İşi_73 {row[26]}, Paketleme_30 {row[27]}, "
                    f"Operatör_Parça_Ölçüm_12 {row[28]}, ÇY_DESTEK_89 {row[29]}, "
                    f"ELEKTRİK_ARIZASI_58 {row[30]}, Operatöre_Teslim_9998 {row[31]}, "
                    f"Bakımcı_Bekleme_46 {row[32]}, PNÖMATİK_ARIZA_61 {row[33]}, "
                    f"TEZ_Ayar_Problemi_69 {row[34]}, F_Parça_Götürme_72 {row[35]}, "
                    f"Takımhaneye_Gitme_4 {row[36]}, Dökümantasyon_13 {row[37]}, "
                    f"Kasacı_Bekleme_16 {row[38]}, Kalıp_Parça_Götürme_36 {row[39]}, "
                    f"HOMMEL_MAF_Ölçüm_49 {row[40]}, Kalıp_Apara_Bekleme_47 {row[41]}, "
                    f"Kalıp_Ölçüm_Bekleme_37 {row[42]}, Talaş_Sarma_94 {row[43]}, "
                    f"Markalama_22 {row[44]}, Tezgah_Soğuma_Bekleme_86 {row[45]}, "
                    f"Yağ_Su_Ekleme_11 {row[46]}, Talaş_Akıtma_19 {row[47]}, "
                    f"Ayar_Kontrol_Bekleme_71 {row[48]}, AYAR_Kont_Ölçüm_28 {row[49]}, "
                    f"Kalıp_Arıza_Teslim_68 {row[50]}, Parça_Ayıklama_23 {row[51]}, "
                    f"Önceki_Operatör_Bekleme_21 {row[52]}, POKE_YOKE_Kontrol_74 {row[53]}, "
                    f"Operatör_Bekleme_39 {row[54]}, Kalite_Ölçüm_38 {row[55]}, "
                    f"Arıza_Tespit_9995 {row[56]}, Toplantı_Eğitim_Televizyon_Görüşme_5 {row[57]}, "
                    f"Performans_Seçim {row[58]}, Sağlam_Üretim {row[59]}, "
                    f"Yapılabilir_Çalışılan {row[60]}, Toplam_Parça {row[61]}","\n")
    def addValues(self,fileName):   
        self.conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="373737",  
        database="zfprodanalysis" ) 
        print("Veritabanına başarıyla bağlanıldı.")
        self.cursor=self.conn.cursor()
        # girişte alınan değerler liste içine alınır.
        self.fileName=fileName
        # Veriler okunur ve dataframe haline getirilir.
        file=f"{fileName}.csv"
        dt=pd.read_csv(file,encoding='utf-8')
        # CSV dosyasını oku
        df=pd.DataFrame(dt)
        # Kolon bilgisi alma için algoritma.
        column = df.loc[2]
        # Kolonlar ayrıştırılır.
        columns = [satir.split(';') for satir in column]
        columnsList=[]
        # DataFrame oluşturma
        for row in columns:
            for i in row:
                columnsList.append(i)
        # Tüm satırı gösterme ayarlarını yapma
        pd.set_option('display.max_colwidth', None)
        pd.set_option('display.expand_frame_repr', False)
        values=[]
        # For döngüsü index hesabı yapilir.
        indexNumber=(df.index.max()-1)
        # Anlamlı veri aralığı seçilir.
        for k in range (4,indexNumber):
             # Veriyi string şekilde alınır.
            dataStr = str(df.loc[k])
             # Gereksiz kısımları kaldırma
            cleanData = dataStr.replace("Operatör Duruş;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;", " ").replace(f"Name: {k}, dtype: object", "").strip()
            # Noktalı virgülle ayrılmış öğeleri listeye atma
            data = cleanData.split(';')
            # Veri listesine degerler eklenir.
            values.append(data)
        # Anlamsiz veriler cikarilir.
        values.pop(164)
        values.pop(341)
        #dataframe formatinda geçici dosya alinir.,
        df=pd.DataFrame(data=values)
        df.to_csv(f"{self.fileName}Temp.csv")    
        # geçici dosya okunarak gerekli düzeltmeler yapılır.
        file2 =f"{self.fileName}Temp.csv"  
        df2 = pd.read_csv(file2)
        df2['3'] = df2['3'].replace('-', 'Operatör yok')
        df2['4'] = df2['4'].replace('-', 'Parça kodu yok')
        df2.fillna(0, inplace=True) 
        # Dosyanın son hali okunur.
        df2.to_csv(f"{self.fileName}Out.csv")    
        # CSV dosyasını okuyun
        file2 =f"{self.fileName}Out.csv"  
        # Son hali okununca geçici versiyon silinir.
        if os.path.exists(f"{self.fileName}Temp.csv"):
            os.remove(f"{self.fileName}Temp.csv")
            print(f"{f"{self.fileName}Temp.csv"} başarıyla silindi.")
        else:
            print(f"{self.fileName}Temp bulunamadı.")
        # DataFrame'deki her satırı tuple olarak listeye çevirme
        values_list = [tuple(x) for x in df2.to_numpy()]
        # SQL INSERT sorgusu
        query = """
        INSERT INTO production (id, Tarih, Vardiya, Makine, Operatör, Parça_Kodu, Başlangıç_Zamanı, Bitiş_Zamanı, Toplam_İş_Süresi, Toplam_Duruş_Süresi, Duruşsuz_Süre, Toplam_Duruş, İş_Yok_35, Vardiya_Sonu_88, Belirsiz_Duruş_0, Yemek_Molası_80, Çay_Molası_81, Op_Tez_Müd_45, Referans_Değişimi_6, Proje_Çalışması_1111, Günlük_Bak_Temiz_15, Kesici_Değiştirme_18, OP_AYAR_HATASI_63, Kişisel_İhtiyaç_10, Sıkma_Ringi_Mon_44, İkinci_Tezgah_Çalış_25, Malzeme_Aktarma_20, MEKANİK_ARIZA_62, Ekip_Lider_İşi_73, Paketleme_30, Operatör_Parça_Ölçüm_12, ÇY_DESTEK_89, ELEKTRİK_ARIZASI_58, Operatöre_Teslim_9998, Bakımcı_Bekleme_46, PNÖMATİK_ARIZA_61, TEZ_Ayar_Problemi_69, F_Parça_Götürme_72, Takımhaneye_Gitme_4, Dökümantasyon_13, Kasacı_Bekleme_16, Kalıp_Parça_Götürme_36, HOMMEL_MAF_Ölçüm_49, Kalıp_Apara_Bekleme_47, Kalıp_Ölçüm_Bekleme_37, Talaş_Sarma_94, Markalama_22, Tezgah_Soğuma_Bekleme_86, Yağ_Su_Ekleme_11, Talaş_Akıtma_19, Ayar_Kontrol_Bekleme_71, AYAR_Kont_Ölçüm_28, Kalıp_Arıza_Teslim_68, Parça_Ayıklama_23, Önceki_Operatör_Bekleme_21, POKE_YOKE_Kontrol_74, Operatör_Bekleme_39, Kalite_Ölçüm_38, Arıza_Tespit_9995, Toplantı_Eğitim_Televizyon_Görüşme_5, Performans_Seçim, Sağlam_Üretim, Yapılabilir_Çalışılan, Toplam_Parça
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
                     %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s)
                    """
        for n in range (len(values_list)):
              # Veriyi MySQL'e aktar
            try:
                self.cursor.execute(query, values_list[n])
                # Veritabanı değişikliklerini kaydet ve bağlantıyı kapat
                self.conn.commit()
                print("DataFrame başarıyla MySQL veritabanına aktarıldı!")
            except mysql.connector.Error as err:
                print(f"Hata: {err}")
            # Bağlantıyı kapatma
        self.cursor.close()
        self.conn.close()
    def deleteValues(self):
        # veri silme için sorgu oluşturulur.
        sql = "DELETE FROM production"
        # Verileri silme
        self.cursor.execute(sql)
        self.conn.commit()  # Değişiklikleri kaydet
        self.cursor.close()
        self.conn.close()
        print("Tüm veriler başarıyla silindi!")
    def writeValues(self):
        #veri tabanı okunur.
        file="cleanData.csv"
        df=pd.read_csv(file)
        #DataFrame'deki her satırı tuple olarak listeye çevirme
        values_list = [tuple(x) for x in df.to_numpy()]
        # SQL sorgusu
        query = """
        INSERT INTO production (id, Tarih, Vardiya, Makine, Operatör, Parça_Kodu, Başlangıç_Zamanı, Bitiş_Zamanı, Toplam_İş_Süresi, Toplam_Duruş_Süresi, Duruşsuz_Süre, Toplam_Duruş, İş_Yok_35, Vardiya_Sonu_88, Belirsiz_Duruş_0, Yemek_Molası_80, Çay_Molası_81, Op_Tez_Müd_45, Referans_Değişimi_6, Proje_Çalışması_1111, Günlük_Bak_Temiz_15, Kesici_Değiştirme_18, OP_AYAR_HATASI_63, Kişisel_İhtiyaç_10, Sıkma_Ringi_Mon_44, İkinci_Tezgah_Çalış_25, Malzeme_Aktarma_20, MEKANİK_ARIZA_62, Ekip_Lider_İşi_73, Paketleme_30, Operatör_Parça_Ölçüm_12, ÇY_DESTEK_89, ELEKTRİK_ARIZASI_58, Operatöre_Teslim_9998, Bakımcı_Bekleme_46, PNÖMATİK_ARIZA_61, TEZ_Ayar_Problemi_69, F_Parça_Götürme_72, Takımhaneye_Gitme_4, Dökümantasyon_13, Kasacı_Bekleme_16, Kalıp_Parça_Götürme_36, HOMMEL_MAF_Ölçüm_49, Kalıp_Apara_Bekleme_47, Kalıp_Ölçüm_Bekleme_37, Talaş_Sarma_94, Markalama_22, Tezgah_Soğuma_Bekleme_86, Yağ_Su_Ekleme_11, Talaş_Akıtma_19, Ayar_Kontrol_Bekleme_71, AYAR_Kont_Ölçüm_28, Kalıp_Arıza_Teslim_68, Parça_Ayıklama_23, Önceki_Operatör_Bekleme_21, POKE_YOKE_Kontrol_74, Operatör_Bekleme_39, Kalite_Ölçüm_38, Arıza_Tespit_9995, Toplantı_Eğitim_Televizyon_Görüşme_5, Performans_Seçim, Sağlam_Üretim, Yapılabilir_Çalışılan, Toplam_Parça
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
          %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
          %s, %s, %s, %s)
        """
        # DataFrame'deki verileri MySQL'e ekleme
        self.cursor.executemany(query, values_list)
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
    def averageValues(self):
        sql="SELECT AVG(Toplam_İş_Süresi) from production"
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        print(f"AVG(Toplam_İş_Süresi) {result[0]}")
        self.cursor.close()
        self.conn.close()
    def dataAnalysis(self):
        sql = "SELECT * FROM users WHERE Operating_System LIKE '%Android%' "
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        androidCount=len(result)
        sql = "SELECT * FROM u sers WHERE Operating_System LIKE '%iOs%' "
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        iOSCount=len(result)
        print(androidCount,iOSCount)
        dataTypes="android","iOS"
        counts=[androidCount,iOSCount]
        colors=["blue","red"]
        plt.subplot(1, 2, 1)
        plt.pie(counts,labels=dataTypes,colors=colors,autopct='%1.0f%%')
        plt.title('Kullanıcı Dağılımı')
        # Bar grafiği
        sql_android = "SELECT AVG(Screen_On_Time) FROM users WHERE Operating_System LIKE '%Android%'"
        self.cursor.execute(sql_android)
        avg_android = self.cursor.fetchone()[0]
        # iOS kullanıcılarının ortalama ekran süresini almak için SQL sorgusu
        sql_ios = "SELECT AVG(Screen_On_Time) FROM users WHERE Operating_System LIKE '%iOs%'"
        self.cursor.execute(sql_ios)
        avg_ios = self.cursor.fetchone()[0]
        # Verileri grafik için hazırlama
        operating_systems = ['Android', 'iOS']
        average_screen_times = [avg_android, avg_ios]
        # Çubuk grafiği oluşturma
        plt.subplot(1, 2, 2)
        plt.bar(operating_systems, average_screen_times, color=['blue', 'red'], alpha=0.7)
        # Başlık ve etiketler
        plt.title('Ortalama Ekran Süreleri')
        plt.xlabel('İşletim Sistemi')
        plt.ylabel('Ortalama Ekran Süresi (Saat)')
    # Değerleri grafik üzerinde gösterme
        for i, v in enumerate(average_screen_times):
            plt.text(i, v + 0.05, f"{v:.2f}", ha='center', va='bottom')  # Değerleri yazdır
    # Grafiği göster
        plt.tight_layout()
        plt.show()
    # Bağlantıyı kapatma
        self.cursor.close()
        self.conn.close()
    def closeConnection(self):
        # Bağlantıyı kapatma
        self.cursor.close()
        self.conn.close()
        print("Veritabanı bağlantısı kapatıldı.")
        exit()
while True:
    # Kullanıcıdan veri girişi
    userChoice=input("islem seciniz:\n1-Verileri ekle\n2-Verileri oku\n3-Verileri yaz\n4-Verileri sil\n5-Baglantiyi kopart\n6-Ortalama getir\n7-Analiz yap\n")
    if(userChoice=="1"):
        try:
            fileName = input("dosya adi: ")
            result=Production()
            result.addValues(fileName)
            another_entry = input("Başka bir islem yapmak ister misiniz? (E/H): ")
            if (another_entry.lower() != 'e'):
                break
            continue
        except mysql.connector.Error as err:
            print(f"{err}")
            break
        finally:
            print("blok calisti")
    elif(userChoice=="2"):
        result=Production()
        result.readValues()
    elif(userChoice=="3"):
        result=Production()
        result.writeValues()
    elif(userChoice=="4"):
        result=Production()
        result.deleteValues()
    elif(userChoice=="5"):
        result=Production()
        result.closeConnection()
    elif(userChoice=="6"):
        result=Production()
        result.averageValues()    
    elif(userChoice=="7"):
        result=Production()
        result.dataAnalysis()   
    else:
        print("hatali giris")
    
