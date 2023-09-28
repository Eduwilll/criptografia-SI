import hashlib
import crcmod.predefined
import os
from tkinter import *
from tkinter import ttk
import base64
from tkinter import filedialog as fd
import webbrowser

class Application:
    def __init__(self):
        self.root = root
        self.Criptografia = Criptografia(self)
        self.tela()
        root.mainloop()

    def tela(self):
        self.root.title("Criptografia")
        self.ferramentas()
        self.root.configure(bg="#adc2da", padx=100, pady=100)
        self.dimension()

        # create a notebook
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        # create tabs
        self.tab1 = Frame(self.notebook)
        self.tab2 = Frame(self.notebook)


        # add tabs to notebook
        self.notebook.add(self.tab1, text='Criptigrafia de Texto- Base64')
        self.notebook.add(self.tab2, text='Checksum')


        # set current tab
        self.notebook.select(self.tab1)

        self.contents()

    @staticmethod
    def ferramentas():
        # cria a barra de ferramentas
        toolbar = Menu(root)

        def open_file():
            print("Opening file...")
            filetypes = (
                ('Text files', '*.txt'),
                ('All files', '*.*')
            )
            fd.askopenfile(filetypes=filetypes)

        def show_about_dialog():
            about_window = Toplevel(root)
            about_window.title("Sobre")
            about_window.geometry("400x200")
            about_window.resizable(False, False)

            # calculate x and y coordinates for the 'about window'
            x = int((root.winfo_screenwidth() / 2) - (400 / 2))
            y = int((root.winfo_screenheight() / 2) - (200 / 2))
            about_window.geometry(f"+{x}+{y}")

            Label(about_window, text="Criptografia v1.0", font=("Arial", 16)).pack(pady=20)
            Label(about_window,
                  text="Este programa foi desenvolvido por Eduwill!",
                  font=("Arial", 12)).pack()
            # Add a link to a website
            link = Label(about_window, text="Visite o meu GitHub!", font=("Arial", 16), fg="blue", cursor="hand2")
            link.pack()
            link.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/Eduwilll"))

        # cria o menu "Arquivo"
        file_menu = Menu(toolbar, tearoff=0)
        file_menu.add_command(label="Novo")
        file_menu.add_command(label="Abrir", command=open_file)
        file_menu.add_command(label="Salvar", command="save_file")
        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=root.quit)
        toolbar.add_cascade(label="Arquivo", menu=file_menu)

        # cria o menu "Ajuda"
        help_menu = Menu(toolbar, tearoff=0)
        help_menu.add_command(label="Sobre", command=show_about_dialog)
        toolbar.add_cascade(label="Ajuda", menu=help_menu)

        # adiciona a barra de ferramentas à janela principal
        root.config(menu=toolbar)

    @staticmethod
    def dimension():
        # get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # calculate x and y coordinates for the Tk root window
        x = int((screen_width / 2) - (750 / 2))
        y = int((screen_height / 2) - (550 / 2))

        # set the dimensions of the screen
        root.geometry(f"750x550+{x}+{y}")

    def contents(self):

        # criar as caixas de entrada e saída
        message_label = Label(self.tab1, text="Mensagem:")
        message_label.grid(row=0, column=0, padx=10, pady=10, sticky=E)
        self.message_entry = Entry(self.tab1)
        self.message_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W + E, ipadx=50)

        encrypted_label = Label(self.tab1, text="Mensagem Criptografada:")
        encrypted_label.grid(row=1, column=0, padx=10, pady=10, sticky=E)
        self.encrypted_entry = Entry(self.tab1)
        self.encrypted_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W + E, ipadx=50)

        # criar as caixas para o resultado da criptografia
        result_label = Label(self.tab1, text="Resultado da Criptografia:")
        result_label.grid(row=4, column=0, padx=10, pady=10, sticky=E)
        self.result_entry = Entry(self.tab1, justify='center', fg="blue")
        self.result_entry.grid(row=4, column=1, padx=10, pady=10, sticky=W + E, ipadx=50, ipady=20)
        self.result_entry.config(font=("Arial", 17))

        # criar os botões de criptografia e descriptografia
        encrypt_button = Button(self.tab1, text="Criptografar", command=self.Criptografia.encryptBase64)
        encrypt_button.grid(row=3, column=0, padx=10, pady=10, sticky=W + E, ipadx=50)

        decrypt_button = Button(self.tab1, text="Descriptografar", command=self.Criptografia.decryptBase64)
        decrypt_button.grid(row=3, column=1, padx=10, pady=10, sticky=W + E, ipadx=50)

        # centralizar todos os widgets
        self.tab1.grid_columnconfigure(0, weight=1)
        self.tab1.grid_columnconfigure(1, weight=1)
        self.tab1.grid_columnconfigure(4, weight=1)
        self.tab1.grid_columnconfigure(3, weight=1)

        #tab 2 contents
        def open_file():
            filetypes = (
                ('Text files', '*.txt'),
                ('All files', '*.*')
            )
            file_path = fd.askopenfilename(filetypes=filetypes)
            if file_path:
                # Extract the file name from the path
                file_name = os.path.basename(file_path)
                file_label.config(text=f"Selected File: {file_name}")

                # Calculate checksums
                calculate_checksums(file_path)

        def calculate_checksums(file_path):

            # Calculate MD5 checksum
            md5 = calculate_md5(file_path)
            md5_label.config(text=f"MD5: {md5}")

            # Calculate SHA-1 checksum
            sha1 = calculate_sha1(file_path)
            sha1_label.config(text=f"SHA-1: {sha1}")

            # Calculate SHA-256 checksum
            sha256 = calculate_sha256(file_path)
            sha256_label.config(text=f"SHA-256: {sha256}")

        def calculate_md5(file_path):
            hash_md5 = hashlib.md5()
            with open(file_path, 'rb') as file:
                for chunk in iter(lambda: file.read(4096), b''):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()

        def calculate_sha1(file_path):
            hash_sha1 = hashlib.sha1()
            with open(file_path, 'rb') as file:
                for chunk in iter(lambda: file.read(4096), b''):
                    hash_sha1.update(chunk)
            return hash_sha1.hexdigest()

        def calculate_sha256(file_path):
            hash_sha256 = hashlib.sha256()
            with open(file_path, 'rb') as file:
                for chunk in iter(lambda: file.read(4096), b''):
                    hash_sha256.update(chunk)
            return hash_sha256.hexdigest()

        checksum_button = Button(self.tab2, text="Open File", command=open_file)
        checksum_button.grid(row=1, column=0, padx=10, pady=10, sticky=W + E, ipadx=50)

        file_label = Label(self.tab2, text="Selected File: ")
        file_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        md5_label = Label(self.tab2, text="MD5: ")
        md5_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        sha1_label = Label(self.tab2, text="SHA-1: ")
        sha1_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        sha256_label = Label(self.tab2, text="SHA-256: ")
        sha256_label.grid(row=5, column=0, padx=5, pady=5, sticky=W)

class Criptografia:

    def __init__(self, app):
        self.app = app
    # função para criptografar uma mensagem

    def encryptBase64(self):

        message = self.app.message_entry.get().encode()
        message = base64.b64encode(message)
        self.app.result_entry.delete(0, END)
        self.app.result_entry.insert(0, message.decode())
        self.app.message_entry.delete(0, END)
        # messagebox.showinfo("Information", "Informative message")

    # função para descriptografar uma mensagem
    def decryptBase64(self):
        message = self.app.encrypted_entry.get().encode()
        message = base64.b64decode(message)
        self.app.result_entry.delete(0, END)
        self.app.result_entry.insert(0, message.decode())
        self.app.encrypted_entry.delete(0, END)


if __name__ == "__main__":
    # criar a janela principal
    root = Tk()
    # executar a janela principal
    Application()
