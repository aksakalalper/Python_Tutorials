from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from githubUserInfo import username,password
import time

class Github:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.browser=webdriver.Chrome()
        self.sourceUrl="https://github.com/login"

    def logIn(self):
        contents=[]
        self.browser.get(self.sourceUrl)
        time.sleep(1)
        self.browser.maximize_window()
        self.browser.find_element(By.XPATH,"//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element(By.XPATH,"//*[@id='password']").send_keys(self.password)
        time.sleep(1)
        self.browser.find_element(By.XPATH,"//*[@id='login']/div[4]/form/div/input[13]").click()
        self.browser.get("https://github.com/aksakalalper?tab=repositories")
        content=self.browser.find_elements(By.CLASS_NAME,"d-inline-block mb-1")
        print(type(content))
        print(content)
        print(contents)
        while True:
            pass
gitHub=Github(username=username,password=password)
x=gitHub.logIn()
        
