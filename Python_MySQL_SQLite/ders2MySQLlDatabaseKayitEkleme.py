import mysql.connector

def insertProduct(list):
    # Veritabanı bağlantısı oluştur
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="373737",
    database="node-app")

# Bir cursor oluştur
    cursor = conn.cursor()

# Veri ekleme
    sql = "INSERT INTO product (productName, productPrice, imageURL, description) VALUES (%s, %s, %s, %s)"
    values = list
    cursor.executemany(sql, values)

# Veritabanına değişiklikleri kaydetme
    conn.commit()

# Bağlantıyı kapatma
    cursor.close()
    conn.close()

list=[]

while True:
    name=input("isim: ")
    price=input("fiyat: ")
    imageURL=input("adres: ")
    description=input("tanim: ")
    list.append((name,price,imageURL,description))
    userChoice=input("devam e/h")

    if (userChoice=="e"):
        print("devam ediliyor")
        continue
    elif(userChoice=="h"):
        #insertProduct(name=name,price=price,imageURL=imageURL,description=description)
        insertProduct(list)
        print("listelere eklendi.")
        break
    else:
        print("hatali giris")