#이게 무슨 일이지 왜 git이 안 되지?
import googlemaps
import pandas as pd
df_list = pd.read_csv(filename+'.csv',encoding='utf-8')

gmaps_key = "AlzaSyBb-qcA00eiqk_9JZZkcQUhVcgG_5Xw"
gmaps  = googlemaps.Client(key=gmaps_key)

place_lat = []
place_lng = []

max_lat = 38.0
min_lat = 33.0
max_lng = 132.0
min_lng = 126.0

for place in df_list["Addr"]:
    if tmp:
        tmp_loc = tmp[0].get("geometry")
        tmp_lat = tmp_loc["location"]["lat"]
        tmp_lng = tmp_loc["location"]["lng"]
        
        if(tmp_lat>max_lat or tmp_lat<min_lat or tmp_lng>max_lng or tmp_lnng<min_lng):
            place_lat.append("0")
            place_lng.append("0")
        
        else:
            place_lat.append(tmp_lat)
            place_lng.append(tmp_lng)   
    else:
        place_lat.append("0")
        place_lng.append("0")
        
print("위경도 추가 완료")

df_list2 = pd.DataFrame(place_lat)
df_list2 = df_list2.rename(columns={0:"lat"})
df_list3 = pd.DataFrame(place_lng)
df_list3 = df_list3.rename(columns={0:"lng"})

df = pd.concat([df_list,df_list2,df_list3], axis=1)

df = df.query("lat != '0'")
df.to_csv(filename+"location.csv",encoding="utf-8-sig")
df.tail()
