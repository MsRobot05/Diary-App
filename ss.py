import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog

# --- Secret mapping (letter-based) ---
letter_map = {
    'a':'Δ', 'b':'β', 'c':'Ψ', 'd':'δ', 'e':'ε',
    'f':'φ','g':'γ','h':'η','i':'ι','j':'ϑ','k':'κ',
    'l':'λ','m':'μ','n':'ν','o':'ο','p':'π','q':'θ',
    'r':'ρ','s':'σ','t':'τ','u':'υ','v':'ν','w':'ω',
    'x':'χ','y':'ψ','z':'ζ',' ':' '
}

original_text = ""

# --- Functions ---
def on_key(event):
    global original_text
    char = event.char
    if char.isalpha() or char==' ' or char=='\n':
        original_text += char
        coded_char = letter_map.get(char.lower(), char)
        text_widget.insert(tk.INSERT, coded_char)
        return "break"

def toggle_view():
    global original_text
    text_widget.delete("1.0", tk.END)
    if toggle_btn.config('text')[-1] == 'Show Original':
        text_widget.insert(tk.END, original_text)
        toggle_btn.config(text='Show Coded')
    else:
        coded = ''.join(letter_map.get(c.lower(), c) for c in original_text)
        text_widget.insert(tk.END, coded)
        toggle_btn.config(text='Show Original')

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(original_text)
    root.update()
    messagebox.showinfo("Copied", "Original text copied to clipboard!")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files","*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(original_text)
        messagebox.showinfo("Saved", f"Diary saved to {file_path}")

def load_file():
    global original_text
    file_path = filedialog.askopenfilename(filetypes=[("Text files","*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            original_text = f.read()
        # show coded view by default
        coded = ''.join(letter_map.get(c.lower(), c) for c in original_text)
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, coded)
        toggle_btn.config(text="Show Original")
        messagebox.showinfo("Loaded", f"Diary loaded from {file_path}")

# --- GUI ---
root = tk.Tk()
root.title("Secret Diary")

text_widget = scrolledtext.ScrolledText(root, width=80, height=25, wrap=tk.WORD)
text_widget.pack(padx=10, pady=10)

toggle_btn = tk.Button(root, text="Show Original", command=toggle_view)
toggle_btn.pack(pady=5)

copy_btn = tk.Button(root, text="Copy Original Text", command=copy_to_clipboard)
copy_btn.pack(pady=5)

save_btn = tk.Button(root, text="Save Diary", command=save_file)
save_btn.pack(pady=5)

load_btn = tk.Button(root, text="Load Diary", command=load_file)
load_btn.pack(pady=5)

text_widget.bind("<Key>", on_key)

root.mainloop()