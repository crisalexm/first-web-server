import requests

def get_categories():

    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code) #status from http
    print(r.text) #respuesta, retorno o información que nos está entregando esta API
    print(type(r.text)) #reviso el formato... El formato es String pero necesito transformarlo a formato python (json)

    #convierto a json o formato python
    categories = r.json()

    #itero la lista, para solo mostrar el nombre
    for category in categories:
        print(category['name'])