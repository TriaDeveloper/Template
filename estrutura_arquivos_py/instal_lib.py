import subprocess
import importlib
from estrutura_arquivos_py.config import *

def instalar_bibliotecas():
    for biblioteca in bibliotecas:
        try:
            importlib.import_module(biblioteca)
        except ImportError:
            subprocess.check_call(["pip", "install", biblioteca])
            

#if __name__ == "__main__":
    #bibliotecas_para_instalar = ["requests", "psutil", "pyautogui","rpa_hypercoe_log"]
    #instalar_bibliotecas(bibliotecas_para_instalar)




