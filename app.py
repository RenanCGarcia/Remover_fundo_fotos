import customtkinter as ctk
from tkinter import *
import tkinter as tk
from rembg import remove
from PIL import Image
import os


class Functions():
    def center_window(self, window, h, w):
        height = h
        width = w

        height_window = window.winfo_screenheight()
        width_window = window.winfo_screenwidth()

        x = (width_window - height) // 2
        y = (height_window - width) // 2

        position = f"{height}x{width}+{x}+{y}"
        window.geometry(position)

class App(Functions):
    def __init__(self):
        self.window = ctk.CTk()
        self.window_Properties()
        self.main_Frame()

    def window_Properties(self):
        # Título da tela
        self.window.title('Removedor de fundos')
        # Não permite que mude o tamanho da tela
        self.window.resizable(width=False, height=False)
        # Determina o tamanho da tela, e inicia ela no meio
        self.center_window(self.window, 800, 200)

    def main_Frame(self):
        # Criação do frame principal
        self.main_frame = ctk.CTkFrame(master=self.window)
        self.main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Botão de selecionar imagem
        self.btn_select_IMG = ctk.CTkButton(master=self.main_frame, text="Selecionar Imagem", command=self.select_IMG)
        self.btn_select_IMG.place(relx=0.1, rely=0.30)

        # Botão de remover fundo da imagem
        self.btn_remove_background = ctk.CTkButton(master=self.main_frame, text="Remover fundo", command=self.remove_background)
        self.btn_remove_background.place(relx=0.725, rely=0.30)

    def select_IMG(self):
        # Abre a tela de selecionar diretório
        self.diretory_IMG = ctk.filedialog.askopenfilename()
        # Separa o diretório do nome da Imagem
        for pos in range(len(self.diretory_IMG) -1, -1, -1):
            if self.diretory_IMG[pos] == "/":
                self.diretory = self.diretory_IMG[:pos]
                self.name = self.diretory_IMG[pos + 1:]
                break
        # Pega o nome da imagem sem a extenção do arquivo
        for pos in range(len(self.name) -1, -1, -1):
            if self.name[pos] == ".":
                self.name = self.name[:pos]
                break
        # Box que mostra o diretório da imagem selecionada
        self.diretory_box = ctk.CTkEntry(master=self.main_frame, placeholder_text=f"{self.diretory_IMG}")
        self.diretory_box.place(relx=0.1, rely=0.1, relwidth=0.8)

    def remove_background(self):
        img = Image.open(self.diretory_IMG)
        img_no_background = remove(img)
        print(f"{self.diretory}/{self.name}_sem_fundo.png")
        img_no_background.save(f"{self.diretory}/{self.name}_sem_fundo.png")
        tk.messagebox.showinfo(title="Imagem gerada com sucesso!", message=f"Imagem criada com sucesso!\nEm: {self.diretory}")
        os.startfile(f'{self.diretory}')


    def run(self):
        self.window.mainloop()


app = App()
app.run()