import random

def descobre_numero(numero_recebido):

    numero_aleatorio = random.randint(1, 100)
    return "O número que você adivinhou foi: " + str(numero_aleatorio)

def main():

    print('Olá, eu sou o mestre dos magos e vou adivinhar o número que você digitar!')

    numero_usuario = int(input("Digite um número: "))

    print(descobre_numero(numero_usuario))

if __name__ == '__main__':
    main()