import os
import sys
from . import generate
from . import entry as tkinter
# from . import list_dir
import time
import threading

__path = os.path.join(os.path.dirname(sys.argv[0]), 'PassWords')

def __generate(caracteres:str, entry:tkinter.Entry):
    try:
        caracters = int(caracteres)
    except ValueError:
        caracters = len(caracteres)
    
    caracters = caracters if caracters != 0 else 8

    senha = generate.generate(caracters)
    entry.configure(state='normal')
    entry.delete(0, tkinter.END)
    entry.insert('end', senha)
    entry.configure(state='readonly')

def __save(name:str, pass_:str):
    if pass_:
        if name and name != 'Nome da sua Senha':
            if not os.path.exists(__path):
                os.mkdir(__path)
            path = os.path.join(__path, f'{name}.txt')
            f = open(path, 'w')
            retornar = f.write(pass_)
            f.close()
        else:
            retornar = -2
    else:
        retornar = -1
    if retornar == -2:
        outputLabel.configure(text='Por favor insira um nome!')
    elif retornar == -1:
        outputLabel.configure(text='Por favor clique em gerar para criar uma nova senha!')
    else:
        outputLabel.configure(text='Senha Salva com Sucesso!')

    outputLabel.update()
    threading.Thread(target=lambda: f"{time.sleep(3)}{outputLabel.configure(text='')}").start()

def criar():
    window = tkinter.Tk()
    window.title('Criador de Senhas')
    window.geometry('400x300')
    window.resizable(False, False)
    # local de geração
    window.copy = tkinter.PEntry(window, state='readonly', width=50, justify='center')
    window.copy.place(relx=.5, y=250, anchor='center')
    # local de configuração
    window.caracteres = tkinter.PEntry(window, width=3, placeholder='8')
    window.caracteres.place(relx=.6, y=60, anchor='center')
    #
    tkinter.Label(window, text='N° de caracteres:').place(relx=.45, y=60, anchor='center')
    #
    window.nome = tkinter.PEntry(window, placeholder='Nome da sua Senha', width=50)
    window.nome.place(relx=.5, y=20, anchor='center')
    #
    global outputLabel
    outputLabel = tkinter.Label(window, text='', justify='center')
    outputLabel.place(relx=.5, rely=.5, anchor='center')
    # botão de gerar
    window.button1 = tkinter.Button(window, text='Gerar', command=lambda: __generate(window.caracteres.get(), window.copy))
    window.button1.place(relx=.56, y=200, anchor='center')
    # botão de salvar
    window.button2 = tkinter.Button(window, text='Salvar', command=lambda: __save(window.nome.get(), window.copy.get()))
    window.button2.place(relx=.44, y=200, anchor='center')
    # loop principal
    window.mainloop()

def gerenciar():
    window = tkinter.Tk()
    window.title('Gerenciador de Senhas')
    window.geometry('400x300')
    window.resizable(False, False)

    passwords: list[tkinter.Entry] = list()

    if not os.path.exists(__path):
        os.mkdir(__path)

    window.Frame = tkinter.Listbox(window)
    window.Frame.pack(fill=tkinter.BOTH, expand=True)

    barra_rolagem = tkinter.Scrollbar(window.Frame, orient=tkinter.VERTICAL, command=window.Frame.yview)
    barra_rolagem.pack(side=tkinter.RIGHT, fill=tkinter.Y)

    window.Frame.configure(yscrollcommand=barra_rolagem.set)

    with os.scandir(__path) as arquivos:
        for arquivo in arquivos:
            if arquivo.is_file():
                name = arquivo.name.replace('.' + arquivo.name.split('.')[-1], '')
                with open(arquivo, 'r') as f:
                    label_text = f'{name}: {f.read()}'
                    passwords.append(label_text)

    for password in passwords:
        window.Frame.insert(tkinter.END, password)

    window.mainloop()
