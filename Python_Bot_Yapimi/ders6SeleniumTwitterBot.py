
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from twitterUserInfo import username,password
import time

class Twitter:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.browserProfile=webdriver.ChromeOptions()
        #self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages':'en,en_US'})
        self.browser=webdriver.Chrome()

    def logIn(self):
        logInURL="https://x.com/i/flow/login"
        self.browser.get(logInURL)
        time.sleep(3)
        enterUsername=self.browser.find_element(By.XPATH,"//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input")
        enterUsername.send_keys(self.username)
        enterUsername.send_keys(Keys.ENTER)
        time.sleep(3)
        enterPassword=self.browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]").click( )
        enterPassword.send_keys(self.password)
        enterPassword.send_keys(Keys.ENTER)
        time.sleep(3)    
        x=input('type exit to exit')
        while True:
            pass
            if (x=='exit'):
                break
            else:
                continue
                    

twitter=Twitter(username=username,password=password)
while True:
    menuText="Twitter App"
    menuText=menuText.center(50,'*')
    print(menuText)
    userChoice=input('\nSelect a Choice\n1-Log in\n2-See followers\n3-Exit\nChoice:\n')
    if (userChoice=='1'):
        twitter.logIn()
    elif(userChoice=='2'):
        pass
    elif (userChoice=='3'):
        break
    else:
        print('Wrong input!')

        
