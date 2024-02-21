import os

## Inserir registros de configuração do Bot

#TOKEN API HYPERCOE
ClientToken = '<Capturar token gerado pelo portal HyperCoe no painel do usuário>'
Kill_Process = {'EXCEL.EXE','firefox.exe'}
bibliotecas = ["requests", "psutil", "pyautogui","rpa-hypercoe"]
path = fr"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}\config.txt"