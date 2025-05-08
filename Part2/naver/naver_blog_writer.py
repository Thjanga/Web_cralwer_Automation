from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import pyperclip
import pyautogui
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.get('https://nid.naver.com/nidlogin.login')

time.sleep(2)
pyperclip.copy('naserpqwl7125')  
driver.find_element(By.NAME, 'id').send_keys(Keys.CONTROL, 'v')
time.sleep(1)

pyperclip.copy('KUROMA472019!') 
pw_input = driver.find_element(By.NAME, 'pw')
pw_input.send_keys(Keys.CONTROL, 'v')
time.sleep(1)

pw_input.send_keys(Keys.ENTER)  

time.sleep(3)
driver.get('https://blog.naver.com/031008_/postwrite')
time.sleep(2)

driver.implicitly_wait(10)

pyautogui.click(239, 791)  # 화면 기준 좌표
pyautogui.write("test title")

time.sleep(2)

iframe = driver.find_element(By.CSS_SELECTOR, "iframe[id^='input_buffer']")
driver.switch_to.frame(iframe)

e = driver.find_element(By.CSS_SELECTOR, '[contenteditable="true"]')
e.send_keys('test body')

driver.switch_to.default_content()

time.sleep(2)
input('enter')
driver.quit()
