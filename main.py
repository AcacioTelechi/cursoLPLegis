import requests
import json
import pandas as pd

url = "https://dadosabertos.camara.leg.br/api/v2"

resposta = requests.get(url)

resposta = resposta.content

xlxs = resposta.to_excel("exemplo.xlsx")