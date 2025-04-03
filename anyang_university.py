from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
# .env 사용하려고 할 때
from dotenv import load_dotenv
import os

# .env file load
load_dotenv()

driver = webdriver.Chrome()
driver.get('https://cyber.anyang.ac.kr/')
time.sleep(3)

# 아이디 입력
driver.find_element(By.NAME, 'username').send_keys(os.getenv('uid'))

# 비밀번호 입력
driver.find_element(By.NAME, 'password').send_keys(os.getenv('upw'))

driver.find_element(By.CLASS_NAME,'main_login_btn').click()
driver.find_element(By.CLASS_NAME,'close_notice').click()
# driver.find_element(By.XPATH,'//*[@id="page-content"]/div/div[1]/div[2]/ul/li[1]/div/a/div/div[2]/h3').click() # 기독교개론
# driver.find_element(By.XPATH,'//*[@id="page-content"]/div/div[1]/div[2]/ul/li[4]/div/a/div/div[2]/h3').click() # 데이터베이스
# driver.find_element(By.XPATH,'//*[@id="page-content"]/div/div[1]/div[2]/ul/li[6]/div/a/div/div[2]/h3').click() # 운영체제
# driver.find_element(By.XPATH,'//*[@id="page-content"]/div/div[1]/div[2]/ul/li[7]/div/a/div/div[2]/h3').click() # 데이터구조응용

# 강의 선택
number = 22844
# driver.find_element(By.ID,'section-13').click()
driver.find_element(By.XPATH,f'//*[@id="module-{number}"]/div/div/div[1]/div/a/span').click()
# driver.find_element(By.XPATH,f'//*[@id="module-{number}"]/div/div/div[2]/div/a/span').click()

# 화면 전환
window_handles = driver.window_handles
driver.switch_to.window(window_handles[1])
time.sleep(3)

# 강의 재생
try:
    time.sleep(2)
    
    # 알림 창으로 전환
    alert = driver.switch_to.alert
    print(f"Alert 내용: {alert.text}") 
    
    # 확인 클릭
    alert.accept()
    print("Alert 확인 완료!")

except NoAlertPresentException:
    print("Alert이 없습니다.")
    # alert 안뜨면 영상 재생
    video_poster = driver.find_element(By.CLASS_NAME, 'vjs-poster')
    driver.execute_script("arguments[0].click();", video_poster)

try:
    # JavaScript 실행: 비디오의 전체 길이 가져오기
    video_duration = driver.execute_script("return document.querySelector('video').duration;")
    print(f"강의 길이: {video_duration}초")

    # 강의 시간이 존재하면 기다림
    if video_duration and video_duration > 0:
        print("강의 재생 중...")
        time.sleep(video_duration + 5)  # 재생 시간이 지나고 +5초 여유
        print("강의 종료 완료!")

except:
    print("비디오 길이 확인 실패!")


input('enter')
driver.quit()