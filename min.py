N='netsh wlan connect name="SOBRI MMM5"'
M='http://sobricom.net/login'
E=True
C=False
A=print
import os,time as B,requests as D,sys
from bs4 import BeautifulSoup as J
import webbrowser as K
def F():A('reloaded ...')
def O():
	B=C;A('veillez vous authenntifier ...');id=input(' ')
	if id=='gedeon':B=E
	else:B=C
	if B:A('heureux de vous revoir ')
	else:A('identifiant de connexion invalide')
def G():
	G=C;F=0
	while not G:
		try:H=D.get(M);G=E;B.sleep(1)
		except:F+=1
		if F>=100:F=0;os.system(N);A('erreur de connexion');B.sleep(1)
	O=H.text;L=J(H.content,'html.parser');I=L.find_all('a')[0].get('href');K.open_new(I);A('link is ',I)
def H():os.system('tmac -n Wi-Fi -nr02 -re -s');A('mac mis a jour ')
def I():
	A('connexion check');I=B.time();F=E;K=60*4+40;G=0;H=0
	while F:
		J=B.time()
		if J>=I+K:F=C
		else:
			try:
				D.get(M)
				if J>=I+10:
					try:B.sleep(1);D.get('https://www.google.com/')
					except:G+=1;A('no internet  connexion')
			except:H+=1;B.sleep(1)
		if G>=3:G=0;F=C
		if H>=5:H=0;os.system(N);A('not connected to wifi')
		B.sleep(2)
def L():
	A('hacktools start ...');C=E;D=60*4+40;J=B.time()
	while C:H();G();F();I()
L()