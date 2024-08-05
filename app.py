import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url) #acessa dados contidos na url

if response.status_code == 200: # se o aceesso for valido status é 200
    dados_json = response.json() # armazena dados da url na variável
    
    dados_restaurantes = {}   # dicionário vazio
    
    for item in dados_json: # para cada item encontrado nos dados
        nome_do_restaurante = item['Company'] # armazena item específico na variável
        if nome_do_restaurante not in dados_restaurantes: # se os dados não for encontrado no dicionário 
            dados_restaurantes[nome_do_restaurante] = [] # armazena em uma lista vazia
            
        dados_restaurantes[nome_do_restaurante].append({ # adiciona lista em (dicionário vazio)
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })

        for nome_do_restaurante, dados in dados_restaurantes.items():
            nome_do_arquivo = f'{nome_do_restaurante}.jason'
            with open(nome_do_arquivo, 'wgit') as arquivo_restaurante:
                json.dump(dados, arquivo_restaurante, indent=4)
      
else: # se status não for válido 
    print(f'o erro foi {response.status_code}') #mostra status
    

#print(dados_restaurantes['McDonald’s']) # mostra infor filtrada pela chave dicionário