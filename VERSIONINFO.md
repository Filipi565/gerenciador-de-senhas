# Versão 0.0.1
Criação dos arquivos iniciais

criação das funções iniciais

criação das classes iniciais

importação dos módulos iniciais

# Versão 0.0.2
Adicionado Botão Salvar 

função main() agora se chama criar()

programa app.py agora se chama Gerador.py

# Versão 1.0.0
Programa de Gerenciamento fora do Programa de Gerar senhas

* _
_
init
_
_.py

```Função __generate()```

se o parâmetro "caracteres" não for um número inteiro, ele vai pegar a quantidade de caracteres que tem no parâmetro como base, porém a quantidade de caracteres for 0, ele vai colocar a padrão: 8.

logo após, a função vai gerar uma senha nova de acordo com a quantidade de caracteres na função generate() do módulo generate.

```Função __save()```

essa função vai salvar um arquivo na pasta "PassWords" com o nome dado e escrever o conteúdo "pass_".

```Função criar()```

essa função cria uma janela de criação de senha usando o tkinter com elementos de gerar senha, colocar um nome para a senha, colocar um número de caracteres, botão de gerar e salvar e uma barra onde você pode copiar sua nova senha.

```Função gerenciar()```

essa função cria uma janela de gerenciamento de senha usando o tkinter. nessa tela você pode ver sua senha salva anteriormente na pasta "PassWords".

* entry.py

```Classe PEntry```

essa classe é uma Entry do tkinter, porém com uma placeholder

* generate.py

```Função generate()```

essa função vai gerar uma senha aleatória de acordo com a quantidade de caracteres que foi dado.

* random_.py

nesse módulo, só adiciona uma função amais para a biblioteca random.

```Função randletter()```

retorna uma letra aleatória

* list_dir.py

dfsr = disable file system redirection
use essa classe para bugs na hora de usar os.listdir
olhe a pergunta: <a href="https://stackoverflow.com/questions/19187812">os.listdir can't see my directory</a>