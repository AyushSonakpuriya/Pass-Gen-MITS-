import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator (MITS)")
        self.root.geometry("520x620")
        self.root.resizable(False, False)

        self.current_theme = "light"
        self.colors = {
            "light_bg": "#f0f4f8",
            "dark_bg": "#222831",
            "light_fg": "#222831",
            "dark_fg": "#eeeeee",
            "button_light_bg": "#4a90e2",
            "button_dark_bg": "#30475e",
            "button_fg": "#ffffff",
            "accent": "#ff5722",
            "strength_weak": "#ff4d4d",
            "strength_moderate": "#ffb74d",
            "strength_strong": "#4caf50"
        }

        self.setup_ui()
        self.apply_theme()

    def setup_ui(self):
        self.canvas = tk.Canvas(self.root, width=520, height=620, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.circle1 = self.canvas.create_oval(-100, -100, 300, 300, fill="#ff7043", outline="")
        self.circle2 = self.canvas.create_oval(400, 450, 650, 700, fill="#4fc3f7", outline="")

        self.title_label = tk.Label(self.root, text="Password Generator", font=("Poppins", 26, "bold"))
        self.title_label.place(x=130, y=40)

        self.length_label = tk.Label(self.root, text="Password Length", font=("Poppins", 14))
        self.length_label.place(x=50, y=120)
        self.length_entry = tk.Entry(self.root, font=("Poppins", 14), width=5, justify='center')
        self.length_entry.insert(0, "12")
        self.length_entry.place(x=230, y=115)

        self.var_lower = tk.BooleanVar(value=True)
        self.var_upper = tk.BooleanVar(value=True)
        self.var_digits = tk.BooleanVar(value=True)
        self.var_symbols = tk.BooleanVar(value=False)

        self.chk_lower = tk.Checkbutton(self.root, text="Include Lowercase", font=("Poppins", 13), variable=self.var_lower)
        self.chk_lower.place(x=50, y=170)
        self.chk_upper = tk.Checkbutton(self.root, text="Include Uppercase", font=("Poppins", 13), variable=self.var_upper)
        self.chk_upper.place(x=50, y=210)
        self.chk_digits = tk.Checkbutton(self.root, text="Include Digits", font=("Poppins", 13), variable=self.var_digits)
        self.chk_digits.place(x=50, y=250)
        self.chk_symbols = tk.Checkbutton(self.root, text="Include Symbols", font=("Poppins", 13), variable=self.var_symbols)
        self.chk_symbols.place(x=50, y=290)

        self.generate_button = tk.Button(self.root, text="Generate Password", font=("Poppins", 14, "bold"),
                                         command=self.generate_password, bd=0, relief="ridge")
        self.generate_button.place(x=160, y=350, width=200, height=45)

        self.password_entry = tk.Entry(self.root, font=("Consolas", 16, "bold"), justify="center", bd=3, relief="sunken")
        self.password_entry.place(x=50, y=420, width=420, height=45)
        self.password_entry.configure(state="readonly")

        self.copy_button = tk.Button(self.root, text="Copy to Clipboard", font=("Poppins", 13),
                                     command=self.copy_password, bd=0, relief="ridge")
        self.copy_button.place(x=180, y=480, width=160, height=40)

        self.theme_button = tk.Button(self.root, text="Switch to Dark Mode", font=("Poppins", 10),
                                      command=self.toggle_theme, bd=0, relief="ridge")
        self.theme_button.place(x=360, y=580, width=150, height=30)

    def apply_theme(self):
        if self.current_theme == "light":
            bg = self.colors["light_bg"]
            fg = self.colors["light_fg"]
            btn_bg = self.colors["button_light_bg"]
            btn_fg = self.colors["button_fg"]
            circle1_color = "#ffccbc"
            circle2_color = "#b3e5fc"

            self.canvas.itemconfig(self.circle1, fill=circle1_color)
            self.canvas.itemconfig(self.circle2, fill=circle2_color)
            self.root.config(bg=bg)

        else:
            bg = self.colors["dark_bg"]
            fg = self.colors["dark_fg"]
            btn_bg = self.colors["button_dark_bg"]
            btn_fg = self.colors["button_fg"]
            circle1_color = "#bf360c"
            circle2_color = "#0288d1"

            self.canvas.itemconfig(self.circle1, fill=circle1_color)
            self.canvas.itemconfig(self.circle2, fill=circle2_color)
            self.root.config(bg=bg)

        widgets = [self.title_label, self.length_label,
                   self.chk_lower, self.chk_upper, self.chk_digits, self.chk_symbols]

        for widget in widgets:
            widget.config(bg=bg, fg=fg)

        entries = [self.length_entry, self.password_entry]
        for entry in entries:
            entry.config(bg="white" if self.current_theme == "light" else "#444444",
                         fg=fg, insertbackground=fg)

        buttons = [self.generate_button, self.copy_button, self.theme_button]
        for btn in buttons:
            btn.config(bg=btn_bg, fg=btn_fg,
                       activebackground=self.colors["accent"],
                       activeforeground="white")

        for chk in [self.chk_lower, self.chk_upper, self.chk_digits, self.chk_symbols]:
            chk.config(selectcolor=bg)

    def toggle_theme(self):
        self.current_theme = "dark" if self.current_theme == "light" else "light"
        self.theme_button.config(text="Switch to Light Mode" if self.current_theme == "dark" else "Switch to Dark Mode")
        self.apply_theme()

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for password length.")
            return

        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4.")
            return

        options = ''
        if self.var_lower.get():
            options += string.ascii_lowercase
        if self.var_upper.get():
            options += string.ascii_uppercase
        if self.var_digits.get():
            options += string.digits
        if self.var_symbols.get():
            options += string.punctuation

        if not options:
            messagebox.showerror("Error", "Select at least one character type.")
            return

        password = ''.join(random.choice(options) for _ in range(length))

        self.password_entry.config(state="normal")
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        self.password_entry.config(state="readonly")

    def copy_password(self):
        password = self.password_entry.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password to copy!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
git 