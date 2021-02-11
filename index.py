import os
import time
import requests as rq
import sys
from bs4 import BeautifulSoup
import webbrowser as wb

def toast():
	print('reloaded ...')
	#sys.exit()

def auth():
	isvalide=False
	print('veillez vous authenntifier ...')
	id=input(' ')
	if id=='gedeon':
		isvalide=True
	else:
		isvalide=False

	if isvalide:
		print('heureux de vous revoir ')
	else:
		print('identifiant de connexion invalide')
	

def scraping():
	isvalide=False
	loop=0
	while not isvalide:
		try:
			data=rq.get('http://sobricom.net/login')
			isvalide=True
			
		except :
			loop+=1
			time.sleep(1)
		if loop>=10:
			loop=0
			os.system('netsh wlan connect name="SOBRI MMM5"')
			print('erreur de connexion')
			time.sleep(1)

	dataParse=data.text
	soup = BeautifulSoup(data.content, 'html.parser')
	link=soup.find_all("a")[0].get('href')
	#link=soup.find('a').get('href')
	wb.open_new(link)
	print('link is ',link)


def macChanger():
	os.system('tmac -n Wi-Fi -nr02 -re -s')
	#os.system('TMAC/tmac.exe -n Wi-Fi -nr02 -re -s')
	print('mac mis a jour ')

def ConnexionCheck():
	print('connexion check')
	Itime=time.time()
	loop=True
	refresh=60*4+40
	notconected=0
	tour=0
	while loop:
		curtime=time.time()
		if curtime >=Itime+refresh:
			loop=False
		else:
			try:
				rq.get('http://sobricom.net/login')
				if curtime >=Itime+10:
					try:
						time.sleep(1)
						rq.get('https://www.google.com/')
					except:
						#loop=False
						notconected+=1
						print('no internet  connexion')

			except:
				tour+=1
				time.sleep(1)

		if notconected>=5:
			notconected=0
			loop=False

		if tour>=5 or tour==1:
			tour=0
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