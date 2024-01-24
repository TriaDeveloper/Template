################ IMPORTS ################
import os
import json
##########################################

def getBotID():
    #Obtenha o diretório do arquivo
    try:
        CAMINHO_ARQUIVO = fr"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}\config.txt"
        with open(CAMINHO_ARQUIVO, 'r') as arquivo:
            Dados = arquivo.read()
            Dados_Json = json.loads(Dados)
            BOT_ID = Dados_Json['BotId']
            ClientToken = Dados_Json['ClientToken']
            Valores = {'BOT_ID': BOT_ID,
                     'ClientToken': ClientToken}
            return Valores
    except Exception as erro:
        print('Erro na etapa de leitura do botId.txt')
        raise Exception('Erro na etapa de leitura do botId.txt')