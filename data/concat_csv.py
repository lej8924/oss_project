from os import read

from pandas.core.reshape.concat import concat
import fnmatch as fn
import pandas as pd
#data1 = readcsv.readdata('no1.csv')
data1 = pd.read_csv('no1.csv')
data1 = data1.drop('Unnamed: 0',axis=1)


df = data1['Typename']

china = ['중화요리','양꼬치','중식'] #1
japan = ['초밥,롤', '일식집', '일본식주점', '일식', '퓨전일식', '일본식라면'] #2
west = ['패스트푸드', '패밀리레스토랑', '양식', '뷔페', '피자', '와인바', '햄버거', '샌드위치', '스테이크,립', '이탈리안' ]#3
cafe = ['커피전문점', '카페', '디저트카페', '테마카페', '북카페', '키즈카페', '제과,베이커리', '도넛']#4
other = ['호프,요리주점', '베트남음식', '동남아음식', '태국음식', '인도음식' ,'술집' ,'아시아음식']#5

classify = []
for i, type in enumerate(df):
    if type in china:
        classify.append(1)
    elif type in japan:
        classify.append(2)
    elif type in west:
        classify.append(3)
    elif type in cafe:
        classify.append(4)
    elif type in other:
        classify.append(5)
    else:
        classify.append(0)

classify = pd.DataFrame(classify)
classify.columns=['Typenum']  
     
df_list = pd.concat([data1,classify],axis=1)
df_list.to_csv('nowon.csv')




