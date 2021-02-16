from modules import * 

os.system('cls' if os.name=='nt' else 'clear')

def header():
    f = Figlet(font='bulbhead')
    print(f.renderText('hack tools'))

config={

	'ssid':'SOBRICOM',
	'url':'http://sobricom.net/login',
	'ssid_list':['SOBRI MMM5','SOBRICOM','SOBRICOM 2'],
}

def toast():
	'''  
		permet de faire des notif a chaque reload de la boucle pricipale 
	'''
	print('reloaded ...')
	#sys.exit()

def auth():
	'''
		se charge de l'autentification 
	'''
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
	'''
		soccupe de recuperer le liens de free trial et 
		l'ouvre dans un nouvel onglet du navigateur par defaut
	'''
	isvalide=False
	loop=0
	while not isvalide:
		try:
			data=rq.get(config['url'])
			isvalide=True
			
		except :
			loop+=1
			time.sleep(1)
		if loop>=10:
			loop=0
			os.system('netsh wlan connect name="{}"'.format(config['ssid']))
			print('erreur de connexion')
			time.sleep(1)

	dataParse=data.text
	soup = BeautifulSoup(data.content, 'html.parser')
	link=soup.find_all("a")[0].get('href')
	#link=soup.find('a').get('href')
	wb.open_new(link)
	print('link is ',link)


def macChanger():
	'''
		change aleatoirement l'adresse mac 
	'''
	os.system('tmac -n Wi-Fi -nr02 -re -s')
	#os.system('TMAC/tmac.exe -n Wi-Fi -nr02 -re -s')
	print('mac mis a jour ')

def ConnexionCheck():
	'''
		le composent intelligent du core : verifier et resout les probleme de 
		connexion au wifi et a internet 
	'''
	print('connexion check')
	Itime=time.time()
	loop=True
	refresh=60*4+30
	notconected=0
	tour=1
	max_notconected=3
	max_tour=5
	first_loop=True
	while loop:
		curtime=time.time()
		if curtime >=Itime+refresh:
			loop=False
		else:
			time.sleep(1)
			try:
				rq.get('http://sobricom.net/login')
				if curtime >=Itime+10:
					try:
						rq.get('https://www.google.com/')
					except:
						#loop=False
						notconected+=1
						print('no internet  connexion')

			except:
				tour+=1

		if notconected>=max_notconected:
			notconected=0
			loop=False

		if tour>=max_tour :
			tour=0
			os.system('netsh wlan connect name="{}"'.format(config['ssid']))
			print('not connected to wifi')

		if first_loop==True and tour==2:
			
			os.system('netsh wlan connect name="{}"'.format(config['ssid']))
			first_loop=False
			print('not connected to wifi @ first loop')
			time.sleep(3)

		time.sleep(2)


def main():
	'''
		boucle principale 
	'''
	header()
	Iloop=True
	Isleep=60*4+40
	Itime=time.time()

	while Iloop:
		macChanger()
		scraping()
		toast()
		ConnexionCheck()

main()

### wifi hacker by anonymous13 ###