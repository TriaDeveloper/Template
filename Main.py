
################ IMPORTS ################
from estrutura_arquivos_py.config import *
from botcity.core import DesktopBot
from estrutura_arquivos_py.envio_email_outlook import *
from estrutura_arquivos_py.mensagem_resposta import *
from estrutura_arquivos_py.authentication import Authentication as Auth
from estrutura_arquivos_py.api_banco_centrtal_dollar import *
from estrutura_arquivos_py.api_hypercoe import *
import pyautogui
##########################################

#Chamada API para Alterar o Status do Bot
BOT_Status = 1 # Active=0, Running=1, Paused=2, Error=3
Chamada_API_Status = ApiHyperCoe.API_Status(BOT_Status)

#Chamada API para Captura da IterationID
ID_Iteration = ApiHyperCoe.API_Iteration()

#Chamada API de LOG
level = 0 # Level - info=0, warn=1, error=2
typeError = ""
message = "Inicio Processamento Robô Coleta Taxa Dolar"
pathfile = "" #Caminho absoluto do arquivo
finalLog = False
Chamada_API_Log = ApiHyperCoe.API_Log(level,typeError,message,pathfile,ID_Iteration,finalLog)


class Bot(DesktopBot):

    def action(self, execution=None):
        
        # Inseri dados de cotação em uma lista.
        oData =  ApiBancoCenrtal.retorna_payloads()
        
        #Chamada API de LOG
        level = 0 # Level - info=0, warn=1, error=2
        typeError = ""
        message = f"Cat G --- valor: {oData[0]['Ukurs']} / Cat B --- valor: {oData[1]['Ukurs']} / Cat M --- valor: {oData[2]['Ukurs']} / Cat P --- valor: {oData[3]['Ukurs']}"
        pathfile = "" #Caminho absoluto do arquivo
        finalLog = False
        Chamada_API_Log = ApiHyperCoe.API_Log(level,typeError,message,pathfile,ID_Iteration,finalLog)

        # Inserir dados no SAP Via Gateway 
        result_status_code = []
        for payload in oData:
            result_status_code.append(Auth(url, endpoint, USER_SAP, PASSWORD_SAP).post(payload=payload))            
        
        #Chamada API de LOG
        level = 0 # Level - info=0, warn=1, error=2
        typeError = ""
        message = "Cadastro cambio no Sistema SAP"
        pathfile = "" #Caminho absoluto do arquivo
        finalLog = False
        Chamada_API_Log = ApiHyperCoe.API_Log(level,typeError,message,pathfile,ID_Iteration,finalLog)

        # Tira foto da área de trabalho.
        pyautogui.screenshot(CAMINHO_ARQUIVO)
        
        # Enviando E-mail.
        if result_status_code[0] == 201:
            
            #Chamada API de LOG
            level = 0 # Level - info=0, warn=1, error=2
            typeError = ""
            message = "Cadastro cambio no Sistema SAP realizado com sucesso"
            pathfile = CAMINHO_ARQUIVO #Caminho absoluto do arquivo
            finalLog = False
            Chamada_API_Log = ApiHyperCoe.API_Log(level,typeError,message,pathfile,ID_Iteration,finalLog)
            
            mensagem =  Mensagem(result_status_code[1], result_status_code).mensagem_sucesso()
        else:
            #Chamada API de LOG
            level = 2 # Level - info=0, warn=1, error=2
            typeError = "Business Exception"
            message = "Cadastro cambio no Sistema SAP realizado com falha"
            pathfile = CAMINHO_ARQUIVO #Caminho absoluto do arquivo
            finalLog = False
            Chamada_API_Log = ApiHyperCoe.API_Log(level,typeError,message,pathfile,ID_Iteration,finalLog)

            mensagem = Mensagem(result_status_code[0], result_status_code).mensagem_erro()            
        
        caminhos_anexos = CAMINHOS_ANEXOS_SUCESSO 
        enviar_email = SendEmail(TO= DESTINATARIOS_EMAIL,
                                assunto=Mensagem.assunto_email(ambiente),
                                caminhos_anexos=caminhos_anexos,
                                mensagem=mensagem)
        print(enviar_email)

    def not_found(self, label):
        print(f"Element not found: {label}")
    

if __name__ == '__main__':
    Bot.main()

#Chamada API de LOG
level = 0 # Level - info=0, warn=1, error=2
typeError = ""
message = "Fim Processamento Robô Coleta Taxa Dolar"
pathfile = "" #Caminho absoluto do arquivo
finalLog = True
Chamada_API_Log = ApiHyperCoe.API_Log(level,typeError,message,pathfile,ID_Iteration,finalLog)

#Chamada API para Alterar o Status do Bot
BOT_Status = 0 # Active=0, Running=1, Paused=2, Error=3
Chamada_API_Status = ApiHyperCoe.API_Status(BOT_Status)
