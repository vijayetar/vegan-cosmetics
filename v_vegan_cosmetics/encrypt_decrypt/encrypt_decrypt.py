from cryptography.fernet import Fernet

def encrypt_password(str_pwd):
  #get key from the file
  file = open('key.key','rb')
  key = file.read()
  file.close()

  #encode the password to binary
  encoded = str_pwd.encode()

  #encrypt the password
  f = Fernet(key)
  e_pwd = f.encrypt(encoded)

  #decode it to string format
  decoded_e_pwd = e_pwd.decode()
  return decoded_e_pwd

def decrypt_password(decoded_e_pwd):
  #get the key from the file
  file = open('key.key','rb')
  key = file.read()
  file.close()

  #encode pwd into binary format
  e_pwd = decoded_e_pwd.encode()

  #decrypt the binary pwd
  f= Fernet(key)
  d_pwd = f.decrypt(e_pwd)

  #decode it to the string format
  str_pwd = d_pwd.decode()
  return str_pwd