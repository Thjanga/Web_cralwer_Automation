from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import os, time

load_dotenv()

# 강의 재생 함수
def play_video():
    global driver, main_window

    # 새 창으로 전환
    window_handles = driver.window_handles
    for handle in window_handles:
        if handle != main_window:
            driver.switch_to.window(handle)
            break

    time.sleep(4)

    # 위치 클릭으로 바꾸기 
    try:
        alert = driver.switch_to.alert # 이어보기
        alert.accept()
        print("이어보기 alert 처리")
    except NoAlertPresentException:
        try:
            video_poster = driver.find_element(By.CLASS_NAME, 'vjs-big-play-button')
            print(video_poster.text)
            driver.execute_script("""
        const video = document.querySelector('video');
        if (video) {
            video.muted = true;  // 자동재생 정책 우회
            video.play();
            console.log("비디오 재생 시도");
        }
    """) 
            time.sleep(2)
            actions = ActionChains(driver)
            actions.send_keys('D').perform()

            # 영상 재생
            print("영상 재생 시작")
        except Exception as e:
            print(f"재생 실패: {e}")
            return

    # 영상 끝날 때까지 대기
    while True:
        try:
            is_ended = driver.execute_script("""
                const video = document.querySelector('video');
                if (!video) return false;
                return video.ended || video.currentTime >= video.duration;
            """)
            if is_ended:
                print("강의 종료")
                time.sleep(2)
                try:
                    driver.close()
                    print("강의 탭 닫기 완료")

                    try:
                        alert = driver.switch_to.alert
                        alert.accept()
                        print("닫기 alert 처리")
                    except NoAlertPresentException:
                        pass

                except Exception as e:
                    print(f"탭 닫기 실패: {e}")

                driver.switch_to.window(main_window)
                print("수업 목록 탭 복귀")
                break
            else:
                print("강의 진행 중...")
        except Exception as e:
            print(f"확인 중 에러 발생: {e}")
            break
        time.sleep(5)


# 메인
option = Options()
option.add_argument(r'user-data-dir=C:\Users\kspqi\AppData\Local\Google\Chrome\User Data')
driver = webdriver.Chrome(options=option)
driver.get('https://cyber.anyang.ac.kr/')
time.sleep(3)

# 로그인
driver.find_element(By.NAME, 'username').send_keys(os.getenv('universityid'))
driver.find_element(By.NAME, 'password').send_keys(os.getenv('universitypw'))
driver.find_element(By.CLASS_NAME, 'main_login_btn').click()
time.sleep(2)

# 공지 닫기
try:
    driver.find_element(By.CLASS_NAME, 'close_notice').click()
except:
    pass

과목_리스트 = [3020,3906,3909,3912]  # 수업 번호 3020,3906,3909,3912

for 과목번호 in 과목_리스트:
    try:
        # 과목 선택
        driver.get(f'https://cyber.anyang.ac.kr/course/view.php?id={과목번호}')
        time.sleep(2)

        main_window = driver.current_window_handle

        # 주차 클릭
        week = 11
        driver.find_element(By.XPATH, f"//a[text()='{week}주차']").click()

        # 주차 로딩 대기
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f"li.section.main.week-{week}"))
        )

        # 섹션 탐색
        week_sections = driver.find_elements(By.CSS_SELECTOR, f'li.section.main.week-{week}')

        for section in week_sections:
            video_items = section.find_elements(By.CSS_SELECTOR, 'li.activity.vod.modtype_vod span.instancename')

            for el in video_items:
                try:
                    # <span class='accesshide'> 제거 -> 강의 영상이 추가됨
                    driver.execute_script("""
                        let spans = arguments[0].querySelectorAll('span.accesshide');
                        spans.forEach(s => s.remove());
                    """, el)
                except:
                    pass

                title = el.text.strip()
                print(f"강의 제목: {title}")

                try:
                    # 강의 클릭
                    driver.execute_script("arguments[0].click();", el)
                    time.sleep(2)
                    play_video()
                except Exception as e:
                    print(f"강의 클릭 실패: {e}")
                    continue

        # 과목 목록으로 복귀
        driver.back()
        time.sleep(2)

    except Exception as e:
        print(f"\n과목 {과목번호} 처리 중 오류 발생: {e}")
        continue

input('\n모든 과목 강의 수강 완료')
driver.quit()
