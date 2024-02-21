import os

## Inserir registros de configuração do Bot


# Alterar o Kill Process de acordo o processo que deverá ser encerrado
Kill_Process = {'EXCEL.EXE','firefox.exe'}

# Não alterar os parâmetros abaixo
bibliotecas = ["requests", "psutil", "pyautogui","rpa-hypercoe","jsonpickle"]
path = fr"{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}\config.txt"