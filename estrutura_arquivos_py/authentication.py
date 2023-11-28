
import requests
# from authentication import *
from estrutura_arquivos_py.config import *

class Authentication:
    def __init__(self, url, endpoint, user, password):
        self._url = url
        self._endpoint = endpoint
        self._user = user
        self._password = password     
     
    def __get_tokken(self) -> list:
        try:
            httpHEAD = requests.head(url + endpoint, headers={"x-csrf-token": "fetch"}, auth=(self._user, self._password))
            token = httpHEAD.headers.get("x-csrf-token")
            set_cookie = httpHEAD.headers.get("set-cookie")
            mandt = set_cookie[0:30]
            sectionID = set_cookie[40:110]
            status_code = httpHEAD.status_code 
            
            resultadoPayloadGet = {
                "authorization": "Basic " + self._user + ":" + self._password,
                "Cookie": sectionID + mandt,
                "Content-Type": "application/json",
                "x-csrf-token": token
            }
            
        except Exception as error:
            resultadoPayloadGet = error            
        finally:
            listData = [resultadoPayloadGet, status_code]
            print('Status Code Head ' + str(status_code))
        return listData
    
    def post(self, payload):
        result_list = self.__get_tokken()
        if result_list[1] == 200: 
            httpPOST = requests.post(self._url + self._endpoint, auth=(self._user, self._password), headers=result_list[0], json=payload)
            get_sap_message = httpPOST.headers.get('sap-message')
            rf = get_sap_message.find('</message>')
            ri = get_sap_message.find('<message>') + len('<message>')
            
            if httpPOST.status_code == 201:
                status_code = httpPOST.status_code
                message = get_sap_message[ri:rf]
                print(f'Status code {httpPOST.status_code}. {get_sap_message[ri:rf]}')   
            else:       
                status_code = httpPOST.status_code
                message = 'Erro de comunicação.'
                print(f'{message}. Status code {status_code}.')      
        else:            
            status_code = result_list[1]
            message = 'Erro de comunicação.'
            print(f'Erro de autenticação. Status code {result_list[1]}.')
        return [status_code, message, payload]
    
    
        