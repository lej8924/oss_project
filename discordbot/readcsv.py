import csv

def readdata():
    no1data = []
    with open('discordbot/final.csv','r') as no1:
        csvreader = csv.reader(no1)

        for line in csvreader:
            no1data.append(line)
    
    return no1data
