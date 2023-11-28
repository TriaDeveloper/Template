from PIL import ImageGrab

caminho_arquivo = r"C:\BotCity - Projetos\BOT_TAXA_DOLAR\Rpa_Taxa_Dolar\taxa_cambial_dolar\bot_taxas_dolar\bot_taxas_dolar\Prints\print.png"

def salvar_screenshot(caminho_arquivo):
    # Captura a tela inteira
    imagem = ImageGrab.grab()

    # Salva a imagem no caminho especificado
    imagem.save(caminho_arquivo)

    return caminho_arquivo