import pandas as pd

#파일 불러오기
filename = input("불러올 파일이름 입력: ")
data1 = pd.read_csv(filename)
data1 = data1.drop('Unnamed: 0',axis=1)

#판단기준 및 가중치 설정
norms = [4.5, 4, 3.75, 3.6, 3.5, 3, 2.5, 2.0, 0]
weight = [1.5, 1.3, 1.2, 1.1, 1, 0.75, 0.5, 0.3, 0.3]

#필요한 데이터 뽑기
star = data1['Score']
numstar = data1['Numberofscore']

#총점 계산 및 별점수에따른 도전여부 설정
totalscore = []
challenge = []
for i,s in enumerate(star):
    for j,norm in enumerate(norms):
        if s >= norm:
            n = numstar[i]
            temp = s*n*weight[j]
            totalscore.append(round(temp,4))
            break
    if numstar[i] <= 10:
        challenge.append(0)
    else:
        challenge.append(1)

#header 지정 
totalscore = pd.DataFrame(totalscore)
totalscore.columns=['Totalscore']
challenge = pd.DataFrame(challenge)
challenge.columns=['Challenge']    

#리스트 합치고 내림차순으로 정렬 후 csv파일 내보내기
df_list = pd.concat([data1,challenge,totalscore],axis=1)
df_list = df_list.sort_values(by = ['Dong','Challenge','Totalscore'],ascending=[True,False,False])
df_list.to_csv('final.csv')

print("완료")
