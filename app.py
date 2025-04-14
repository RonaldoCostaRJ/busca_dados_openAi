#Última alteração: 10/04/2025 por: Ronaldo Ramos da Costa
#######################################################################
##### importações necessárias para o funcionamento da API #############

from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
from schemas import *
from flask_cors import CORS
import openai


######################################################################################################################
##CHAVE DA OPEN AI UTILIZADA PARA A BUSCA (Aqui deve ser colocada a chave passada na entrega do trabalho) ############
######################################################################################################################

chaveOpenAI = 

######################################################################################################################
######################################################################################################################
######################################################################################################################
# NOME DA  API
info = Info(title=" Busca Metadados via IA (OpenIA) para Automóvel e Região", version="1.0.0")
#chamada a OpenAPI
app = OpenAPI(__name__, info=info)
CORS(app)

# definição das tags que serão utilizadas
home_tag = Tag(name="Documentação", description="Documentação: Swagger")
busca_tag = Tag(name="Metadados de automóvel e Região", description="Adição, visualização e remoção de um registro de busca por um automóvel na base")
#################################################################################################################
#redirecionamento para Open API
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, swagger, apresentando a tela que contém a documentação da API.
    """
    return redirect('/openapi/swagger#')
######################################################################################################################
######################################################################################################################
######################################################################################################################


##################################################################################################################
##################################################################################################################
########################### ENRIQUECIMENTO DE DADOS A PARTIR DA BUSCA NA OPENAI ##################################
##################################################################################################################
##################################################################################################################
####ROTAS DE BUSCA:
##################################################################################################################
#Busca na API da OPENAI 4 características Positivas do automóvel desejado a partir de uma pergunta "Request".   
@app.get('/bestcaracteristicasautomovel',responses={"200": Modelo_ChatGPT_ResponseSchema, "404": ErrorSchema}) # type: ignore
def get_bestcaracteristicasautomovel(query: Modelo_ChatGPT_ResponseSchema):
   

    
    client = openai.OpenAI(api_key=chaveOpenAI)
    response = client.responses.create(
    model="gpt-4o-mini",
    input=query.request
    )
   
    return response.output_text
##################################################################################################################
#Busca na API da OPENAI O valor médio do automóvel e ano, na região informada a partir de uma pergunta "Request".   
@app.get('/valormedionaregiao',responses={"200": Modelo_ChatGPT_ResponseSchema, "404": ErrorSchema}) # type: ignore
def get_valormedionaregiao(query: Modelo_ChatGPT_ResponseSchema):
   
    client = openai.OpenAI(api_key=chaveOpenAI)
    response = client.responses.create(
    model="gpt-4o-mini",
    input=query.request
    )
   
    return response.output_text
##################################################################################################################
#Busca na API da OPENAI O valor médio do Seguro anual para o automóvel e ano, na região informada a partir de uma pergunta "Request".   
@app.get('/valormedioseguroautonaregiao',responses={"200": Modelo_ChatGPT_ResponseSchema, "404": ErrorSchema}) # type: ignore
def get_valormedioseguroautonaregiao(query: Modelo_ChatGPT_ResponseSchema):
   
    client = openai.OpenAI(api_key=chaveOpenAI)
    response = client.responses.create(
    model="gpt-4o-mini",
    input=query.request
    )
  
    return response.output_text
##################################################################################################################
#Busca na API da OPENAI informações e características sobre a rua/bairro da região informada a partir de uma pergunta "Request".   
@app.get('/informacoesregiao',responses={"200": Modelo_ChatGPT_ResponseSchema, "404": ErrorSchema}) # type: ignore
def get_informacoesregiao(query: Modelo_ChatGPT_ResponseSchema):
   
    client = openai.OpenAI(api_key=chaveOpenAI)
    response = client.responses.create(
    model="gpt-4o-mini",
    input=query.request
    )
    return response.output_text
##################################################################################################################
##################################################################################################################
##################################################################################################################
##################################################################################################################
