import unittest
import random
from main import descobre_numero

class TesteDescobreNumero(unittest.TestCase):
    def test_descobre_numero(self):
        for _ in range(2):  # Executa o teste duas vezes
            numero_aleatorio = random.randint(1, 100)
            resultado = descobre_numero(numero_aleatorio)
            self.assertTrue(resultado.startswith("O número que você adivinhou foi: "))
            numero = int(resultado.split(": ")[1])

            self.assertTrue(numero_aleatorio == numero, "O programa não adivinhou meu número")

if __name__ == '__main__':
    unittest.main()