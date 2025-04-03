import time
import undetected_chromedriver as uc
import cloudscraper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# .env 사용하려고 할 때
from dotenv import load_dotenv
import os

# .env file load
load_dotenv()
# ✅ Cloudflare 우회 요청
scraper = cloudscraper.create_scraper()
response = scraper.get("https://tickets.interpark.com/")

if response.status_code != 200:
    print(f"⚠️ Cloudflare 우회 실패! 상태 코드: {response.status_code}")
    exit()

print("✅ Cloudflare 우회 성공! 쿠키 적용 중...")

# ✅ Chrome 실행 (탐지 우회 설정)
options = uc.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")  
options.add_argument("--user-data-dir=C:/Users/kspqi/AppData/Local/Google/Chrome/User Data")  
options.add_argument("--profile-directory=Default")  
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36")

driver = uc.Chrome(options=options)
wait = WebDriverWait(driver, 15)  # ✅ 대기 시간 15초로 증가

try:
    # ✅ Cloudflare 체크 페이지 우회
    driver.get("https://tickets.interpark.com/")
    time.sleep(5)  # ✅ Cloudflare가 로딩되는 시간 확보

    # ✅ 쿠키 적용 후 새로고침
    for cookie in response.cookies:
        driver.add_cookie({'name': cookie.name, 'value': cookie.value, 'domain': 'tickets.interpark.com'})
    driver.refresh()

    # ✅ 로그인 버튼이 있는지 확인 후 클릭
    login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'header_menu__720a4')))
    if login_button:
        login_button.click()
    else:
        print("⚠️ 로그인 버튼을 찾을 수 없습니다!")
        exit()

    # ✅ 아이디 입력
    username_input = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
    if username_input:
        username_input.send_keys(os.getenv('parkid'))
    else:
        print("⚠️ 아이디 입력창을 찾을 수 없습니다!")
        exit()

    # ✅ 비밀번호 입력
    password_input = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
    if password_input:
        password_input.send_keys(os.getenv('parkpw'))
    else:
        print("⚠️ 비밀번호 입력창을 찾을 수 없습니다!")
        exit()

    # ✅ 로그인 버튼 클릭
    login_submit = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'button_btnStyle__SEYzh')))
    if login_submit:
        login_submit.click()
    else:
        print("⚠️ 로그인 버튼을 찾을 수 없습니다!")
        
        exit()

    # ✅ 검색창 입력
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/header/div[2]/div[1]/div/div[3]/div/input')))
    if search_box:
        search_box.send_keys('LCK')
    else:
        print("⚠️ 검색창을 찾을 수 없습니다!")
        exit()

    # ✅ 검색 결과 클릭
    ticket_item = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'TicketItem_imageWrap__iVEOw')))
    if ticket_item:
        ticket_item.click()
    else:
        print("⚠️ 티켓 아이템을 찾을 수 없습니다!")
        exit()

except Exception as e:
    print(f"🚨 오류 발생: {e}")

input('Press Enter to exit...')
driver.quit()
