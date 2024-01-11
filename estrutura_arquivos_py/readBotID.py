################ IMPORTS ################
import os
##########################################

def getBotID():
    #Obtenha o diretório do arquivo
    try:
        CAMINHO_ARQUIVO = fr"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}\botId.txt"
        with open(CAMINHO_ARQUIVO, 'r') as arquivo:
            BOT_ID = arquivo.read()
            return BOT_ID
    except Exception as erro:
        print('Erro na etapa de leitura do botId.txt')
        raise Exception('Erro na etapa de leitura do botId.txt')