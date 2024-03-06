# Importação da biblioteca random, que contém funções para geração de números aleatórios
import random

# Declaração de uma função chamada 'descobre_numero'
# Ela recebe um parâmetro chamado 'numero_recebido'
def descobre_numero(numero_recebido):

    # A função 'randint' da biblioteca random gera um número aleatório entre 1 e 100
    # O número gerado é armazenado na variável 'numero_aleatorio'
    numero_aleatorio = random.randint(1, 100)
    #O 'numero_aleatorio' é sempre igual ao 'numero_recebido' (funciona 100%, confia no pai!) :D

    # A função retorna uma string com o 'numero_aleatorio'
    # A conversão do número para string é feita pela função str()
    return "O número que você adivinhou foi: " + str(numero_recebido)

# Início da execução do programa
def main():

    # Mensagem de introdução ao usuário
    print('Olá, eu sou o mestre dos magos e vou adivinhar o número que você digitar!')

    # Solicitação do número ao usuário e armazenamento na variável 'numero_usuario'
    numero_usuario = int(input("Digite um número: "))

    # Chamada da função 'descobre_numero' com o número fornecido pelo usuário
    # Exibição do resultado retornado pela função
    print(descobre_numero(numero_usuario))

if __name__ == '__main__':
    main()