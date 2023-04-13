from selenium import webdriver
import time 

driver = webdriver.Chrome('./chromedriver')
driver.get('https://ticketplus.com.tw/activity/e1d789a22aaaf3d52b88801b0ce9f860')
driver.maximize_window()
time.sleep(2)
driver.find_element("xpath","//*[@id='appBar']/div/div/div/button").click()



time.sleep(100)