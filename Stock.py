import yfinance as yf
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup 
import csv

def Analyze(stock, howlong):
	try:
		df = yf.download(stock,period=howlong,interval='1d')["Adj Close"]
		df = df.iloc[::-1]
		dfnp = df.to_numpy()

		mean = np.mean(dfnp)
		std = np.std(dfnp)
		now_price = df[0]

		if(now_price<mean-std):
			return ["very low", stock, round(mean, 2), round(std, 2), round(now_price, 2)]
		elif(now_price<mean):
			return "dont"#["low", stock, mean, std, now_price]
		else:
			return "dont"
	except:
		return "nodata"

StockIdList=[]
def gethList():
	hList = ["https://tw.stock.yahoo.com/h/kimosel.php?tse=1&cat=%E6%B0%B4%E6%B3%A5&form=menu&form_id=stock_id&form_name=stock_name&domain=0"]
	root = "https://tw.stock.yahoo.com"
	r = requests.get(hList[0]) #將此頁面的HTML GET下來
	soup = BeautifulSoup(r.text,"html.parser")
	sel = soup.select("td.c3 a")
	for s in sel:
		hList.append(root+s["href"])
	return hList

def getId(herf):
	global StockIdList
	r = requests.get(herf)
	soup = BeautifulSoup(r.text,"html.parser")
	sel = soup.select("TR TD a.none")
	for s in sel:
		sl = s.text.replace("\n", "").split(" ")
		print(sl)
		StockIdList.append([sl[0]])

def SaveCSV():
	hList = gethList()
	for h in hList:
		try:
			getId(h)
		except:
			pass
	np_StockIdList = np.array(StockIdList)
	print(np_StockIdList)
	np.savetxt('./StockIdList.csv', np_StockIdList, delimiter=",", fmt='%s')



#print(Analyze("1101.TW", "2y"))
