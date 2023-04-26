import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

# selenium 사용 코드 : 자동화
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# 창 최대화
driver.maximize_window()
# 주소 가져 오기
driver.get('https://www.youtube.com/results?search_query=%EB%8B%A4%EC%9D%B4%EC%86%8C')
time.sleep(2)

for temp in range(500):
    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(3)

html = driver.page_source
bs = BeautifulSoup(html,'html.parser')
titles = bs.find_all('a', id = 'video-title')

result = []
for temp in titles:
    title = temp.get('aria-label').split('조회수')[0]
    print(title)
    result.append(title)
#    dict_result = {}
#    dict_result['제목'] = temp.get('aria-label').split('조회수')[0]
#    dict_result['조회수'] = temp.get('aria-label').split('조회수')[1]
#    dict_result['링크'] = temp.get('href')
#    print(dict_result['링크'])

df = pd.DataFrame(result)
df.to_csv('다이소_유튜브_제목.csv')

