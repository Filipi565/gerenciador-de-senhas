import os
import sys
from . import generate
from . import entry as tkinter
from . import list_dir

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

def __save(nome:str, pass_:str):
    if pass_:
        if nome and nome != 'Nome da sua Senha':
            if not os.path.exists(__path):
                os.mkdir(__path)
            path = os.path.join(__path, f'{nome}.txt')
            f = open(path, 'w')
            retornar = f.write(pass_)
            f.close()
        else:
            retornar = None
            print(retornar)
    else:
        retornar = None
        print(retornar)
    return retornar

def criar():
    window = tkinter.Tk()
    window.title('Criador de Senhas')
    window.geometry('400x300')
    window.resizable(False, False)
    # local de geração
    copy = tkinter.PEntry(window, state='readonly', width=50, justify='center')
    copy.place(relx=.5, y=250, anchor='center')
    # local de configuração
    window.caracteres = tkinter.PEntry(window, width=3, placeholder='8')
    window.caracteres.place(relx=.6, y=60, anchor='center')
    #
    tkinter.Label(window, text='N° de caracteres:').place(relx=.45, y=60, anchor='center')
    #
    window.nome = tkinter.PEntry(window, placeholder='Nome da sua Senha', width=50)
    window.nome.place(relx=.5, y=20, anchor='center')
    # botão de gerar
    window.button1 = tkinter.Button(window, text='Gerar', command=lambda: __generate(window.caracteres.get(), copy))
    window.button1.place(relx=.56, y=200, anchor='center')
    # botão de salvar
    window.button2 = tkinter.Button(window, text='Salvar', command=lambda: __save(window.nome.get(), copy.get()))
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

    with os.scandir(__path) as entries:
        for entry in entries:
            if entry.is_file():
                name = entry.name.replace('.' + entry.name.split('.')[-1], '')
                with open(entry, 'r') as f:
                    label_text = f'{name}: {f.read()}'
                    passwords.append(label_text)

    for password in passwords:
        window.Frame.insert(tkinter.END, password)

    window.mainloop()
