from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome() #chrome browser atamasi yapildi

url="https://www.google.com.tr/" #kaynak url eklendi
driver.get(url) #tarayici get fonk. ile url yi açtı
#ime.sleep(1) #1 saniye bekledi
driver.maximize_window() #ekran kaplandi
#clickAccept=driver.find_element(By.ID,"L2AGLb").click()
print(driver.title) #tarayici basligi yazdirildi
searchInput=driver.find_element(By.ID,"APjFqb")  
#time.sleep(1)
searchInput.send_keys("zf group"+Keys.ENTER)
driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3").click()
while True:
    pass

