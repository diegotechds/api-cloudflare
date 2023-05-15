#!/usr/bin/env python3
"""Script para criação e alteração de records DNS na CloudFlare 

Script para quem esta querendo atualizar o ip do registro do DNS 
do seu site ou url de sitema no a CloudFlare. 

Meu caso de uso:

No meus estudos sempre estou derubando a minha infra e não quero
deixar o ip fixo, então fica com o ip dinamico e com esse script posso 
pegar a saida do Terrform ou aws cli para pegar os ips dos servidores e atualizar
meu registros. 

Como usar: 
Vc pode colocar os valores de ids e nome de zonas na mão ou pegar
das variaveis de ambiente, pra isso estou importanto o "OS".

"""

__version__ = "0.1.0"
__author__ = "Diego Marques"
__license__ = "Unlicense"

import requests
import os, sys


# Insira suas credenciais do Cloudflare aqui
email = 'VAR_EMAIL'
key = 'VAR_TOKEN'
# Insira o nome do zona que vai mudar o record
zone_name = 'VAR_NOME_ZONA'
# Insira o nome do registro DNS que deseja atualizar
record_name = 'VAR_RECORD_DNS'
# Insira o ip que vai ser criado ou subistituir o record dns
record_ip = 'VAR_IP'


# URL da API do Cloudflare para listar ZONAS DNS
url = f'https://api.cloudflare.com/client/v4/zones'

# Cabeçalhos da solicitação
headers = {
    'X-Auth-Email': email,
    'Authorization': key,
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers).json()
dns_zones = response['result']

zone_id = None
for zone in dns_zones:
    if zone['name'] == zone_name:
        zone_id = zone['id']
        break

# URL da API do Cloudflare para listar registros DNS
url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'

# Cabeçalhos da solicitação
headers = {
    'X-Auth-Email': email,
    'Authorization': key,
    'Content-Type': 'application/json'
}

# Lista todos os registros DNS da zona
response = requests.get(url, headers=headers).json()
dns_records = response['result']

# Procura pelo registro DNS com o nome especificado
record_id = None
for record in dns_records:
    if record['name'] == record_name:
        record_id = record['id']
        break

# Se o registro for encontrado, atualiza-o
if record_id:
    # URL da API do Cloudflare para atualizar o registro DNS
    url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}'

    # Dados para atualizar o registro DNS
    data = {
        'type': 'A',
        'name': record_name,
        'content': record_ip
    }

    # Envia a solicitação PUT para atualizar o registro DNS
    response = requests.put(url, headers=headers, json=data)

    # Verifica se a solicitação foi bem-sucedida
    if response.status_code == 200:
        print('Registro DNS atualizado com sucesso!')
    else:
        print('Erro ao atualizar o registro DNS:', response.text)
else:
    print('Registro DNS não encontrado.')
