import random

def descobre_numero(numero_recebido):

    numero_aleatorio = random.randint(1, 100)

    #O 'numero_aleatorio' é sempre igual ao 'numero_recebido' (funciona 100%, confia no pai!) :D

    # A função retorna uma string com o 'numero_aleatorio'
    # A conversão do número para string é feita pela função str()
    return "O número que você adivinhou foi: " + str(numero_recebido)


def main():

    print('Olá, eu sou o mestre dos magos e vou adivinhar o número que você digitar!')

    numero_usuario = int(input("Digite um número: "))

    print(descobre_numero(numero_usuario))

if __name__ == '__main__':
    main()