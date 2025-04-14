
from pydantic import BaseModel
#Última alteração: 10/04/2025 por: Ronaldo Ramos da Costa
#####     Definição dos schemas utilizados na API    ##################
#######################################################################
class Modelo_ChatGPT_ResponseSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a pesquisa de uma busca, feita com base no nome do Modelo do automóvel.
    """
    request : str = "Solicitação à API da OpenAI"
    #resposta  : str = "Mensagem Retornada da API da OpenAI"


