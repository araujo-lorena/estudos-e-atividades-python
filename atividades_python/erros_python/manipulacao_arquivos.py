""" Crie uma função que tente abrir um arquivo para leitura. Se o arquivo não existir, capture
 a FileNotFoundError e crie o arquivo (em modo de escrita). Use um bloco finally para garantir 
 que o arquivo seja fechado se for aberto."""

def manipular_arquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'r')
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)

    except FileNotFoundError:
        arquivo = open(nome_arquivo, 'w')
        print("Arquivo criado.")

    finally:
        arquivo.close()
        print("Arquivo fechado.")

manipular_arquivo('nome_arquivo.txt')