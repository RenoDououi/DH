# 105971001 數位人文作業1
from os import listdir, walk
from os.path import isfile, isdir, join
import os
import glob
import sys
import re
"""
書面作業
學期成績比重：5%
寄交電子檔案；在 Moodle 課程網頁上上傳你的程式和回答下列問題；
上傳截止時間：四月廿五日上午 8:00 之前 (系統會自動關閉，請注意時間)
作業上傳網址：HW1 (http://moodle.nccu.edu.tw/mod/assign/view.php?id=166309)
一、資料來源：從「臺灣數位人文小小讚」網站下載《紅樓夢》語料
==> 進入「臺灣數位人文小小讚」、點選上方 「文本語料」，然後下載該網頁中的紅樓夢
二、自己撰寫程式分析上述語料並且回答下列問題。
1. 賈寶玉在這一份《紅樓夢》中出現幾次？林黛玉幾次？
2. 賈寶玉在這一份《紅樓夢》中笑過幾次？林黛玉幾次？
三、工作說明：你必須撰寫自己的程式，不可以用手算、也不可以用任何其他軟體工具，來回答上面的問題。你必須繳交你的程式的文字檔案。
四、討論和心得：以上這兩個問題並不簡單，你應該多加思考；除了回答上述問題之外，你必須說明上面的問題為何不簡單？
五、上傳方式：把你的程式、答案和心得壓縮在一份壓縮檔案中一併上傳。
"""
'''
失敗屍體：一次抓整個資料夾
DATA_DIR = "../pyt/RBD"
file_data = []
for filename in os.listdir(DATA_DIR):
    print ("Loading: %s" % filename)
    loadFile = open(os.path.join(DATA_DIR, filename),'r')
    file_data.append(loadFile.read())
    n1 = file_data.count("保育")
    print("「寶玉」這個字出現了",n1,"次")
    loadFile.close()
    #print(file_data)
'''
d1 = {1:"一",
      2:"二",
      3:"三",
      4:"四",
      5:"五",
      6:"六",
      7:"七",
      8:"八",
      9:"九",
      0:"零",
      "w":"十",
      "x":"佰",
      "y":"仟",
      "z":"萬",}

text = []
#預設擷取的章節頭尾
head = 1
tail = 120
print("歡迎來到：「黛玉寶玉呵呵笑計數器：」""請問您想要從哪一回開始查呢？：")
head = eval(input())
print("想要查到哪一回？：")
tail = eval(input())
#每回出現次數 dy黛玉 by寶玉
dy = 0
by = 0
#總共出現次數
dysum = 0
bysum = 0
#笑數量 dys=>黛玉笑,  dysc=>黛玉笑.count (每一回校的次數)
dysc = 0
bysc = 0
#全部笑的次數 dysct =>dys.count total
dysct = 0
bysct = 0

for n in range(head,tail+1,1):
    chpt = [] #第幾回
    #這邊的回數有四種表達法：1~9, 10~19 十到十九, 20~99 二十到九十九, 100~999 一零零到九九九
    a = int(n/100) #百位數
    b = int(n%100/10) #十位數
    c = int(n%10/1) #個位數
    if a>0:
        chpt = d1[a],d1[b],d1[c]
    elif b>=2 and c != 0:
        chpt = d1[b],"十",d1[c]
    elif b>=2 and c == 0:
        chpt = d1[b],"十"
    elif 2>b>=1 and c != 0:
        chpt = "十",d1[c]
    elif b==1 and c==0:
        chpt = "十"
    elif c>=0:
        chpt = d1[c]
    chpt = "".join(chpt) #list to string
    #print(n,a,b,c,chpt) #測試數字轉漢字有沒有錯
    #上面是冗長的chpt計算

# MAC的編碼糟糕 要寫encoding 常用GKB,UTF-8,簡中GB2312,繁中Big5
# notice:檔名 第一一一回_.txt 回後面有一個空格
    with open("../pyt/RBD/第%s回 .txt" %(chpt), "r", encoding='UTF-8') as f1:
        text = f1.readlines() #為了刪掉每章節標題而沒用read
        del text[0] #刪掉每章節標題
        text = "".join(text) #list to string
        #print(text) #測試用
        dy = text.count("黛玉")
        dysum = dysum + dy
        by = text.count("寶玉")
        bysum = bysum + by    
        
        #以下是笑 dys=>黛玉笑(文字), dysc=>黛玉笑count, dysct=dysc 
        #笑的同義詞：http://www.hkdictionary.net/synonym/result2.asp?Sense=%AF%BA
        #除了：忍俊不禁/前仰後合/哂/哄堂/捧腹/哧哧/發噱/絕倒/開顏/粲/嫣然/噴飯/噱/樂/囅然
       
        dys = re.findall('黛玉+笑',text) #這行還要再改
        dys = "".join(dys)
        dysc = dys.count('黛玉笑')
        dysct = dysct + dysc
        #print(dys,sep='',end='') #測試用
        bys = re.findall('寶玉+笑',text) #這行還要再改
        bys = "".join(bys)
        bysc = bys.count('寶玉笑')
        bysct = bysct + bysc

        #每一回中出現幾次
        print("在第",chpt,"回中，「黛玉」出現了",dy,"次，笑了",dysc,"次。寶玉出現了",by,"次，笑了",bysc,"次。",sep="")

#總共出現多少次
print("從第",head,"回到第",tail,"回中，",sep='')
print("黛玉總共出現",dysum,"次，笑了",dysct,"次。")
print("寶玉總共出現",bysum,"次，笑了",bysct,"次。")