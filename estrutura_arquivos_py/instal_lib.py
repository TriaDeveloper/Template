import subprocess
import importlib
from estrutura_arquivos_py.config import *

def instalar_bibliotecas():
    for biblioteca in bibliotecas:
        try:
            importlib.import_module(biblioteca)
            print(f'A biblioteca {biblioteca} já está instalada.')
        except ImportError:
            print(f'Instalando a biblioteca {biblioteca}...')
            subprocess.check_call(["pip", "install", biblioteca])
            print(f'Biblioteca {biblioteca} instalada com sucesso.')

#if __name__ == "__main__":
    #bibliotecas_para_instalar = ["requests", "psutil", "pyautogui","rpa_hypercoe_log"]
    #instalar_bibliotecas(bibliotecas_para_instalar)




