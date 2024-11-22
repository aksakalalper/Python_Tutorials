from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome() #chrome browser atamasi yapildi

sourceUrl="https://orteil.dashnet.org/cookieclicker/" #kaynak url eklendi
driver.get(sourceUrl) #tarayici get fonk. ile url yi açtı
driver.maximize_window() #ekran kaplandi
time.sleep(1) #1 saniye bekledi

while True:
    actions=ActionChains(driver=driver) #actions chains kutuphanesi basit tiklamalar ve mouse hareketleri icin kullanilir.
    cookieCount=driver.find_element(By.ID,"cookies").text
    cookieClick=driver.find_element(By.ID,"bigCookie").click()
    print(cookieCount)
    pass

#actions.click()
#actions.perform()




