import os

def obter_caminho_arquivo(pasta):
    # Verificar se a pasta existe
    if not os.path.exists(pasta):
        print(f"A pasta '{pasta}' não existe.")
        return None
    
    # Listar todos os arquivos na pasta
    arquivos = os.listdir(pasta)

    # Verificar se há apenas um arquivo
    if len(arquivos) != 1:
        print(f"A pasta '{pasta}' não contém um único arquivo.")
        return None

    # Obter o caminho completo do arquivo
    caminho_arquivo = os.path.join(pasta, arquivos[0])
    return caminho_arquivo

def excluir_arquivo(caminho_arquivo):
    # Verificar se o arquivo existe
    if not os.path.exists(caminho_arquivo):
        print(f"O arquivo '{caminho_arquivo}' não existe.")
        return
    
    # Excluir o arquivo
    try:
        os.remove(caminho_arquivo)
        print(f"O arquivo '{caminho_arquivo}' foi excluído com sucesso.")
    except OSError as e:
        print(f"Erro ao excluir o arquivo '{caminho_arquivo}': {str(e)}")
