import socket
import datetime
import os

# Obter o endereço IPv4 da máquina
ipv4_address = socket.gethostbyname(socket.gethostname())

# Obter a data e hora atual
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Criar o conteúdo a ser gravado no bloco de notas
note_content = f" Endereço IPv4:{ipv4_address}\nData e Hora: {current_time}"

# Nome do arquivo do bloco de notas
file_name = "servidor_ip.txt"

# Caminho completo para a pasta onde o script está localizado
script_folder = os.path.dirname(os.path.abspath(__file__))

# Caminho completo para o arquivo de bloco de notas
file_path = os.path.join(script_folder, file_name)

# Gravar o conteúdo no bloco de notas
with open(file_path, "w") as file:
    file.write(note_content)

print(f"Endereço IPv4 ({ipv4_address}) foi gravado no arquivo {file_name}")
