################ IMPORTS ################
from estrutura_arquivos_py.instal_lib import *
instalar_bibliotecas()
from estrutura_arquivos_py.config import *
from estrutura_arquivos_py.readBotID import *
from estrutura_arquivos_py.screnshot import *
from estrutura_arquivos_py.killprocess import *
from rpa_hypercoe import Function
##########################################

## Inserir fluxo de processamento do robô dentro do try:
try:
    kill_process() #Função para fechar processos que foram inseridos no config
    Function.Start_Status(path)
    Function.Iteration(path)
    message = "Inicio Processamento bot"
    Function.Log(message,path)

    # Desenvolver o código a partir dessa etapa






# Registro de log de erro/exceção do bot em caso de erro no processamento
except Exception as erro:
    print(f"Erro API Status: ", erro) 
    message = f"Falha no processamento, erro: {erro}"
    Function.Log_Error(message,path)
    #Oberter captura da tela através da função para inserir no log de registro para os casos de falha
    CAMINHO_ARQUIVO = save_screenshot()
    pathfile = CAMINHO_ARQUIVO #Caminho absoluto do arquivo
    Function.Log_Attaching_File (message,pathfile,path)
    
finally:
    kill_process() #Função para fechar processos que foram setados no config
    message = "Fim Processamento do bot"
    Function.End_Log (message,path)
    Function.End_Status(path)