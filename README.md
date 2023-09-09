# api-cloudflare

Install dependencia para rodar o script: 

Comando: 
#sudo pip install requests 


Script para criação e alteração de records DNS na CloudFlare 

Script para quem esta querendo atualizar o ip do registro do DNS 
do seu site ou url de sitema no a CloudFlare. 

Meu caso de uso:

No meus estudos sempre estou derubando a minha infra e não quero
deixar o ip fixo, então fica com o ip dinamico e com esse script posso 
pegar a saida do Terrform ou aws cli para pegar os ips dos servidores e atualizar
meus registros. 

Como usar: 
Vc pode colocar os valores de ids e nome de zonas na mão ou pegar
das variaveis de ambiente, pra isso estou importanto o "OS".
