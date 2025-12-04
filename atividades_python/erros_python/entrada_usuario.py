"""Solicite uma entrada ao usuário e trate a exceção KeyboardInterrupt caso ele pressione Ctrl+C
 para cancelar a operação"""

def entrada_usuario():
    try:
        nome = input("Digite seu nome: ")
        print(f"Olá, {nome}!")

    except KeyboardInterrupt:
        print("\nA execução foi interrompida pelo usuário.")

entrada_usuario()