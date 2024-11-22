from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from instagramUserInfo import username,password
import time

class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.browser=webdriver.Chrome()

    def logIn(self):
        logInURL="https://www.instagram.com/"
        self.browser.get(logInURL)
        time.sleep(2)
        enterUsername=self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
        enterPassword=self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")
        enterUsername.send_keys(username)
        enterPassword.send_keys(password)
        enterPassword.send_keys(Keys.ENTER)
        time.sleep(3)
        seeFollowersURL="https://www.instagram.com/daily_1solo/followers"
        self.browser.get(seeFollowersURL)
        time.sleep(2)
        #seeFollower=self.browser.find_element(By.CSS_SELECTOR,"//*[@id='mount_0_0_wR'/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]")
        #seeFollower.click()
        seeFollower=self.browser.find_element(By.CSS_SELECTOR,".x78zum5.x1q0g3np.xieb3on").find_element(By.TAG_NAME,"a").click()
        output=self.browser.find_element(By.CSS_SELECTOR,"div[role=dialog]").find_elements(By.CSS_SELECTOR,".x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3")
        for user in output:
            a=user.find_element(By.CSS_SELECTOR,"_ap3a._aaco._aacw._aacx._aad7._aade")
            print(a)       
           

    def seeFollowers(self):
        seeFollowersURL="https://www.instagram.com/daily_1solo/followers"
        self.browser.get(seeFollowersURL)
        time.sleep(2)
        #seeFollower=self.browser.find_element(By.CSS_SELECTOR,"//*[@id='mount_0_0_wR'/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]")
        #seeFollower.click()
        seeFollower=self.browser.find_element(By.CSS_SELECTOR,"div[role=dialog]").find_elements(By.CSS_SELECTOR,"div")
        for user in seeFollower:
            output=user.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
            print(output)
        
        x=input('type exit to exit')
        while True:
            pass
            if (x=='exit'):
                break
            else:
                continue
                    

instagram=Instagram(username=username,password=password)
while True:
    menuText="Instagram App"
    menuText=menuText.center(50,'*')
    print(menuText)
    userChoice=input('\nSelect a Choice\n1-Log in\n2-See followers\n3-Exit\nChoice:\n')
    if (userChoice=='1'):
        instagram.logIn()
    elif(userChoice=='2'):
        instagram.seeFollowers()
    elif (userChoice=='3'):
        break
    else:
        print('Wrong input!')

        


