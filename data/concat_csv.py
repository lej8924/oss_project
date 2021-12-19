from os import read
from pandas.core.reshape.concat import concat
import pandas as pd

#파일 불러오고 첫째 열 제거
data1 = pd.read_csv('data/no1.csv')
data1 = data1.drop('Unnamed: 0',axis=1)

df = data1['Typename'] #data1의 Typename열 새로운 리스트에 저장

#구분하는 기준, 카카오맵 기준
china = ['중화요리','양꼬치','중식'] #1
japan = ['초밥,롤', '일식집', '일본식주점', '일식', '퓨전일식', '일본식라면'] #2
west = ['패스트푸드', '패밀리레스토랑', '양식', '뷔페', '피자', '와인바', '햄버거', '샌드위치', '스테이크,립', '이탈리안' ]#3
cafe = ['커피전문점', '카페', '디저트카페', '테마카페', '북카페', '키즈카페', '제과,베이커리', '도넛']#4
other = ['호프,요리주점', '베트남음식', '동남아음식', '태국음식', '인도음식' ,'술집' ,'아시아음식']#5
#나머지는 한식 = 0

category = [china,japan,west,cafe,other]

classify = []
for i, type in enumerate(df):
    count = 1
    for cate in category:
        if type in cate:
            classify.append(count)
            break
        count += 1

    if count == 6:
        classify.append(0)
classify = pd.DataFrame(classify)
classify.columns=['Typenum']  

#지역을 대문자 알파벳으로 추가
df2 = data1['Addr2']
locations = ['공릉','월계','상계','중계','하계']
locationclass = ['A','B','C','D','E']
dong = []
for addr in df2:
    for i,location in enumerate(locations):
        if addr[:2] == location:
            dong.append(locationclass[i])
            break

dong = pd.DataFrame(dong)
dong.columns=['Dong']  
     
df_list = pd.concat([data1,classify,dong],axis=1)
df_list.to_csv('nowon.csv')


