from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# .env 사용하려고 할 때
from dotenv import load_dotenv
import os

# .env file load
load_dotenv()

driver = webdriver.Chrome()
driver.get('https://instagram.com')
time.sleep(1)

# 아이디 입력
driver.find_element(By.NAME, 'username').send_keys(os.getenv('instagramid'))

# 비밀번호 입력
driver.find_element(By.NAME, 'password').send_keys(os.getenv('instagrampw'))

driver.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[3]/button/div').click()

input('enter')
driver.close()