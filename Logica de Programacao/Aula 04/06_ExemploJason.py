import requests

url = 'https://api.adviceslip.com/advice'

for i in range (10):
    resposta = requests.get(url)
    resposta = resposta.json()
#reponse 200 - Ok
    print(resposta['slip']['advice'])