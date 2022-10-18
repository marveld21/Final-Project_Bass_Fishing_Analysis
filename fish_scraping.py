import undetected_chromedriver as uc
import selenium
import time
import pandas as pd

from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from configparser import ConfigParser
config_1 = ConfigParser()
config_1.read('config.ini')

username = config_1['login']['un']
password = config_1['login']['pw']

options = webdriver.chromium.options.ChromiumOptions
options.headless=False

MLF_URL = "https://majorleaguefishing.com/"

print("start")
#go to site
driver = uc.Chrome()
driver.get(MLF_URL)
sleep(0.5)


#click user button
driver.find_element(By.XPATH, '/html/body/header/nav/div/div[3]/div[2]/a').click()
#input user and pw and submit
driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/form/div[1]/input").send_keys(username)
driver.find_element(By.XPATH, "/html/body/div[5]/div/div/div[2]/form/div[2]/input").send_keys(password)
driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[2]/form/input').click()
#wait 1 second after login
sleep(1)

driver.quit()
