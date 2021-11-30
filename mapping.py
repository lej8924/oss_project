import googlemaps
import pandas as pd
import glob

#csv 파일 합치기
filenames = glob.glob('/Users/yu/Desktop/oss_project-master/*.csv')

df_list = []
for filename in filenames:
    df_list.append(pd.read_csv(filename,index_col=None, header=0))
df_list = pd.concat(df_list, axis=0, ignore_index=True)

#gmaps 인증
gmaps_key = "AIzaSyBWwCkmpNU-s28QzFyunENlPjgUcCxpekI"
gmaps  = googlemaps.Client(key=gmaps_key)

#위도,경도 리스트 정의 및 범위지정
place_lat = []
place_lng = []

max_lat = 38.0
min_lat = 33.0
max_lng = 132.0
min_lng = 126.0

#위도 경도 불러오기
i=0
for place in df_list["Addr"]:
    try:
        print(i)
        i+=1
        tmp_loc = gmaps.geocode(place)[0].get('geometry')
        tmp_lat = tmp_loc["location"]["lat"]
        tmp_lng = tmp_loc["location"]["lng"]
        
        if(tmp_lat>max_lat or tmp_lat<min_lat or tmp_lng>max_lng or tmp_lng<min_lng):
            place_lat.append("0")
            place_lng.append("0")
        
        else:
            place_lat.append(tmp_lat)
            place_lng.append(tmp_lng)
  
    except:
        place_lat.append("0")
        place_lng.append("0")
        print("error")
        print(place)
        
print("위경도 추가 완료")

#최종파일에 위도경도 추가
df_list2 = pd.DataFrame(place_lat)
df_list2 = df_list2.rename(columns={0:"lat"})
df_list3 = pd.DataFrame(place_lng)
df_list3 = df_list3.rename(columns={0:"lng"})

df = pd.concat([df_list,df_list2,df_list3], axis=1)

#csv파일로 출력
df = df.query("lat != '0'")
df.to_csv('/Users/yu/Desktop/oss_project-master/no1won_data_'+"location.csv",encoding="utf-8-sig")
df.tail()
