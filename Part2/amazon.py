import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time

# 미완성
options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36")

driver = webdriver.Chrome(options = options)
driver.get('https://www.amazon.com/s?k=monitor&crid=FHLEDQSAFSSE&sprefix=monitor%2Caps%2C336&ref=nb_sb_noss_1')

time.sleep(3)

soup = BeautifulSoup(driver.page_source,'html.parser')
titles = soup.select('.a-size-medium')

for t in titles:
    print(t.text)

driver.quit()


# 정적 크롤링 안됨
# h = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}

# c = {
#     'aws-target-data':'%7B%22support%22%3A%221%22%7D',
#     'regStatus':'pre-register', 'AMCV_7742037254C95E840A4C98A6%40AdobeOrg':'1585540135%7CMCIDTS%7C20173%7CMCMID%7C80710856042195013811218291271397939666%7CMCAAMLH-1743486681%7C11%7CMCAAMB-1743486681%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1742889082s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0', 'aws-target-visitor-id':'1742881881652-476205.42_0', 'session-id':'143-2554764-5335301', 'session-id-time':'2082787201l', 'i18n-prefs':'USD', 'sp-cdn':'L5Z9:KR', 'skin':'noskin', 'ubid-main':'133-6996033-656663', 'session-token':'5QW5g/dSDUD050OC9B2qmfwaB+KEJ3rW0vJ4V5fQZio4+sRhMakKzubjyQC9jNRbNL3S1Kl1xOoEC0Yo+gf9EsQihZy3kA0JMCT2GXrqWf3ymweDg9Dxe9DIU9K0Pa4uQm3QbYGG4v0CNHXODheuWAb8Z3miO4l4qRLGUOn2hC8LB5varq0MAFxLHGXIKsSTd9TVP3XoctflB+mc9EgQ7zNZOZNEHhjO4rEc7QstDiI9J5TAXLuFELRH9vb47rVCjvlnGqZlF+cYJ2plYi26OWo7GmFgtX5epSQMYSTTSCCypSQXYt73+gQeoAWlx1FkeMDcOHHMys6KScHbhQFIA1yhW549gip+',
# }

# r = requests.get('https://www.amazon.com/s?k=monitor&crid=FHLEDQSAFSSE&sprefix=monitor%2Caps%2C336&ref=nb_sb_noss_1',headers = h,cookies=c)

# soup = BeautifulSoup(r.content,'lxml')
# print(soup.select('.a-size-medium')[0])
# soup = BeautifulSoup(r.content,'html')
# print(soup)

# print(r.status_code)
# print(r.content)


