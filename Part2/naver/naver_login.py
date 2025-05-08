from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyperclip
import time

option = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.get('https://nid.naver.com/nidlogin.login?realname=Y&type=modal&svctype=262144&returl=https%3A%2F%2Fmy.naver.com')

time.sleep(2)

pyperclip.copy('naserpqwl7125')
driver.find_element(By.NAME,'id').send_keys(Keys.CONTROL,'v')
time.sleep(1)

pyperclip.copy('KUROMA472019!')
e = driver.find_element(By.NAME,'pw')
e.send_keys(Keys.CONTROL,'v')
time.sleep(1)

e.send_keys(Keys.ENTER)

input('enter')
driver.quit()