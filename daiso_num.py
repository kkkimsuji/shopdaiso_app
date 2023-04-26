# 구글 맵을 통해 다이소 매장 수 구하기
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

# 다이소 지역별 매장
k_city = []
# 다이소 서울
k_city.append('https://www.google.com/search?q=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EC%84%9C%EC%9A%B8&biw=1280&bih=556&tbm=lcl&ei=aXgvZIiCCPjN2roP04mdiAs&ved=0ahUKEwjI2si41Zb-AhX4plYBHdNEB7EQ4dUDCAk&uact=5&oq=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EC%84%9C%EC%9A%B8&gs_lcp=Cg1nd3Mtd2l6LWxvY2FsEAMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoGCAAQHhAPOggIABAHEB4QDzoHCAAQigUQQ1DRBljbHWCuH2gBcAB4AIABcIgBoweSAQMxLjiYAQCgAQHAAQE&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[37.6804996,127.0869974],[37.485461199999996,126.91260969999999]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:4')
# 다이소 경기
k_city.append('https://www.google.com/search?q=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EA%B2%BD%EA%B8%B0&biw=1280&bih=556&tbm=lcl&ei=engvZNzTBqu22roPxey1-Aw&ved=0ahUKEwjc-NTA1Zb-AhUrm1YBHUV2Dc8Q4dUDCAk&uact=5&oq=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EA%B2%BD%EA%B8%B0&gs_lcp=Cg1nd3Mtd2l6LWxvY2FsEAMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgQIABAeMgQIABAeMgQIABAeMgYIABAeEA8yBggAEB4QDzIGCAAQHhAPOgcIABCKBRBDOggIABCABBCxA1DZBVjvD2DQEWgAcAB4AIABdogBzQaSAQMyLjaYAQCgAQHAAQE&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[37.8214119,127.363368],[37.3230888,126.96981659999999]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:4')
# 다이소 인천
k_city.append('https://www.google.com/search?q=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EC%9D%B8%EC%B2%9C&biw=1280&bih=556&tbm=lcl&ei=3HgvZKdh8KDV7w_TlpWgBg&ved=0ahUKEwinv6zv1Zb-AhVwUPUHHVNLBWQQ4dUDCAk&oq=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EC%9D%B8%EC%B2%9C&gs_lcp=Cg1nd3Mtd2l6LWxvY2FsEAxQAFgAYABoAHAAeACAAQCIAQCSAQCYAQA&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[37.625756599999995,126.75722539999998],[37.383219499999996,126.6383635]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:4')
# 다이소 강원
k_city.append('https://www.google.com/search?q=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EA%B0%95%EC%9B%90&biw=1280&bih=556&tbm=lcl&ei=-XgvZNCFItuSoASm-7qgAw&ved=0ahUKEwiQ5rf91Zb-AhVbCYgKHaa9DjQQ4dUDCAk&uact=5&oq=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EA%B0%95%EC%9B%90&gs_lcp=Cg1nd3Mtd2l6LWxvY2FsEAMyBggAEB4QDzIGCAAQHhAPMgQIABAeMggIABAIEB4QDzIKCAAQCBAeEA8QCjIGCAAQCBAeMggIABAIEB4QDzIICAAQCBAeEA86BQgAEIAEOgcIABCKBRBDOggIABCABBCxA1COBViTEGCwEWgAcAB4AIABjwGIAfsIkgEEMC4xMJgBAKABAcABAQ&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[38.2661573,129.1996962],[37.1118771,127.6372863]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:4')
# 다이소 광주광역시
k_city.append('https://www.google.com/search?tbs=lf:1,lf_ui:4&tbm=lcl&q=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EA%B4%91%EC%A3%BC%EA%B4%91%EC%97%AD%EC%8B%9C&rflfq=1&num=10&sa=X&ved=2ahUKEwj5i9uw_Jb-AhVNhlYBHcSUCpEQjGp6BAgREAE&biw=1280&bih=556&dpr=1.5#rlfi=hd:;si:;mv:[[35.2253827,126.93236329999999],[35.092006,126.7601908]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:4')
# 다이소 대전
k_city.append('https://www.google.com/search?q=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EB%8C%80%EC%A0%84&biw=1280&bih=556&tbm=lcl&ei=o3kvZL29BaKi2roP4K6GiAc&ved=0ahUKEwj9mqPO1pb-AhUikVYBHWCXAXEQ4dUDCAk&uact=5&oq=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EB%8C%80%EC%A0%84&gs_lcp=Cg1nd3Mtd2l6LWxvY2FsEAMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgYIABAeEA8yBggAEB4QDzIECAAQHjoHCAAQigUQQzoICAAQgAQQsQNQjwVY9AxggQ5oAXAAeAGAAZMBiAHzBpIBAzIuNpgBAKABAcABAQ&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[36.4050283,127.44638309999998],[36.2920748,127.3119335]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:4')
# 다이소 울산
k_city.append('https://www.google.com/search?q=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EC%9A%B8%EC%82%B0&biw=1280&bih=556&tbm=lcl&ei=unkvZIHRL7O22roPkKKV-AM&ved=0ahUKEwiBlsnZ1pb-AhUzm1YBHRBRBT8Q4dUDCAk&uact=5&oq=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EC%9A%B8%EC%82%B0&gs_lcp=Cg1nd3Mtd2l6LWxvY2FsEAMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgQIABAeMgQIABAeMgQIABAeMgYIABAeEA8yBAgAEB4yBAgAEB46BwgAEIoFEEM6CAgAEIAEELEDUI4FWJkOYL0PaAFwAHgBgAGjAYgBjwiSAQMyLjeYAQCgAQHAAQE&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[35.6500768,129.4520915],[35.4243363,129.0940346]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:4')
# 다이소 세종
k_city.append('https://www.google.com/search?q=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EC%84%B8%EC%A2%85&biw=1280&bih=556&tbm=lcl&ei=xnkvZNbdA9nJ2roPh46Y0A0&ved=0ahUKEwjW2Pne1pb-AhXZpFYBHQcHBtoQ4dUDCAk&uact=5&oq=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EC%84%B8%EC%A2%85&gs_lcp=Cg1nd3Mtd2l6LWxvY2FsEAMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgQIABAeMgQIABAeMgYIABAeEA8yBggAEAgQHjIGCAAQCBAeMgYIABAIEB46BwgAEIoFEEM6CAgAEIAEELEDUPsEWNEKYOMLaAFwAHgAgAFxiAGfBpIBAzQuNJgBAKABAcABAQ&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[36.6086945,127.37323029999999],[36.465728,127.2335769]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:4')
# 다이소 충북
k_city.append('https://www.google.com/search?q=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EC%B6%A9%EB%B6%81&biw=1280&bih=556&tbm=lcl&ei=B3ovZMbZJvvh2roPuqiQyA8&ved=0ahUKEwiG-Zv-1pb-AhX7sFYBHToUBPkQ4dUDCAk&uact=5&oq=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EC%B6%A9%EB%B6%81&gs_lcp=Cg1nd3Mtd2l6LWxvY2FsEAMyBggAEAgQHjIGCAAQCBAeMggIABAIEB4QDzIICAAQCBAeEA86BQgAEIAEOgQIABAeOgYIABAeEA86BwgAEIoFEEM6CAgAEIAEELEDUNoEWKINYJwOaABwAHgAgAGCAYgBwQeSAQMzLjaYAQCgAQHAAQE&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[37.1706826,128.4321137],[36.1193989,127.26410550000001]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:4')
# 다이소 충남
k_city.append('https://www.google.com/search?q=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EC%B6%A9%EB%82%A8&biw=1280&bih=556&tbm=lcl&ei=EXovZLC0OPnc2roP1pyUgAc&ved=0ahUKEwjwgJCD15b-AhV5rlYBHVYOBXAQ4dUDCAk&uact=5&oq=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EC%B6%A9%EB%82%A8&gs_lcp=Cg1nd3Mtd2l6LWxvY2FsEAMyBggAEAgQHjIGCAAQCBAeMgYIABAIEB4yCAgAEAgQHhAPMggIABAIEB4QDzoFCAAQgAQ6BQghEKABUOwEWN8HYNMIaABwAHgAgAF8iAGEBJIBAzIuM5gBAKABAcABAQ&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[36.9709716,127.23223990000001],[36.082522399999995,126.5696088]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:4')
# 다이소 전북
k_city.append('https://www.google.com/search?q=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EC%A0%84%EB%B6%81&biw=1280&bih=556&tbm=lcl&ei=KHovZLf-GJvi2roPzcmtgAk&ved=0ahUKEwi3suyN15b-AhUbsVYBHc1kC5AQ4dUDCAk&uact=5&oq=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EC%A0%84%EB%B6%81&gs_lcp=Cg1nd3Mtd2l6LWxvY2FsEAMyBggAEB4QDTIGCAAQHhANMggIABAeEA0QDzIKCAAQCBAeEA0QDzIKCAAQCBAeEA0QDzIKCAAQCBAeEA0QDzIICAAQCBAeEA0yCggAEAgQHhANEA8yCggAEAgQHhANEA86BQgAEIAEOggIABCABBCxA1DlCVj5EmCHFGgAcAB4AIABiQGIAaAIkgEDNS41mAEAoAEBwAEB&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[36.0091991,127.1888944],[35.546903,126.6895883]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:4')
# 다이소 전남
k_city.append('https://www.google.com/search?q=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EC%A0%84%EB%82%A8&biw=1280&bih=556&tbm=lcl&ei=LHovZNamAfGk2roPwf-i2AM&ved=0ahUKEwjW7MiP15b-AhVxklYBHcG_CDsQ4dUDCAk&uact=5&oq=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EC%A0%84%EB%82%A8&gs_lcp=Cg1nd3Mtd2l6LWxvY2FsEAMyBQgAEIAEMgYIABAeEA8yBggAEAgQHjoGCAAQHhANOggIABAeEA0QDzoKCAAQCBAeEA0QDzoICAAQCBAeEA1Q3QRY-wdgiAloAHAAeACAAWuIAfIDkgEDMi4zmAEAoAEBwAEB&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[35.3663433,127.79348829999998],[34.4291795,126.17909680000001]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:4')
# 다이소 경북
k_city.append('https://www.google.com/search?q=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EA%B2%BD%EB%B6%81&biw=1280&bih=556&tbm=lcl&ei=NnovZPjqI__L2roPqIyE4A8&ved=0ahUKEwj43c2U15b-AhX_pVYBHSgGAfwQ4dUDCAk&uact=5&oq=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EA%B2%BD%EB%B6%81&gs_lcp=Cg1nd3Mtd2l6LWxvY2FsEAMyBggAEAgQHjIGCAAQCBAeMgYIABAIEB4yCAgAEAgQHhAPMggIABAIEB4QDzIICAAQCBAeEA8yCAgAEAgQHhAPMggIABAIEB4QDzoFCAAQgAQ6BggAEB4QDzoICAAQgAQQsQNQ8wRYkAxghBJoAHAAeACAAXSIAZ8HkgEDMy42mAEAoAEBwAEB&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[37.0755978,129.4796629],[35.563476,128.0394938]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:4')
# 다이소 경남
k_city.append('https://www.google.com/search?q=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EA%B2%BD%EB%82%A8&biw=1280&bih=556&tbm=lcl&ei=QHovZMmzN9SO2roPjIic0AI&ved=0ahUKEwjJ08OZ15b-AhVUh1YBHQwEByoQ4dUDCAk&uact=5&oq=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EA%B2%BD%EB%82%A8&gs_lcp=Cg1nd3Mtd2l6LWxvY2FsEAMyCAgAEB4QDRAPMgoIABAIEB4QDRAPMgoIABAIEB4QDRAPMgoIABAIEB4QDRAPMgoIABAIEB4QDRAPMgoIABAIEB4QDRAPOgYIABAIEB46CAgAEAgQHhAPOgUIABCABDoHCAAQDRCABDoGCAAQHhANOggIABAIEB4QDVCqBVitCGC3CWgAcAB4AIABZ4gB8QOSAQMyLjOYAQCgAQHAAQE&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[35.5309046,129.2565794],[34.798316299999996,127.8173059]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:4')
# 다이소 대구
k_city.append('https://www.google.com/search?q=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EB%8C%80%EA%B5%AC&biw=1280&bih=556&tbm=lcl&ei=SnovZJelGIuD2roPsfaD0Ac&ved=0ahUKEwiX8oae15b-AhWLgVYBHTH7AHoQ4dUDCAk&uact=5&oq=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EB%8C%80%EA%B5%AC&gs_lcp=Cg1nd3Mtd2l6LWxvY2FsEAMyBQgAEIAEMgUIABCABDIFCAAQgAQyBAgAEB4yBggAEB4QDzIECAAQHjIGCAAQHhAPMgQIABAeMgYIABAeEA8yBggAEB4QDzoICAAQHhANEA86CggAEAgQHhANEA86CAgAEIAEELEDUL8EWNsKYPoLaAFwAHgBgAF6iAHFBZIBAzQuM5gBAKABAcABAQ&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[35.9388533,128.7271629],[35.800460699999995,128.4818462]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:4')
# 다이소 부산
k_city.append('https://www.google.com/search?q=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EB%B6%80%EC%82%B0&biw=1280&bih=556&tbm=lcl&ei=VHovZMjjPICo2roP-vyT-A8&ved=0ahUKEwjI3Y2j15b-AhUAlFYBHXr-BP8Q4dUDCAk&uact=5&oq=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EB%B6%80%EC%82%B0&gs_lcp=Cg1nd3Mtd2l6LWxvY2FsEAMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgQIABAeOgYIABAeEA86BwgAEIoFEEM6CAgAEIAEELEDUNUEWLgKYMcLaAFwAHgAgAFyiAGQBpIBAzYuMpgBAKABAcABAQ&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[35.2159513,129.1847784],[35.0918181,128.9957902]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:4')
# 다이소 제주
k_city.append('https://www.google.com/search?q=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EC%A0%9C%EC%A3%BC&biw=1280&bih=556&tbm=lcl&ei=X3ovZIauLZru2roP1eeRiAQ&ved=0ahUKEwjG2Z2o15b-AhUat1YBHdVzBEEQ4dUDCAk&uact=5&oq=%EB%8B%A4%EC%9D%B4%EC%86%8C+%EC%A0%9C%EC%A3%BC&gs_lcp=Cg1nd3Mtd2l6LWxvY2FsEAMyBQgAEIAEMgUIABCABDIECAAQHjIECAAQHjIECAAQHjIGCAAQHhAPMgQIABAeMgYIABAeEA8yBAgAEB4yBggAEB4QDzoHCAAQigUQQzoICAAQgAQQsQNQ1ARYrAlg9ApoAXAAeAGAAZsBiAGrBpIBAzMuNJgBAKABAcABAQ&sclient=gws-wiz-local#rlfi=hd:;si:;mv:[[33.5402653,126.95493390000001],[33.2036619,126.21453349999999]];tbs:lrf:!1m4!1u3!2m2!3m1!1e1!2m1!1e3!3sIAE,lf:1,lf_ui:4')
#cities = ['서울','경기','인천','강원','광주','대전','울산','세종','충북','충남','전북','전남','경북','경남','대구',
#               '부산','제주']
daiso_store = []
# 주소 가져 오기
for st in k_city: # 탭하기
    driver.get(st)
    time.sleep(2)

    # 다이소 매장 정보 페이지 클릭
    driver.find_element(By.XPATH,'//*[@id="rl_ist0"]/div/div[1]/div[3]').click()

    time.sleep(1)
    i = 0

    for i in range(10):
        try:
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            time.sleep(1)
            j = i+3
            html = driver.page_source
            bs = BeautifulSoup(html,'html.parser')
            #page_num = driver.find_element(By.CLASS_NAME, 'fl')     # a / aria-label="Page 9" / class="fl"
            strdata = f'//*[@id="rl_ist0"]/div/div[2]/div/table/tbody/tr/td[{j}]/a'
            print (strdata)
            page_num = driver.find_element(By.XPATH,strdata )
            page_num.click()
            time.sleep(2)
            stores = bs.find_all('a', class_='vwVdIc')# 매장 정보
        except:
            break
        i += 1
        for temp_store in stores:
            dictdata = {}
            sdata = temp_store.find_all('div')
            cnt = 0
            for temp_s in sdata[2:4]:
                if cnt == 0:
                    dictdata['매장명'] = temp_s.text
                    cnt = 1
                else :
                    dictdata['주소'] = temp_s.text
                print(temp_s.text)
            daiso_store.append(dictdata)
            print('-------------------------------')
    print(daiso_store)

df = pd.DataFrame(daiso_store)
df.to_csv('다이소_전국_매장.csv')
