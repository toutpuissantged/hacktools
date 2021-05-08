from modules import * 

class HackTools(object):
	'''
	HackTools est un script qui exploite une faille particulier 'le free minute trial' sur 
	les reseaux wifi public et permet d'automatiser des taches comme la verification de 
	connexion reseaux , la verification de la connection a internet , le changement automatique 
	et a interval de temps regulier de l'adresse mac '''

	def __init__(self):
		'''
			la configuration du script ce fait ici , donc desolee pour les non programmeur 
			l'objet config permet de configurer le ssid , l'url de la page de connexion , 
			le site de test pour verifier la connexion internet , refresh pour specifier le 
			temps de rechargement de l'adresse mac , dev-data est un objets custom pour le 
			developement '''

		self.config={
			'user':'prod',
			'ssid':'SOBRI MMM5',
			'url':'http://sobricom.net/login',
			'ssid_list':['SOBRI MMM5','SOBRICOM','SOBRICOM 2','SOBRICOM 3','WIFI FOZANE 2'],
			'test':'https://www.google.com/',
			'refresh':60*4+10, # temps de rafraichissement 
			'dev-data':{
				'ssid':'SOBRI MMM5',
				'url':'http://sobricom.net/login',
				'ssid_list':['SOBRI MMM5','SOBRICOM','SOBRICOM 2','SOBRICOM 3','WIFI FOZANE 2'],
				'test':'https://www.google.com/',
				'refresh':1,
			},
		}
		self.state={
            'statut':'disconnected',
            'reload':0,
            'wifi-name':'Sobri mimi',
            'username':'?',
            'app-name':'HACKTOOLS',
			'start-time':time.time()

        }
		self.wifi_used=self.config['ssid']
		self.link=""
		self.version = '2.0'




	def arg_pars(self):
		pass

	def time_builder(self,timer):
		timer=int(timer)
		time_schema={
			'heures':0,
			'minutes':0,
			'seconde':0,
		}

		minute=timer//60
		time_schema['seconde']=timer
		if (minute<1):
			return time_schema
		seconde=timer%60
		minute=timer//60
		time_schema['seconde']=seconde
		time_schema['minutes']=minute
		if (minute//60<1):
			return time_schema

		heures=minute//60
		minute=minute%60
		time_schema['heures']=heures
		time_schema['minutes']=minute

		return time_schema

	def showConnectedInfo(self):

		os.system('cls' if os.name=='nt' else 'clear')
		data=self.time_builder(time.time()-self.state['start-time'])
		heures=''
		minutes=''
		seconde=''
		if(data['heures']>0):
			heures=' {}h'.format(data['heures'])

		if(data['minutes']>0):
			minutes=' {}m'.format(data['minutes'])

		if(data['seconde']>0):
			seconde=' {}s'.format(data['seconde'])

		print(" > {} : {} \t  reload : {} \t --- {} --- \t user > {} \t active time >{} {} {} ".format(self.state['wifi-name'],self.state['statut'],self.state['reload'],self.state['app-name'],self.state['username'],heures,minutes,seconde),end="\r")
		time.sleep(1)

	def header(self):
		'''
			permet de presenter l'application en exposent la version utiliser ,
			le nom , le developeur etc ...

		'''

		print(" --------------- hack tools  version {}  by anonymous13  ---------- \n".format(self.version))
		print(" ---------------- demarage du moteur ... -------------------")
		res=input('\n En continuent vous accepter etre l\'unique responsable de l\'utilisation que vous faites de cet logiciel qu\'il s\'agit de piratage ou autres action efeectuer sur un reseau qui n\'est pas le votre ainsi vous assumer entirement toutes poursuite judicaire occasionner ? Oui/Non ')
		if(res!='Oui'):
			print('\n ====> ok donc allez vous faire ')
			time.sleep(2)
			sys.exit()

	def Connect(self,ssid):
		'''
			permet de connecter le peripherique au reseau via un appel systeme 
			developer pour windows , les utilisateurs linux 

		'''
		cmd = 'netsh wlan connect name="{}"'.format(ssid)
		rep=subprocess.call(cmd)
		return 0

	def scraping(self):
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
				self.Connect(self.wifi_used)
				time.sleep(1)

		dataParse=data.text
		soup = BeautifulSoup(data.content, 'html.parser')
		self.link=soup.find_all("a")[0].get('href')
		#link=soup.find('a').get('href')
		wb.open(self.link)
		self.state['statut']= 'connecting ...'
		
		print('link is ',self.link)

	def macChanger(self):
		'''
			change aleatoirement l'adresse mac 
			attention pour ceux qui on telechager les script 
			sur internet , il faut installer tmac et le mettre dans 
			les variables d'environement = le PATH ou soit de mettre l'excecutable tmac 
			danc un dossiers nommer TMAC et de faire l'appelle systeme vers cet dossiers 
			ex : os.systeme('/TMAC/tmac.exe -n Wi-Fi -nr02 -re -s')

		'''
		#os.system('tmac -n Wi-Fi -nr02 -re -s')
		subprocess.call('tmac -n Wi-Fi -nr02 -re -s')
		
		print('mac mis a jour ')

	def ConnexionCheck(self):
		'''
			le composent intelligent du core : verifier et resout les probleme de 
			connexion au wifi et a internet 
		'''
		print('connexion check')
		
		Itime=time.time()
		loop=True
		refresh=self.config['dev-data']['refresh'] 
		notconected=0
		tour=1
		max_notconected=5
		max_tour=5
		first_loop=True
		first_loop_state=1
		wifi_used_id=0

		while loop:
			self.showConnectedInfo()
			curtime=time.time()
			if curtime >=Itime+refresh:
				loop=False
				self.state['statut']= 'reloading'
			else:
				time.sleep(1)
				try:
					rq.get(config['url'])
					self.state['statut']= 'connected'
					if curtime >=Itime+10:
						try:
							rq.get(config['test'])
						except:
							#loop=False
							notconected+=1
							self.state['statut']= 'no internet  connexion'
							print('no internet  connexion')
							
							wb.open(link)
							print('link is ',link)
							time.sleep(2)

				except:
					tour+=1
					self.state['statut']= 'disconnected'

			if notconected>=max_notconected:
				notconected=0
				loop=False

			if tour>=max_tour :
				tour=0
				self.Connect(self.wifi_used)

			if first_loop==True :
				
				first_loop_state=self.Connect(self.wifi_used)
				if first_loop_state:
					first_loop=True
				else:
					first_loop=False
						
				#first_loop=False
				print('@ first loop')
				time.sleep(1)

			time.sleep(2)

	def start(self):
		'''
			boucle principale qui est le chef d'aurchestre du script 

		'''
		os.system('cls' if os.name=='nt' else 'clear')
		self.header()
		while True:
			self.showConnectedInfo()
			self.macChanger()
			self.scraping()
			self.ConnexionCheck()


hack = HackTools()

hack.start()


#######################################################
##
##  version 1.4   
##
##  developer par  toutpuissantged 
##
##  github  : https://www.github.com/toutpuissantged
##
#######################################################