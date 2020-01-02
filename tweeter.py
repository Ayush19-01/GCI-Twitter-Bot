#Made for the sole purpose of GCI 2019
from selenium import webdriver
import time
import pyautogui
import feedparser
a=feedparser.parse("https://fedoramagazine.org/feed/")
title=a["entries"][0]["title"]
link=a["entries"][0]["links"][0]["href"]
toadd="Have a read on this latest fedora magazine article on\n"+title+"\nClick to read the article:"+link
a=input("Enter twitter username:")
b=input("Enter twitter password:")
driver = webdriver.Chrome("./chromedriver")
driver.get("https://twitter.com/login")
username = driver.find_element_by_css_selector("input[placeholder='Phone, email or username']")
password= driver.find_element_by_css_selector("input[class='js-password-field']")
username.send_keys(a)
password.send_keys(b)
time.sleep(3)
submit = driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button')
submit.click()
time.sleep(7)
for i in range(14):
    pyautogui.press('tab')
time.sleep(1)
pyautogui.typewrite(toadd)
time.sleep(1)
for i in range(6):
    pyautogui.press('tab')
pyautogui.press('enter')
print("TWEET COMPLETED!")
