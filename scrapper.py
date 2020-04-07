from tkinter import * as tk
from bs4 import BeautifulSoup
import request
import webbrowser
url=input("enter the url heare")
if url=="":
	url=""
try:
	page=request.get(url)
	print("Response:",page)
	data=page.text
	feature='html.parser'
	soup=BeautifulSoup(data,features)
except:
	pass
def open1():
	a=(list.curselection())
	b=a[0]
	webbrowser.open(list1.get(b))

root=Tk()
root.geometry("400x400")
root.title("web_scrapper")
list1=ListBox(root,width=300,height=20,selectmode=SINGLE)
list1.pack(fill=BOTH)
x=0
for link in soup.find_All('a'):
	link1=(link.get('href'))
	link1=(str(link1))
	if link1.startswith('http')==True:
		list1.insert(x,link1)
	else:
		if link1=="None" or link1=="#":
			pass
		else 
		link1==url+link1
		list1.insert(x,link1)
	x+=1
button1=Button(root,text="open",command=open1)
button1.pack(fill=BOTH)
root.mainloop()

