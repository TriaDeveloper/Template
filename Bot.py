################ IMPORTS ################
from estrutura_arquivos_py.config import *
from estrutura_arquivos_py.screnshot import *
from rpa_hypercoe_log import Funcao
##########################################

#Chamada API para Alterar o Status do Bot
BOT_ID = '<Inserir ID do Bot gerado pelo Portal HyperCoe>'
ClientToken = '<Inserir token gerado pelo Portal HyperCoe>'
BOT_Status = 1 # Active=0, Running=1, Paused=2, Error=3
Chamada_API_Status = Funcao.Status(BOT_Status,ClientToken,BOT_ID)

#Chamada API para Captura da IterationID
ID_Iteration = Funcao.Iteration(BOT_ID,ClientToken)

## Inserir fluxo de processamento do robô dentro do try:
try:
    #Chamada API de LOG
    level = 0 # Level - info=0, warn=1, error=2
    typeError = ""
    message = "Inicio Processamento bot"
    pathfile = "" #Caminho absoluto do arquivo
    finalLog = False
    Chamada_API_Log = Funcao.Log(level,typeError,message,pathfile,ID_Iteration,finalLog,ClientToken)
    # Inserir código de processamento a partir dessa etapa




# Registro de log de erro/exceção do bot em caso de erro no processamento
except Exception as erro:
    print(f"Erro API Status: ", erro) 
    #Chamada API de LOG
    level = 2 # Level - info=0, warn=1, error=2
    typeError = "Business Exception"
    message = "Cadastro cambio no Sistema SAP realizado com falha"
    #Oberter captura da tela através da função para inserir no log de registro para os casos de falha
    CAMINHO_ARQUIVO = save_screenshot()
    pathfile = CAMINHO_ARQUIVO #Caminho absoluto do arquivo
    finalLog = False
    Chamada_API_Log = Funcao.Log(level,typeError,message,pathfile,ID_Iteration,finalLog,ClientToken)
        
        
### Não alterar os campos abaixo
# Etapa de encerramento padrão do bot
#Chamada API de LOG
level = 0 # Level - info=0, warn=1, error=2
typeError = ""
message = "Fim Processamento do bot"
pathfile = "" #Caminho absoluto do arquivo (caso deseja enviar evidência no log)
finalLog = True # Nessa etapa final do processo o parametro deverá ser True
Chamada_API_Log = Funcao.Log(level,typeError,message,pathfile,ID_Iteration,finalLog,ClientToken)

#Chamada API para Alterar o Status do Bot
BOT_Status = 0 # Active=0, Running=1, Paused=2, Error=3
Chamada_API_Status = Funcao.Status(BOT_Status,ClientToken,BOT_ID)