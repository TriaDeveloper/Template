import subprocess

def install_dependencies():
    # Caminho para o arquivo requirements.txt
    requirements_file = 'requirements.txt'

    # Comando para instalar as dependências
    install_command = ['pip', 'install', '-r', requirements_file]

    # Executar o comando para instalar as dependências
    subprocess.call(install_command)

if __name__ == "__main__":
    install_dependencies()
