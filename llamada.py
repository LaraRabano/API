import requests


apikey = "E1608E4F-F1D1-4449-B8A4-513461E57ECD"
headers = {
    "X-CoinAPI-Key": apikey
}
api_url = "http://rest-sandbox.coinapi.io"
endpoint = "/v1/exchanges"

url = api_url + endpoint

respuesta = requests.get(url, headers=headers,)
codigo = respuesta.status_code

if codigo == 200:
    print ("El resultado de la consulta es:")
    print (respuesta.text)
else:
    print ("La petición a la API ha fallado")
    print("El código del error es {codigo}")
    print(f"Razón del error {respuesta.reason}")
    print(respuesta.text) 
