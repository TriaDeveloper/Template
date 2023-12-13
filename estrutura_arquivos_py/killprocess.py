################ IMPORTS ################
import psutil
from estrutura_arquivos_py.config import *
##########################################

#Fechar processos
def kill_process():
    for item in Kill_Process:
        for proc in psutil.process_iter(['pid', 'name']):
            if item.lower() in proc.info['name'].lower():
                try:
                    p = psutil.Process(proc.info['pid'])
                    p.terminate()
                    print(f'Fechar: {item}')
                except Exception as e:
                    print(f"Erro ao tentar fechar o processo {item}: {e}")