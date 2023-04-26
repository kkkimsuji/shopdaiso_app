from selenium import webdriver      # selenium 사용
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import pandas as pd
import time
from bs4 import BeautifulSoup

# selenium 사용 코드 - 자동 활성화
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_options)

# 창 최대화
driver.maximize_window()
# 접근할 주소 입력
driver.get('https://play.google.com/store/apps/details?id=co.kr.daisomall&hl=ko')
# 2초동안 기다림
time.sleep(2)

driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz[2]/div/div/div[1]/div[2]/div/div[1]/c-wiz[4]/section/header/div/div[2]/button/i').click()

popup = driver.find_element(By.CLASS_NAME, 'fysCi')
popup.click()

prev_count = 0 # 이전 댓글
new_count = 0 # 현재 댓글

while True:
    # 끝까지 스크롤 다운
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(1)

    new_count = len(driver.find_elements(By.CLASS_NAME, 'h3YV2d'))
    print(new_count)

    if new_count == prev_count or new_count > 1000:
        print("====break====")
        break
    else:
        prev_count = new_count

reviews = driver.find_elements(By.CLASS_NAME, 'h3YV2d')
review_list = []
for temp in reviews:
    print(temp.text)
    review_list.append(temp.text)

# review_list 를 판다스로 가져와서 CSV파일로 저장하기
df = pd.DataFrame(review_list)
df.to_csv('다이소몰_구글앱_리뷰.csv')
