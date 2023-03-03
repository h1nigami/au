import time
import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By


login = str(input("Логин:"))
pss = str(input("Пароль:"))
print("Ты даун?")
browser = webdriver.Firefox()
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
options.headless = True
options.set_preference('dom.webdriver.enabled', False)
options.set_preference('dom.image-lazy-loading.enabled', False)
browser.get('https://zelenka.guru/forums/contests/')
driver = webdriver.Firefox(options=options)


def autouchastie(): 
   while True:
    try:     
       time.sleep(1.5)
       browser.refresh()
       time.sleep(1.5)
       block = browser.find_element(By.CLASS_NAME, "discussionListItem--Wrapper")
       block.click()
       time.sleep(1.5)
       uchastie = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div/form/ol/li/div[2]/div[3]/article/div/a")     
       uchastie.click()      
      #  simp = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div/form/ol/li/div[2]/div[3]/div/div[2]/a/span[1]")
      #  simp.click()    
       browser.get('https://zelenka.guru/forums/contests/')       
    except Exception as e:
       print(e)
       browser.get('https://zelenka.guru/forums/contests/')
       time.sleep(60)
       
def authorization():
 button = browser.find_element(By.XPATH, "/html/body/header/div/div[3]/nav/div/div/a[1]")
 button.click()
 log = browser.find_element(By.NAME, "login")
 log.send_keys(login)
 password = browser.find_element(By.NAME, "password")
 password.send_keys(pss)
 log_in = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div/form/div[5]/input")
 log_in.click()
 dva = str(input("Двухфакторка:"))
 dvuxfactorka = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div/form/input[1]")
 time.sleep(20)
 dvuxfactorka.send_keys(dva)
 succes = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div/form/div[2]/input")
 succes.click()
 time.sleep(5)
 flazhok = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div/div/div[3]/div[1]/a[2]")
 flazhok.click()


if __name__ == '__main__':
   authorization()
   autouchastie()
   



