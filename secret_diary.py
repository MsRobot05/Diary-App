import tkinter as tk
from tkinter import messagebox
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

# --- Simple key from password ---
def get_key(password):
    return password.encode().ljust(32, b'0')[:32]  # AES-256 key

# --- Encrypt text ---
def encrypt_text(key, text):
    aesgcm = AESGCM(key)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, text.encode(), None)
    return nonce + ciphertext

# --- Decrypt text ---
def decrypt_text(key, data):
    aesgcm = AESGCM(key)
    nonce = data[:12]
    ciphertext = data[12:]
    return aesgcm.decrypt(nonce, ciphertext, None).decode()

# --- GUI ---
root = tk.Tk()
root.title("Secret Diary")

text_box = tk.Text(root, width=50, height=20)
text_box.pack()

# Save diary
def save_diary():
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Enter password")
        return
    key = get_key(password)
    content = text_box.get("1.0", tk.END)
    encrypted = encrypt_text(key, content)
    with open("diary.sec", "wb") as f:
        f.write(encrypted)
    messagebox.showinfo("Saved", "Diary saved encrypted!")

# Load diary
def load_diary():
    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Enter password")
        return
    key = get_key(password)
    try:
        with open("diary.sec", "rb") as f:
            data = f.read()
        decrypted = decrypt_text(key, data)
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, decrypted)
    except:
        messagebox.showerror("Error", "Wrong password or corrupt file")

# Password entry
password_entry = tk.Entry(root, show="*")
password_entry.pack()
password_entry.insert(0, "mypassword")  # default, optional

save_btn = tk.Button(root, text="Save Diary", command=save_diary)
save_btn.pack()
load_btn = tk.Button(root, text="Load Diary", command=load_diary)
load_btn.pack()

root.mainloop()