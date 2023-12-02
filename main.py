import pandas as pd
import requests
import warnings

warnings.filterwarnings('ignore')

url_dados_campeonato_brasileiro = "https://pt.wikipedia.org/wiki/Campeonato_Brasileiro_de_Futebol_de_2023_-_S%C3%A9rie_A"
req_site = requests.request(method="GET", url=url_dados_campeonato_brasileiro)

tabelas_site = pd.read_html(req_site.text)

tabela_classificacao = tabelas_site[6]
tabelas_jogos = tabelas_site[7]

nomes_times = list(tabelas_jogos["Casa \ Fora"])
apelidos = list(tabelas_jogos.columns)
indice_para_remover = [f for f in range(len(apelidos)) if apelidos[f] == 'Casa \\ Fora'][0]
apelidos.pop(indice_para_remover)

#Zip -> Faz juncao de listas do mesmo tamanho
sigla_times = dict(zip(apelidos, nomes_times))

