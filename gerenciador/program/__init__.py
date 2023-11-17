import os
import sys
from . import generate
from . import entry as tkinter

def __generate(master:tkinter.Tk, caracteres:str):
    try:
        caracters = int(caracteres)
    except ValueError as e:
        master.destroy()

def main():
    window = tkinter.Tk()
    window.title('Gerenciador de Senhas')
    window.geometry('400x300')
    window.resizable(False, False)
    # local de geração
    window.copy = tkinter.Entry(window, state='readonly', width=50, justify='center')
    window.copy.place(relx=.5, y=250, anchor='center')
    # local de configuração
    window.caracteres = tkinter.Entry(window, width=3, placeholder='8')
    window.caracteres.place(relx=.6, y=60, anchor='center')

    tkinter.Label(window, text='N° de caracteres:').place(relx=.45, y=60, anchor='center')

    window.nome = tkinter.Entry(window, placeholder='Nome da sua Senha', width=50)
    window.nome.place(relx=.5, y=20, anchor='center')
    # loop principal    
    window.mainloop()
    
