from modules import * 

os.system('cls' if os.name=='nt' else 'clear')

global wifi_used

config={

	'ssid':'SOBRI MMM5',
	'url':'http://sobricom.net/login',
	'ssid_list':['SOBRI MMM5','SOBRICOM','SOBRICOM 2','WIFI FOZANE 2'],
}

wifi_used=config['ssid']

def configLoad():
	temp1=open('core/version.json','r')
	temp2=temp1.read()
	temp1.close()

	temp3=json.loads(temp2)

	return temp3

def header():
	f = Figlet(font='bulbhead')
	print(f.renderText('hack tools'))
	conf=configLoad()
	print("version {}  by anonymous13 \n".format(conf['version']))
	auth()
	print("demarage du moteur ...")

def Connect(ssid):
	call=os.system('netsh wlan connect name="{}"'.format(ssid))
	#print('not connected to wifi ||| call :{}'.format(call))
	return call

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
	login='gedeon'
	print(' veillez vous authentifier : ')
	id=input(' ==> ')
	if id==login:
		isvalide=True
	else:
		isvalide=False

	if isvalide:
		print('authentification reussi !')
	else:
		print('identifiant de connexion invalide \n fermeture du moteur !!!')
		time.sleep(0.5)
		exit()
	

def scraping():
	'''
		soccupe de recuperer le liens de free trial et 
		l'ouvre dans un nouvel onglet du navigateur par defaut
	'''
	isvalide=False
	loop=0
	global wifi_used
	
	while not isvalide:
		try:
			data=rq.get(config['url'])
			isvalide=True
			
		except :
			loop+=1
			time.sleep(1)
		if loop>=10:
			loop=0
			call=Connect(wifi_used)
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
	refresh=60*4+30 # temps de rafraichissement 
	notconected=0
	tour=1
	max_notconected=3
	max_tour=5
	first_loop=True
	first_loop_state=1
	wifi_used_id=0
	global wifi_used

	while loop:
		wifi_used=config['ssid_list'][wifi_used_id]

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
			Connect(wifi_used)

		if first_loop==True :
			
			first_loop_state=Connect(wifi_used)
			if first_loop_state:
				first_loop=True
			else:
				first_loop=False
    				
			#first_loop=False
			print('@ first loop')
			time.sleep(3)

		time.sleep(2)


def main():
	'''
		boucle principale 
	'''
	header()
	#Iloop=True
	#Isleep=60*4+40
	#Itime=time.time()

	while True:
		macChanger()
		scraping()
		toast()
		ConnexionCheck()

main()

### hack tools by anonymous13 ###