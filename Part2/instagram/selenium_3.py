from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
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
time.sleep(1)

# 비밀번호 입력
driver.find_element(By.NAME, 'password').send_keys(os.getenv('instagrampw'))
time.sleep(1)

driver.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[3]/button/div').click()
time.sleep(5)

# 페이지이동
driver.get('https://www.instagram.com/explore/search/keyword/?q=%23사과')

driver.implicitly_wait(10)

# elements는 여러가지 리스트
driver.find_element(By.CLASS_NAME,'_aagw').click() # 첫번째 사진
time.sleep(2)

# 이미지 시도
img = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[1]/div/div[1]/div[2]/div/div/div/ul/li[2]/div/div/div/div/div[1]/img")
imgurl = img.get_attribute('src')

urllib.request.urlretrieve(imgurl, '1.jpg')

input('enter')
driver.close()