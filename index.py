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
	isvalide=False
	while not isvalide:
		try:
			time.sleep(2)
			data=rq.get('http://sobricom.net/login')
			isvalide=True
		except :
			print('erreur de connexion')

	dataParse=data.text
	soup = BeautifulSoup(data.content, 'html.parser')
	link=soup.find_all("a")[0].get('href')
	#link=soup.find('a').get('href')
	wb.open(link)
	print('link is ',link)


def macChanger():
	os.system('tmac -n Wi-Fi -nr02 -re -s')
	#os.system('TMAC/tmac.exe -n Wi-Fi -nr02 -re -s')
	print('mac mis a jour ')

def ConnexionCheck():
	print('connexion check')
	Itime=time.time()
	loop=True
	refresh=60*4
	while loop:
		curtime=time.time()
		if curtime >=Itime+refresh:
			loop=False
		else:
			try:
				rq.get('http://sobricom.net/login')
				try:
					rq.get('http://www.google.com')
				except:
					loop=False
					print('no internet  connexion')
			except:
				os.system('netsh wlan connect name="SOBRI MMM5"')
				print('not connected to wifi')
		time.sleep(2)


def main():
	print('hacktools start ...')
	Iloop=True
	Isleep=60*4+40
	Itime=time.time()

	while Iloop:
		macChanger()
		scraping()
		#sys.exit()
		toast()
		ConnexionCheck()
		#time.sleep(Isleep)

main()

### wifi hacker by anonymous13 ###