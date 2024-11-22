from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome() #chrome browser atamasi yapildi

url="https://tr.wikipedia.org/wiki/Mao_Zedong" #kaynak url eklendi
driver.get(url) #tarayici get fonk. ile url yi açtı

time.sleep(1) #2 saniye bekledi
driver.maximize_window() #ekran kaplandi
print(driver.title) #tarayici basligi yazdirildi
time.sleep(2) 
driver.close() #tarayici kapatildi.
searchInput=driver.find_element(By.CLASS_NAME,"cdx-text-input__input")  # type: ignore
time.sleep(1)
searchInput.send_keys("python")
searchInput.send_keys(Keys.ENTER)
showOutput=driver.find_element(By.XPATH,"//*[@id='mw-content-text']/div[1]/table[1]")
print(showOutput.text)
time.sleep(5)
driver.close()
