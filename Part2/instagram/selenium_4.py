from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.request
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
import os

load_dotenv()
driver = webdriver.Chrome()
driver.get('https://instagram.com')
time.sleep(1)

# 로그인
driver.find_element(By.NAME, 'username').send_keys(os.getenv('instagramid'))
driver.find_element(By.NAME, 'password').send_keys(os.getenv('instagrampw'))
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button/div').click()
time.sleep(5)

# 페이지 이동
driver.get('https://www.instagram.com/explore/search/keyword/?q=%23사과')
driver.implicitly_wait(10)

# 첫 번째 게시물 클릭
driver.find_element(By.CLASS_NAME, '_aagw').click()
time.sleep(2)

for i in range(2):
    img = driver.find_elements(By.XPATH, "//div[contains(@class, '_aagv')]//img")[i].get_attribute('src')
    urllib.request.urlretrieve(img, f'{i+1}.jpg')
    print(f"{i+1}.jpg 저장 완료")

    # 다음 게시물로 이동
    next_btn = driver.find_element(By.XPATH, "//div[contains(@class, '_aaqg')]/button")
    next_btn.click()
    time.sleep(1)


input('enter')
driver.close()
