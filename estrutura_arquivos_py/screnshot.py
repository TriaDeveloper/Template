################ IMPORTS ################
from datetime import datetime
import os
import pyautogui
##########################################
def save_screenshot():
    # Obter diretorio local
    caminho_arquivo = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = f'{caminho_arquivo}\screnshots'

    # Validar se o diretórios existe
    if not os.path.exists(caminho_arquivo):
        # Criar diretótio
        os.makedirs(caminho_arquivo)

    # Concatenar no screnshot com time atual
    date = datetime.now().strftime("%d%m%Y_%H%M%S")
    nome_arquivo = f"screnshot{date}.png"
    # Caminho completo para o screnshots
    caminho_arquivo = os.path.join(caminho_arquivo, nome_arquivo)

    # Capturar Tela
    pyautogui.screenshot(caminho_arquivo)

    return caminho_arquivo