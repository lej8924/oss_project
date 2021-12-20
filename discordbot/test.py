import pandas as pd
import random

data = pd.read_csv('discordbot/final.csv')
data = data.drop('Unnamed: 0',axis=1)

userdata = ['B', None, 1]


print(userdata)
if userdata[1] == None:
        temp = data.loc[(data['Dong']== userdata[0]) & (data['Challenge']== userdata[2])]
        length = len(temp)
        i = random.randint(0,length)
        t = float(temp['Score'][i:i+1].values)
        url = temp['Link'][i:i+1].values[0]
        print(temp)
        print(temp['Name'][i:i+1].values)
        print(url)
        print(t)

        
if userdata[0] == None:
        temp = data.loc[(data['Typenum']==userdata[1]) & (data['Challenge']== userdata[2])]
        print(temp)
        
if (userdata[0]!=None) and (userdata[1] !=None):
        temp = data.loc[(data['Dong']== userdata[0]) & (data['Typenum']==userdata[1]) & (data['Challenge']== userdata[2])]
        print(temp)