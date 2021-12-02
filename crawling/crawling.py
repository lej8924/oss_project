import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import requests
import csv
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup

#구글 인증
headers = {"User-Agent":"Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/89.0.4389.114 Safari/537.36"}

list = []

url = "https://map.kakao.com/"

options = webdriver.ChromeOptions()
options.add_argument('lang=ko_KR')

chromedriver_path = "chromedriver.exe"

driver = webdriver.Chrome(executable_path='/Users/yu/Desktop/oss_project-master/crawling/chromedriver')   #os.path.join(os.getwd(),chromedriver_path),options=options
driver.get(url)

#검색할 키워드 및 저장할파일명 입력
searchloc = input("찾고싶은 음식=> ")
filename = input("파일이름(영어로 치기)=> ")

#검색창에 키워드 입력
search_area = driver.find_element_by_xpath('//*[@id="search.keyword.query"]')#검색창
search_area.send_keys(searchloc) #검색어 입력
driver.find_element_by_xpath('//*[@id="search.keyword.submit"]').send_keys(Keys.ENTER) # Enter로 실행
time.sleep(2) #로딩시간 2초대기

#장소 버튼 클릭
driver.find_element_by_xpath('//*[@id="info.main.options"]/li[2]/a').send_keys(Keys.ENTER)
time.sleep(1)

def storeNamePrint():
    time.sleep(0.2)
    
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    
    cafe_lists = soup.select('.placelist > .PlaceItem')
    count = 1
    for cafe in cafe_lists:
        temp = []
        cafe_name = cafe.select('.head_item > .tit_name > .link_name')[0].text
        star = cafe.select('.rating > .score > .num')[0].text
        star_num = cafe.select('.rating > .score > .numberofscore')[0].text
        review = cafe.select('.rating > .review')[0].text
        link = cafe.select('.contact > .moreview')[0]['href']
        addr = cafe.select('.addr')[0].text
        
        #review에서 수동으로 글자제거
        review = review[3:len(review)]        
        review = int(re.sub(",","",review))

        #star_num에서 수동으로 마지막 한 글자제거
        star_num_size = len(star_num)
        star_num = star_num[:star_num_size-1]        
        star_num = int(re.sub(",","",star_num))
        
        
        print(cafe_name,star,star_num,review,link,addr)
        
        temp.append(cafe_name)
        temp.append(star)
        temp.append(star_num)
        temp.append(review)
        temp.append(link)
        temp.append(addr)
        
        list.append(temp)
        
    f = open(filename + '.csv',"w",encoding="utf-8-sig",newline="")
    writercsv = csv.writer(f)
    header = ['Name','Score','Numberofscore','Review','Link','Addr']
    writercsv.writerow(header)
    
    for i in list:
        writercsv.writerow(i)
        
page = 1
page2 = 0

for i in range(0,10):
    
    try:
        page2+=1
        
        print("**",page,"**")
        
        driver.find_element_by_xpath(f'//*[@id="info.search.page.no{page2}"]').send_keys(Keys.ENTER)
        time.sleep(2)
        storeNamePrint()
        
        if(page2)%5==0:
            driver.find_element_by_xpath('//*[@id="info.search.page.next"]').send_keys(Keys.ENTER)
            time.sleep(2)
            
            page2 = 0
        page += 1
    except:
        break
    
print("**크롤링완료**")