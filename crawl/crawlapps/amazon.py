from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request
import urllib
import time
import sys
import re
import math
import numpy
import pandas as pd
import xlwt
import random
import os
import shutil
import requests
from datetime import timedelta, timezone, datetime

def crawlproduct(sec, cnt):

    query_url='https://www.amazon.com/bestsellers?ld=NSGoogle'

    now = time.localtime()
    scrape_time = '%04d-%02d-%02d-%02d-%02d-%02d' % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    os.mkdir('media'+'/'+scrape_time)

    if sec == '1' :
          sec_name='Amazon Devices and Accessories'
    elif sec =='2' :
          sec_name='Amazon Launchpad'
    elif sec =='3' :
          sec_name='Appliances'
    elif sec =='4' :
          sec_name='Apps and Games'
    elif sec =='5' :
          sec_name='Arts and Crafts and Sewing'
    elif sec =='6' :
          sec_name='Audible Books and Originals'
    elif sec =='7' :
          sec_name='Automotive'
    elif sec =='8' :
          sec_name='Baby'
    elif sec =='9' :
          sec_name='Beauty and Personal Care'
    elif sec =='10' :
          sec_name='Books'
    elif sec =='11' :
          sec_name='CDs and Vinyl'
    elif sec =='12' :
          sec_name='Camera and Photo'
    elif sec =='13' :
          sec_name='Cell Phones and Accessories'
    elif sec =='14' :
          sec_name='Clothing and Shoes and Jewelry'
    elif sec =='15' :
          sec_name='Collectible Currencies'
    elif sec =='16' :
          sec_name='Computers and Accessories'
    elif sec =='17' :
          sec_name='Digital Music'
    elif sec =='18' :
          sec_name='Electronics'
    elif sec =='19' :
          sec_name='Entertainment Collectibles'
    elif sec =='20' :
          sec_name='Gift Cards'
    elif sec =='21' :
          sec_name='Grocery and Gourmet Food'
    elif sec =='22' :
          sec_name='Handmade Products'
    elif sec =='23' :
          sec_name='Health and Household'
    elif sec =='24' :
          sec_name='Home and Kitchen'
    elif sec =='25' :
          sec_name='Industrial and Scientific'
    elif sec =='26' :
          sec_name='Kindle Store'
    elif sec =='27' :
          sec_name='Kitchen and Dining'
    elif sec =='28' :
          sec_name='Magazine Subscriptions'
    elif sec =='29' :
          sec_name='Movies and TV'
    elif sec =='30' :
          sec_name='Musical Instruments'
    elif sec =='31' :
          sec_name='Office Products'
    elif sec =='32' :
          sec_name='Patio and Lawn and Garden'
    elif sec =='33' :
          sec_name='Pet Supplies'
    elif sec =='34' :
          sec_name='Prime Pantry'
    elif sec =='35' :
          sec_name='Smart Home'
    elif sec =='36' :
          sec_name='Software'
    elif sec =='37' :
          sec_name='Sports and Outdoors'
    elif sec =='38' :
          sec_name='Sports Collectibles'
    elif sec =='39' :
          sec_name='Tools and Home Improvemen'
    elif sec =='40' :
          sec_name='Toys and Games'
    elif sec =='41' :
          sec_name='Video Games'

    if cnt > 30 :
          print("    요청 건수가 많아서 시간이 제법 소요되오니 잠시만 기다려 주세요~~")
    else :
          print("    요청하신 데이터를 수집하고 있으니 잠시만 기다려 주세요~~")

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('disable=gpu')

    driver = webdriver.Chrome(options=options)

    driver.get(query_url)
    time.sleep(5)

    # 분야별 더보기 버튼을 눌러 페이지를 엽니다
    if sec == '1' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[1]/a""").click( )
    elif sec == '2' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[2]/a""").click( )
    elif sec == '3' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[3]/a""").click( )
    elif sec == '4' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[4]/a""").click( )
    elif sec == '5' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[5]/a""").click( )
    elif sec == '6' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[6]/a""").click( )
    elif sec == '7' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[7]/a""").click( )
    elif sec == '8' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[8]/a""").click( )
    elif sec == '9' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[9]/a""").click( )
    elif sec == '10' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[10]/a""").click( )
    elif sec == '11' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[11]/a""").click( )
    elif sec == '12' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[12]/a""").click( )
    elif sec == '13' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[13]/a""").click( )
    elif sec == '14' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[14]/a""").click( )
    elif sec == '15' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[15]/a""").click( )
    elif sec == '16' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[16]/a""").click( )
    elif sec == '17' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[17]/a""").click( )
    elif sec == '18' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[18]/a""").click( )
    elif sec == '19' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[19]/a""").click( )
    elif sec == '20' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[20]/a""").click( )
    elif sec == '21' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[21]/a""").click( )
    elif sec == '22' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[22]/a""").click( )
    elif sec == '23' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[23]/a""").click( )
    elif sec == '24' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[24]/a""").click( )
    elif sec == '25' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[25]/a""").click( )
    elif sec == '26' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[26]/a""").click( )
    elif sec == '27' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[27]/a""").click( )
    elif sec == '28' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[28]/a""").click( )
    elif sec == '29' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[29]/a""").click( )
    elif sec == '30' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[30]/a""").click( )
    elif sec == '31' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[31]/a""").click( )
    elif sec == '32' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[32]/a""").click( )
    elif sec == '33' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[33]/a""").click( )
    elif sec == '34' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[34]/a""").click( )
    elif sec == '35' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[35]/a""").click( )
    elif sec == '36' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[36]/a""").click( )
    elif sec == '37' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[37]/a""").click( )
    elif sec == '38' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[38]/a""").click( )
    elif sec == '39' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[39]/a""").click( )
    elif sec == '40' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[40]/a""").click( )
    elif sec == '41' :
          driver.find_element_by_xpath("""//*[@id="zg_browseRoot"]/ul/li[41]/a""").click( )

    time.sleep(1)

    # 학습목표 2 : 해당 카테고리의 데이터를 수집합니다.
    #Step 4. 화면을 스크롤해서 아래로 이동한 후 요청된 데이터를 수집합니다.

    def scroll_down(driver):

          driver.execute_script("window.scrollBy(0,9300);")
          time.sleep(1)

    scroll_down(driver)

    bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    reple_result = soup.select('#zg-center-div > #zg-ordered-list')
    slist = reple_result[0].find_all('li')

    session = requests.Session()

    if cnt < 51 :

        ranking2=[]
        title3=[]
        price2=[]
        score2=[]
        sat_count2=[]
        store2=[]
        image2=[]

        count = 0

        for li in slist:


            # 판매순위
            try :
                ranking = li.find('span',class_='zg-badge-text').get_text().replace("#","")
            except AttributeError :
                ranking = ""



            #제품 설명
            try :
                title1 = li.find('div',class_='p13n-sc-truncated').get_text().replace("\n","")
            except AttributeError :
                title1 = ''
            else :
                title2=title1.translate(bmp_map).replace("\n","")

                count += 1

            # 가격
            try :
                price = li.find('span','p13n-sc-price').get_text().replace("\n","")
            except AttributeError :
                price = ''



            # 상품평
            try :
                sat_count = li.find('a','a-size-small a-link-normal').get_text().replace(",","")
            except (IndexError , AttributeError) :
                sat_count='0'


            #상품 별점 구하기
            try :
                score = li.find('span','a-icon-alt').get_text()
            except AttributeError :
                score=' '

            time.sleep(0.3)

            ranking2.append(ranking)
            title3.append(title2.replace("\n",""))
            price2.append(price.replace("\n",""))

            try :
                sat_count2.append(sat_count)
            except IndexError :
                sat_count2.append(0)

            score2.append(score)

            #상품이미지 다운로드
            media = '/Users/dukuaris/VENV/Django/media/{}'.format(scrape_time)
            try:
                image_source = li.find('div','a-section a-spacing-small').find('img')['src']
                local_filename = str(count) + ".jpg"
                r = session.get(image_source, stream=True, verify=False)
                with open(local_filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        f.write(chunk)
                current_image_absolute_path = os.path.abspath(local_filename)
                shutil.move(current_image_absolute_path, media)

            except IndexError :
                noimage = 'https://cdn4.iconfinder.com/data/icons/basics-set-2/100/Question-512.png'
                local_filename = str(count) + ".jpg"
                r = session.get(image_source, stream=True, verify=False)
                with open(local_filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        f.write(chunk)
                current_image_absolute_path = os.path.abspath(local_filename)
                shutil.move(current_image_absolute_path, media)

            image2.append(scrape_time+'/'+local_filename)

            if count == cnt :
                break

    elif cnt >= 51 :

        count = 0

        ranking2=[]
        title3=[]
        price2=[]
        score2=[]
        sat_count2=[]
        store2=[]
        image2=[]

        for li in slist:

            # 판매순위
            try :
                ranking = li.find('span',class_='zg-badge-text').get_text().replace("#","")
            except AttributeError :
                ranking = ""


            #제품 설명
            try :
                title1 = li.find('div',class_='p13n-sc-truncated').get_text().replace("\n","")
            except AttributeError :
                title1 = ''
            else :
                title2=title1.translate(bmp_map).replace("\n","")

                count += 1


            # 가격
            try :
                price = li.find('span','p13n-sc-price').get_text().replace("\n","")
            except AttributeError :
                price = ''


            try :
                sat_count = li.find('a','a-size-small a-link-normal').get_text().replace(",","")
            except (IndexError , AttributeError) :
                sat_count='0'


            #상품 별점 구하기
            try :
                score = li.find('span','a-icon-alt').get_text()
            except AttributeError :
                score=' '

            time.sleep(0.3)

            ranking2.append(ranking)
            title3.append(title2.replace("\n",""))
            price2.append(price.replace("\n",""))

            try :
                sat_count2.append(sat_count)
            except IndexError :
                sat_count2.append(0)

            score2.append(score)

            #상품이미지 다운로드
            media = '/Users/dukuaris/VENV/Django/media/{}'.format(scrape_time)
            try:
                image_source = li.find('div','a-section a-spacing-small').find('img')['src']
                local_filename = str(count) + ".jpg"
                r = session.get(image_source, stream=True, verify=False)
                with open(local_filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        f.write(chunk)
                current_image_absolute_path = os.path.abspath(local_filename)
                shutil.move(current_image_absolute_path, media)

            except IndexError :
                noimage = 'https://cdn4.iconfinder.com/data/icons/basics-set-2/100/Question-512.png'
                local_filename = str(count) + ".jpg"
                r = session.get(image_source, stream=True, verify=False)
                with open(local_filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        f.write(chunk)
                current_image_absolute_path = os.path.abspath(local_filename)
                shutil.move(current_image_absolute_path, media)

            image2.append(scrape_time+'/'+local_filename)


        # 1 페이지 정보 추출 후 2 페이지로 넘어가기
        driver.find_element_by_xpath("""//*[@id="zg-center-div"]/div[2]/div/ul/li[3]/a""").click( )
        print("\n")
        print("요청하신 데이터의 수량이 많아 다음 페이지의 데이터를 추출 중이오니 잠시만 기다려 주세요~^^")
        print("\n")

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        reple_result = soup.select('#zg-center-div > #zg-ordered-list')
        slist = reple_result[0].find_all('li')

        for li in slist:

            # 판매순위
            try :
                ranking = li.find('span',class_='zg-badge-text').get_text().replace("#","")
            except AttributeError :
                ranking = ""


            #제품 설명
            try :
                title1 = li.find('div',class_='p13n-sc-truncated').get_text().replace("\n","")
            except AttributeError :
                title1 = ''
            else :
                title2=title1.translate(bmp_map).replace("\n","")

                count += 1


            # 가격
            try :
                price = li.find('span','p13n-sc-price').get_text().replace("\n","")
            except AttributeError :
                price = ''


            try :
                sat_count = li.find('a','a-size-small a-link-normal').get_text().replace(",","")
            except (IndexError , AttributeError) :
                sat_count='0'


            #상품 별점 구하기
            try :
                score = li.find('span','a-icon-alt').get_text()
            except AttributeError :
                score=' '


            time.sleep(0.3)

            ranking2.append(ranking)
            title3.append(title2.replace("\n",""))
            price2.append(price.replace("\n",""))

            try :
                sat_count2.append(sat_count)
            except IndexError :
                sat_count2.append(0)

            score2.append(score)

            #상품이미지 다운로드
            media = '/Users/dukuaris/VENV/Django/media/{}'.format(scrape_time)
            try:
                image_source = li.find('div','a-section a-spacing-small').find('img')['src']
                local_filename = str(count) + ".jpg"
                r = session.get(image_source, stream=True, verify=False)
                with open(local_filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        f.write(chunk)
                current_image_absolute_path = os.path.abspath(local_filename)
                shutil.move(current_image_absolute_path, media)

            except IndexError :
                noimage = 'https://cdn4.iconfinder.com/data/icons/basics-set-2/100/Question-512.png'
                local_filename = str(count) + ".jpg"
                r = session.get(image_source, stream=True, verify=False)
                with open(local_filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=1024):
                        f.write(chunk)
                current_image_absolute_path = os.path.abspath(local_filename)
                shutil.move(current_image_absolute_path, media)

            image2.append(scrape_time+'/'+local_filename)


            if count == cnt :
                break

    amazon_best_seller = pd.DataFrame()
    amazon_best_seller['rank']=ranking2
    amazon_best_seller['title']=pd.Series(title3)
    amazon_best_seller['price']=pd.Series(price2)
    amazon_best_seller['review']=pd.Series(sat_count2)
    amazon_best_seller['score']=pd.Series(score2)
    amazon_best_seller['image']=pd.Series(image2)

    driver.close()

    return amazon_best_seller  #.to_json(orient='records')
