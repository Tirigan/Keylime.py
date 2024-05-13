INGREDIENTS.PY

from cryptography.fernet import Fernet

with open('encryption_key.txt', 'rb') as f:
    encryption_key = f.read()

cipher_suite = Fernet(encryption_key)

with open('encrypted_keystrokes', 'rb') as f:
    encrypted_data = f.read()

decrypted_data = cipher_suite.decrypt(encrypted_data)

with open('decrypted_keystrokes.txt', 'wb') as f:
    f.write(decrypted_data)
