# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 03:22:21 2020

@author: Vishal Rana
"""

import requests
from bs4 import BeautifulSoup
import tkinter as tk

url = 'https://www.worldometers.info/coronavirus/#countries'

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36"}
page = requests.get(url, headers = headers)    
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.findAll('tr')

name = 'India'
def data(name):
    data = []
    for i in table:
        a = i.get_text().strip()
        data.append(a)
        
    for i in data:
        a = i.index(' ')
        b = i[0:a]
        if b == name:
            split = i.split()
            test = str('Total Cases: ') + split[1] + str('\n') + str('New Cases: ') + split[2] + str('\n') + str('Total Deaths: ') + split[3] + str('\n') + str('Total Recovered: ') + split[4] + str('\n') + str('Active Cases: ') + split[5] + str('\n') + str('Total Cases/1M pop: ') + split[6]
            label['text'] = test       
        
root = tk.Tk()
root.title('India Corona Stats')
canvas = tk.Canvas(root, height = 500, width = 500 )
canvas.pack()

frame = tk.Frame(root, bg = "#80c1ff", bd = 5)
frame.place(relx = .5, rely = .1, relwidth = .75, relheight = .1,anchor = 'n')

entry = tk.Entry(frame,font = 40)
entry.place(relwidth = .65, relheight = 1)

button = tk.Button(frame, text = "Get details", font = 10, command = lambda: data(entry.get()))
button.place(relx = 0.7, rely = 0, relwidth = .30, relheight = 1)

lower_frame = tk.Frame(root, bg = "#80c1ff", bd = 10)
lower_frame.place(relx = .5, rely = .25, relwidth = .75, relheight = .6,anchor = 'n')

label = tk.Label(lower_frame)
label.place(relwidth = 1, relheight = 1)

root.mainloop()
