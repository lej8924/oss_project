import tkinter as tk
from fnmatch import fnmatch
from tkinter.constants import BOTH, BOTTOM, CENTER, LEFT, RIGHT
import csv


class getdata:
    def __init__(self):
        self.data = []
        self.features = ['상호명','상권업종대분류코드',
        	'상권업종대분류명',	'상권업종중분류코드',
            '상권업종중분류명',	'상권업종소분류코드',	
            '상권업종소분류명',	'표준산업분류명',	
            '시도명',	'시군구명',	
            '행정동명',	'법정동명',	
            '지번주소',	'도로명주소',	
            '경도',	'위도']

    def reader(self,filename):
        with open(filename,'r') as f:
            csv_reader = csv.reader(f)
            for line in csv_reader:
                self.data.append(line)
        

class ChatBot:
    def __init__(self,data):
        self.data = data
        self.data.reader('/Users/yu/Desktop/OSS/Termproj/노원_상권_정보2.csv')
        self.location = [
            (f'*{self.data.data[1][11]}*', f'{self.data.data[1][11]} 맛집을 찾아드릴게요.\n'+f'{self.data.data[1]}')
        ]
        self.talk_unknown = "I don't understand your words."

    def reply(self, msg):
        for pattern, response in self.location:
            if fnmatch(msg, pattern):
                return response
        return self.talk_unknown

class SimpleChatBotGUI():
    def __init__(self, chatbot, master):
        self.chatbot = chatbot
        self.master = master
        self.master.title('뭐머글랭? - 맛집추천 챗봇')
        self.label = tk.Label(master, text='Dialog')
        self.label.pack()
        self.text_dialog = tk.Text(master)
        self.text_dialog.pack()
        self.label = tk.Label(master, text='Your Message:')
        self.label.pack()
        self.entry_msg = tk.Entry(master)
        self.entry_msg.pack()
        self.button_send = tk.Button(master, text='send', command=self.location_button)
        self.button_send.pack()
        self.text_dialog.insert('end', 'Bot: 뭐 먹지?\n')

    def handle_button(self):
        msg = self.entry_msg.get()
        self.text_dialog.insert('end',msg.rjust(74) + ':You'+ '\n\n')
        self.text_dialog.insert('end', 'Bot: ' + self.chatbot.reply(msg) + '\n\n')
        self.entry_msg.delete(0, tk.END) # Clear 'entry_msg' after reply
    
    def location_button(self): # 버튼 변경
        self.button_send.pack_forget()
        
        for i in range(3):
            self.button_choice = tk.Button(text = f'{self.chatbot.location[i][0]}',command = self.handle_button)
            self.button_choice.pack(side = LEFT,expand=True)

if __name__ == '__main__':
    data = getdata()
    chatbot = ChatBot(data)
    root = tk.Tk()
    app = SimpleChatBotGUI(chatbot, root)
    print(chatbot.location)
    root.mainloop()