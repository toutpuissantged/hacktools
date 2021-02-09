import os
import time
import requests as rq
import sys
from bs4 import BeautifulSoup
import webbrowser as wb

def toast():
	print('reloaded ...')
	#sys.exit()

def scraping():
	data=rq.get('http://sobricom.net/login')
	dataParse=data.text
	soup = BeautifulSoup(data.content, 'html.parser')
	link=soup.find_all("a")[0].get('href')
	#link=soup.find('a').get('href')
	wb.open(link)
	print('link is ',link)


def macChanger():
	#os.system('tmac -n Wi-Fi -nr02 -re -s')
	os.system('TMAC/tmac.exe -n Wi-Fi -nr02 -re -s')
	print('mac mis a jour ')

def main():
	print('hacktools start ...')
	Iloop=True
	Isleep=60*4

	while Iloop:
		scraping()
		#sys.exit()
		macChanger()
		toast()
		time.sleep(Isleep)

main()


### wifi hacker by anonymous13 ###