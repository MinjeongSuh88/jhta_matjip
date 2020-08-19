import requests
import time
import pyautogui
import pyperclip
from bs4 import BeautifulSoup as bs
from pprint import pprint
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# naver_idx = []
# r_name = []
# r_category = []
# price = []
# image_url = []
# distance = []
# SCORE = []
# site_score = []
# REVIEW = []
# site_review = []
# main_menu = []
dict_list = []
cnt = 0
url_place = "https://store.naver.com/restaurants/detail?entry=pll&id="
# url = "https://store.naver.com/restaurants/list?entry=pll&filterId=r09110133&query=%EC%9D%B5%EC%84%A0%EB%8F%99%20%EB%A7%9B%EC%A7%91&sessionid=%2FQDp24r%2FMXU9PW%2Fnrrt2fZQk"
url1 = "https://store.naver.com/restaurants/list?page="
page = 1
url2 = "&query=%EC%9D%B5%EC%84%A0%EB%8F%99%EB%A7%9B%EC%A7%91"
url = url1 + str(page) + url2


for j in range(15):
    url = url1 + str(page) + url2

    browser = webdriver.Chrome("E:\dev\python_workspace\chromedriver.exe")
    browser.get(url)

    # 화면 최대화
    browser.maximize_window()

    time.sleep(1)

    if browser.find_element_by_css_selector("#container > div.placemap_area > div.list_wrapper > div > div.list_area > ul"):
        print("성공")
        pass
    else:
        print("20개 실패 건너뛰기")
        break
    elem = browser.find_element_by_css_selector("#container > div.placemap_area > div.list_wrapper > div > div.list_area > ul")
    # print(elem.text)
    li_list = elem.find_elements_by_css_selector('li')

    # 화면 종료
    # browser.close()


    for store in li_list:
        cnt += 1
        print(cnt,"번째 for문 실행중")

        url_id = store.find_element_by_css_selector('a').get_attribute('href')
        id_pos = url_id.find("id")
        query_pos = url_id.find("query")
        naver_idx = url_id[id_pos+3:query_pos-1]
        print(naver_idx)
        # 리스트에 각 식당의 네이버 id 입력
        
        

        image_url = url_place + naver_idx
        res = requests.get(image_url) # 나중에 여기는 i로 바꿔줘야함
        # res.raise_for_status()
        if res:
            print("성공")
            pass
        else:
            print("실패, 건너뛰기")
            break
        # pprint(res.text)
        # /t 이런것들 나오는 썡 코드

        soup = bs(res.text,'lxml')
        # pprint(soup)
        # /t 이런거 없애준 예쁜 코드

        r_name = soup.find("strong",attrs={"class","name"}).text
        pprint(r_name)
        

        r_category = soup.find("span",attrs={"class","category"}).text
        pprint(r_category)
        

        price2 = soup.find_all("em",attrs={"class","price"})
        # print(price2)
        for p in price2:
            price = p.get_text()
            # print("여기 확인중")
            if price.find(",") > 0:
                # print("성공")
                print(price)
                break
            else :
                # print("실패")
                price = 0
                continue
        # price = soup.find("em",attrs={"class","price"}).text
        # price_num = price.find(",")
        # price = int(price[:price_num]+"000")
        # pprint(price)
        

        dis = soup.find("div",attrs={"class","contact_area"}).text
        print(dis)
        dis_dobo = dis.find("도보")
        dis_bun  = dis.find("분")
        distance = dis[dis_dobo+3:dis_bun+1]
        print(distance)
        
        
        raing_area = soup.find("div",attrs={"class","raing_area"})
        if raing_area:
            score = raing_area.find("span",attrs={"class","score"})
            # print(score)
            site_score = score.find("em",).text
        else:
            site_score = 0
        print(site_score)
        

        reviews = soup.find("div",attrs={"class","info_inner"})
        reviews2 = reviews.find_all("a",attrs={"class","link"})
        site_review = 0
        for rev in reviews2:
            site_review += int(rev.text[7:])
        print(site_review)    
        

        menu = soup.find("div",attrs={"class","menu_area"})
        main_menu = menu.find("span",attrs={"class","name"}).text
        print(main_menu)
        
        dict_list.append({
            'naver_idx' : naver_idx,
            'r_name' : r_name,
            'r_category' : r_category,
            'price' : price,
            'image_url' : image_url,
            'distance' : distance,
            'site_score' : site_score,
            'site_review' : site_review, 
            'main_menu' : main_menu
        })
        print(cnt,"번째 dict 어펜드")

    page += 1

print(dict_list)