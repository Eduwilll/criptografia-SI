from tkinter import *
import base64

# criar a janela principal
root = Tk()


class Application():
    def __init__(self):
        self.root = root
        self.tela()
        root.mainloop()
    def tela(self):
        self.root.title("Criptografia")
        self.root.configure(bg="#adc2da",padx=1)
        self.dimension()
        self.contents()
    def dimension(self):
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
        message_label = Label(root, text="Mensagem:")
        message_label.grid(row=0, column=0)
        message_entry = Entry(root)
        message_entry.grid(row=0, column=1)

        encrypted_label = Label(root, text="Mensagem Criptografada:")
        encrypted_label.grid(row=1, column=0)
        encrypted_entry = Entry(root)
        encrypted_entry.grid(row=1, column=1)

        # criar os botões de criptografia e descriptografia
        encrypt_button = Button(root, text="Criptografar", command=cryptograf.encryptBase64)
        encrypt_button.grid(row=2, column=0)

        decrypt_button = Button(root, text="Descriptografar", command=cryptograf.decryptBase64)
        decrypt_button.grid(row=2, column=1)
class cryptograf(Application):
    def __init__(self):
        self.contents = Application()
    # função para criptografar uma mensagem
    def encryptBase64(self):

        message = self.contents.message_entry.get().encode()
        message = base64.b64encode(message)
        self.contents.encrypted_entry.delete(0, END)
        self.contents.encrypted_entry.insert(0, message.decode())

    # função para descriptografar uma mensagem
    def decryptBase64(self):
        message = self.contents.encrypted_entry.get().encode()
        message = base64.b64decode(message)
        self.contents.message_entry.delete(0, END)
        self.contents.message_entry.insert(0, message.decode())


# executar a janela principal
Application()
