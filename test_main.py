import unittest
from main import descobre_numero

class TesteDescobreNumero(unittest.TestCase):
    def test_descobre_numero(self):
        for _ in range(2):  # Executa o teste duas vezes
            resultado = descobre_numero(5)
            self.assertTrue(resultado.startswith("O número que você adivinhou foi: "))
            numero = int(resultado.split(": ")[1])
            self.assertTrue(numero == 5, "O programa não adivinhou meu número")

if __name__ == '__main__':
    unittest.main()