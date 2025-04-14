# Enriquece Metadados de Veículos via acesso à API da OpenAI
# API Back End - Responsável pelo armazenamento , recuperação das informações de Veículos na base de dados SqlLignt
# Data: 13/04/2025
# Por: Ronaldo Ramos da Costa.
Este pequeno projeto faz parte da entrega do MVP da Disciplina **Arquitetura de Software** 


## Situação Problema


Diversos sistemas envolvendo o cadastramento de Metadados, muitas vezes são incompletos e possuem grande dificuldade para encontrar  informações relevantes que possam garantir a completude de uma gama de dados necessários para o bom funcionamento do negócio. A dificuldade de encontrar informações, pode ser apoiada com o uso de Inteligência Artificial.


##  Objetivo


Utilizar a API da OpenAIi - Inteligência Artificial , para complementar informações cruzadas de Automóveis x Localização a partir do CEP , encontrando valores de venda praticados na região geográfica do veículo, bem como obter o  valor de custo de um seguro Anual do automóvel na região do Cep.

Desta forma é possivel experimentar o uso cruzado de APIs x IAs , com o objetivo de enriquecer metadados necessários para o bom andamento de um negócio.



##  Escopo do MVP

Prover consultas a partir do FRONT-END, funcionando como BACKEND para acesso à AI da OpenAi.

Este Front-End, como Cenário secundário e complementar busca informações via uso de 4 rotas GET na API da OpenAI (ChatGPT), agregando informações  sobre:
    1) As características impactantes do automóvel
    2) O valor de mercado médio na região recuperada via pesquisa do cep 
    3) O valor de seguro anual para o automóvel na região recuperada via pesquisa do CEP.
    4) Caracteristicas da região envolvendo a Cidade , o bairro e o logradouro da região recuperada via pesquisa do CEP

Este projeto valida o conceito de que é possível enriquecer dados a partir do uso de APIS e Inteligência Artificial. Será de grande importância, pois me apoiará a planejae e desenvolver um serviço de busca de dados e enriquecimento de informações associadas ao Business de Petroleo e Gás, cuja demanda e carência de informações é muito grande.

O MVP contempla o cadastro e recuperação de  atributos vinculados a um automóvel, Regiao pesquisada via CEP e Resultado da Busca de informações complementares na API da OpenAI.


---
## Como executar 

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.


É NECESSÁRIA A UTILIZAÇÃO DA CHAVE DE ACESSO A API DA OPENAI - Para o funcionamento, é necessário o uso de uma chave de acesso que criei para integração com a AI da OpenAI. A chave foi enviada no corpo do texto do formulário de entrega do trabalho e deve ser colocada no início do código fonte da app.py específicamente na linha 17:
######################################################################################################################
##CHAVE DA OPEN AI UTILIZADA PARA A BUSCA (Aqui deve ser colocada a chave passada na entrega do trabalho) ############
######################################################################################################################

chaveOpenAI = "CHAVE_DA_OPENAI"

Uma vez informada, todas as rotas passam a utilizar a chave.


------------------------------------------------------------------------------------------------------------------------------
## Como executar 

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.


## ---Docker ----------------------------------------------------------------------------------------------------------
##
--
## Como executar através do Docker

Certifique-se de ter o [Docker](https://docs.docker.com/engine/install/) instalado e em execução em sua máquina.

Navegue até o diretório que contém o Dockerfile e o requirements.txt no terminal.
Execute **como administrador** o seguinte comando para construir a imagem Docker:

```
$ docker build -t rest-api .
```

Uma vez criada a imagem, para executar o container basta executar, **como administrador**, seguinte o comando:

```
$ docker run -p 5001:5001 rest-api
```

## Utilizando o BackEnd
Após a instalação, as rotas e endpoints são disponibilizados na OpenAPI/Swagger para utilização de acordo com a documentação disponível no site.
#######IMPORTANTE: COMO JÁ TEMOS O BACK-END DE ARMAZENAMENTO UTILIZANDO A PORTA 5000, PARA ESTE SERVIÇO O FRONTEND UTILIZARÁ A PORTA 5001. ESTA PORTA JÁ FOI DEVIDAMENTE AJUSTADA NO DOCKERFILE.
Uma vez executando, para acessar a API, basta abrir o [http://localhost:5001/#/](http://localhost:5001/#/) no navegador.





### Alguns comandos úteis do Docker

>**Para verificar se a imagem foi criada** você pode executar o seguinte comando:
>
>```
>$ docker images
>```
>
> Caso queira **remover uma imagem**, basta executar o comando:
>```
>$ docker rmi <IMAGE ID>
>```
>Subistituindo o `IMAGE ID` pelo código da imagem
>
>**Para verificar se o container está em exceução** você pode executar o seguinte comando:
>
>```
>$ docker container ls --all
>```
>
> Caso queira **parar um conatiner**, basta executar o comando:
>```
>$ docker stop <CONTAINER ID>
>```
>Subistituindo o `CONTAINER ID` pelo ID do conatiner
>
>
> Caso queira **destruir um conatiner**, basta executar o comando:
>```
>$ docker rm <CONTAINER ID>
>```
>Para mais comandos, veja a [documentação do docker](https://docs.docker.com/engine/reference/run/).



