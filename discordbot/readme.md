
# Discord Bot-노원구 맛집 추천 봇🤖

  

<img src="https://beebom.com/wp-content/uploads/2018/02/discord-bots.jpg?w=750&quality=75" width="300">

Discord Bot API를 이용하여 노원구 내 맛집🍲을 이용자의 니즈에 따라 추천해주는 봇을 개발함.

  

## 🤔Getting Started

  

- Prerequisites🤷
- About folders🗂️

  

### 🖊️Prerequisites

  
"requirement.txt"에 작성되어 있음

  

```

discord
asyncio
discord_buttons_plugin
discord.ext
discord_components
readcsv
pandas

```

  

### 📁About folders

  

oss_project의 "master" branch에 있는 폴더에 대해 설명하는 부분입니다.


  

**📁folder1. discord_bot**

  

```

📝readcsv.py
final.csv파일을 불러옴

📝requirements.txt
install이 필요한 패키지들을 설명

📝run.py
discord bot 사전 테스트 py파일

📝runtime.txt
필요 파이썬 버전

📝sketch.py
최종 discord bot py파일

```

  

**📁folder2. data**

  

```

📝algo.py
맛집으로 분류할 가중치 알고리즘 파일

📝concat_csv.py
한식,일식,양식,카페,기타(인도/태국 등)으로 식당의 업종 및 지역을 분류하는 파일

📝final.csv
디스코드 봇에 쓰일 최종 csv파일

📝gong2.csv,ha2.csv,joong2.csv,no1.sang2.csv,wol2.csv
각 동마다 추출해낸 식당 리스트 csv파일

📝no1.csv,nowon.csv
final.csv로 가기 전단계 csv파일들

📝readme.md
data폴더에 대한 간단한 설명
```
**📁folder3. crawling**

  

```

📝crawling.py
chromedriver로 카카오맵을 활성화하여
'Name','Score','Numberofscore','Review','Link','Addr1','Addr2','Typename'컬럼을 뽑아내옴.csv파일 형태로 저장함.

📝mapping.py
위의 'crawling.py'에서 뽑아내지 못한 위도와 경도 정보를 googlemaps api를 이용함.
각각 'Latitude','Longtitude'컬럼으로 위의 컬럼들에 이 두 가지를 추가함.

📝chromedriver
설치한 크롬드라이버

📝readme.md
크롤링 폴더에 대해 간단히 설명한 readme파일

```
crawling csv파일 예시

|   | Name | Score | Numberofscore | Review | Link | Addr1 | Addr2 | Typename | Latitude | Longtitude | Typenum | Dong | Challenge | Totalscore |
|---|------|-------|---------------|--------|------|-------|-------|----------|----------|------------|---------|------|-----------|------------|
|   | 식당이름 | 식당평점 |  평가갯수  |  리뷰갯수  | 식당링크 | 도로명주소 |    지번주소   |  음식종류| 위도  |  경도   |  음식종류 정수화  | --동 정수화 |  도전여부         | 알고리즘 결과|

  
## Running OUR project!

  

✨저희의 *노원구 맛집 찾기 Discord Bot*을 소개합니다✨

  

### 📌"sketch"파일 실행

  

실행하는 사진 첨부(python파일)

  

  

### 📌heroku에서 작동

 
 실행하는 사진 첨부(heroku내에서)

  

```

이거는 공릉동에서 한식을 먹고싶은 도전하고 싶지 않은 홍길동씨를 가정하고 봇이랑 대화하는거 첨부

```

  

## Deployment

  <img src="data:image/png;base64,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" width="300">


-heroku에 배포함
(누구든지 discord bot을 사용할 수 있음)

  

## Reference

  

*  [Repository Template ](https://github.com/always0ne/repositoryTemplate)) - 마크다운 양식 참고

*  [Discord Developer Portal — Documentation — Intro](https://discord.com/developers/docs/intro) - discord 공식 API 참고

*  [디스코드 봇 만들기#12 - 서버 호스팅 :: 작업일지](https://lektion-von-erfolglosigkeit.tistory.com/97?category=955777) - discord bot heroku 연동 참고

* [Python Project : 맛집 지도 시각화 ](https://nostalgiaa.tistory.com/36)-카카오맵 웹크롤링 참고
  


## Developers🖥️

  

*  **20102040 이은재** 
*  **18100061 김용욱** 


  

## License💳

  

This project is licensed under the MIT License 

  

## Acknowledgments

 * Discord Bot API, Googlemaps API를 알게 됨
 * github을 통한 협업을 경험해봄
