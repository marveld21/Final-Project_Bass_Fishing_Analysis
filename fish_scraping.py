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


#make sure correct working path is selected
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




#post login

Angler_Name = []
Species = []
Weight = []
Bait = []
Area = []
Cover = []
Depth = []
Recorded_Time = []
Tournament_Day = []


#go to redcrest 2021 page look at ending of url for range
Tournament_Days_URL=range(61, 62)
T_Day = 0
for Tournament_Days in Tournament_Days_URL:
    T_Day = T_Day + 1
    print('Tournament Day =',T_Day)
    Tournament_URL = 'https://majorleaguefishing.com/results/?c=1000505&y=2022&e=1875391&r=61' #+str(Tournament_Days)
    print(Tournament_URL)
    driver.get(Tournament_URL)
    
    #wait 2 sec
    sleep(2)
    
    anglers = driver.find_element("tag name","tr")
  
    sleep(1)
    
    angler_count = len(driver.find_elements("xpath",'//*[@id="data-component"]/div[2]/table/tbody/tr'))
    print(angler_count)
    
    if angler_count <= 20:
        
    
        z=range(0,angler_count+1)
        
        for x in z:
            x=1# this is for test
            redline = len(driver.find_elements("xpath",'//*[@id="data-component"]/div[2]/table/tbody/tr['+str(x)+']/td'))
            print(redline)
            if redline > 2:
                
                print(x-1)
                
                anglerxpath = '//*[@id="data-component"]/div[2]/table/tbody/tr['+str(x)+']/td[3]/a'
                A_N = driver.find_element("xpath",anglerxpath).text
                #clicks angler name to bring up fish caught
                driver.find_element("xpath",anglerxpath).click()
                sleep(2)    
                #counts fish caught to run next for loop
                matches = driver.find_elements("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr')
                fish_data = 0
                
                for match in matches:
                    Angler_Name.append(A_N)
                    fish_data = fish_data + 1
                    Species.append(match.find_element("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr['+str(fish_data)+']/td[1]').text)
                    Weight.append(match.find_element("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr['+str(fish_data)+']/td[2]').text)
                    Bait.append(match.find_element("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr['+str(fish_data)+']/td[4]').text)
                    Area.append(match.find_element("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr['+str(fish_data)+']/td[5]').text)
                    Cover.append(match.find_element("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr['+str(fish_data)+']/td[6]').text)
                    Depth.append(match.find_element("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr['+str(fish_data)+']/td[7]').text)
                    Recorded_Time.append(match.find_element("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr['+str(fish_data)+']/td[8]').text)
                    Tournament_Day.append(T_Day)
                driver.get(Tournament_URL)
                sleep(1)
            
            else: print("redline")
    
    elif angler_count > 20:
        
        z=range(0,20)
        
        for x in z:
            
            redline = len(driver.find_elements("xpath",'//*[@id="data-component"]/div[2]/table/tbody/tr['+str(x)+']/td'))
            if redline > 2:
                
                print(x-1)
                
                anglerxpath = '//*[@id="data-component"]/div[2]/table/tbody/tr['+str(x)+']/td[3]/a'
                A_N = driver.find_element("xpath",anglerxpath).text
                #clicks angler name to bring up fish caught
                driver.find_element("xpath",anglerxpath).click()
                sleep(2)    
                #counts fish caught to run next for loop
                matches = driver.find_elements("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr')
                fish_data = 0
                for match in matches:
                    Angler_Name.append(A_N)
                    fish_data = fish_data + 1
                    Species.append(match.find_element("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr['+str(fish_data)+']/td[1]').text)
                    Weight.append(match.find_element("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr['+str(fish_data)+']/td[2]').text)
                    Bait.append(match.find_element("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr['+str(fish_data)+']/td[4]').text)
                    Area.append(match.find_element("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr['+str(fish_data)+']/td[5]').text)
                    Cover.append(match.find_element("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr['+str(fish_data)+']/td[6]').text)
                    Depth.append(match.find_element("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr['+str(fish_data)+']/td[7]').text)
                    Recorded_Time.append(match.find_element("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr['+str(fish_data)+']/td[8]').text)
                    Tournament_Day.append(T_Day)
                driver.get(Tournament_URL)
                sleep(1)
        
        #move window to see
        driver.execute_script("window.scrollBy(0,1000)", "")
        z=range(20,angler_count+1)
        
        for x in z:
            
            redline = len(driver.find_elements("xpath",'//*[@id="data-component"]/div[2]/table/tbody/tr['+str(x)+']/td'))
            if redline > 2:
            
                print(x-1)
                
                anglerxpath = '//*[@id="data-component"]/div[2]/table/tbody/tr['+str(x)+']/td[3]/a'
                A_N = driver.find_element("xpath",anglerxpath).text
                driver.find_element("xpath",anglerxpath).click()
                sleep(2)    
                matches = driver.find_elements("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr')
                fish_data = 0
                for match in matches:
                    Angler_Name.append(A_N)
                    fish_data = fish_data + 1
                    Species.append(match.find_element("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr['+str(fish_data)+']/td[1]').text)
                    Weight.append(match.find_element_("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr['+str(fish_data)+']/td[2]').text)
                    Bait.append(match.find_element("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr['+str(fish_data)+']/td[4]').text)
                    Area.append(match.find_element("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr['+str(fish_data)+']/td[5]').text)
                    Cover.append(match.find_element("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr['+str(fish_data)+']/td[6]').text)
                    Depth.append(match.find_element("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr['+str(fish_data)+']/td[7]').text)
                    Recorded_Time.append(match.find_element("xpath",'/html/body/div[6]/div/div/div[2]/div[3]/table/tbody/tr['+str(fish_data)+']/td[8]').text)
                    Tournament_Day.append(T_Day)
                driver.get(Tournament_URL)
                sleep(1)
            
            

driver.quit()

df = pd.DataFrame({'Angler_Name':Angler_Name,'Species': Species,'Weight':Weight,'Bait':Bait,'Area':Area,'Cover':Cover,'Depth':Depth,'Recorded_Time':Recorded_Time,'Tournament_Day':Tournament_Day})
df['Depth'] = df['Depth'] + 'ft'
df['Weight'] = df['Weight'] + 'lbs-oz'
df.to_csv('scrape_test_fishing_data.csv', index=False)
print(df)