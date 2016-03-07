from bs4 import BeautifulSoup # libreria para hacer scraping
import requests # libreria para manejar peticiones http

user_name = "crashzedran" # definimos el usuario
url = "https://twitter.com/%s" % user_name # la url

# realizamos la peticion a la web
req = requests.get(url) # metodo get

# obtenemos el estado de la peticion
state_req = req.status_code

# verificamos que el estado sea 200
if state_req == 200:
 	# pasamos el contenido de la web a un objeto BeautifulSoup
 	html_twitter = BeautifulSoup(req.text)

 	# obtenemos la informacion del usuario
 	info_user = html_twitter.find_all('div',{'class':'ProfileHeaderCard'})
 	for i,info in enumerate(info_user):
 		name = info.find('a',{'class':'ProfileHeaderCard-nameLink'}).getText()
 		user = info.find('a',{'class':'ProfileHeaderCard-screennameLink'}).getText()
 		bio = info.find('p',{'class':'ProfileHeaderCard-bio'}).getText()
 		print("Nombre: %s\nUsername: %s\nBiografia: %s" % (name,user,bio))

else:
	print("codigo de esta: " % state_req)