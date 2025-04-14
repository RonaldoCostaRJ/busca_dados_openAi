#Última alteração: 06/07/2024 por: Ronaldo Ramos da Costa
#######################################################################
# importação do BaseModelo a partir do pydantic
from pydantic import BaseModel

#classe de tratamento de erro de Schema
class ErrorSchema(BaseModel):
    """ Define como uma mensagem de erro será representada
    """
    mesage: str
