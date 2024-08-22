from tkinter import *
import tkinter as tk

janela = Tk()
janela.geometry("650x100")
janela.title("Avaliação - Laboratório de Programação (Sistema de busca)")

texto = Label(janela, text="Digite o tema que deseja realizar a busca:")
texto.grid(column=0, row=1, padx=10, pady=20)

entrada = tk.Entry(janela, width=50)
entrada.grid(column=1, row=1, padx=10, pady=10)

botao = Button(janela, text="Buscar")
botao.grid(column=2, row=1, padx=10, pady=10)


janela.mainloop()
