import unittest
from metodos.metodos import soma


class test_soma(unittest.TestCase):

    def test_soma(self):
        # 1. Soma de dois números de 2 dígitos
        self.assertEqual(soma(2, 2), 4)

        # 2. Soma de dois números de 2 dígitos que resulta em 3 dígitos
        self.assertEqual(soma(5, 10), 15)

        # 3. Soma de um número de 3 dígitos com um de 2 dígitos
        self.assertEqual(soma(120, 60), 180)

        # 4. Soma de dois números de 3 dígitos
        self.assertEqual(soma(150, 250), 400)

        # 5. Soma de dois números de 3 dígitos que resulta em 4 dígitos
        self.assertEqual(soma(500, 700), 1200)

        # 6. Soma com um número maior de 3 dígitos e um de 2 dígitos
        self.assertEqual(soma(950, 50), 1000)

        # 7. Soma com o maior número de 3 dígitos
        self.assertEqual(soma(999, 100), 1099)

        # --- Testes com casos especiais (boas práticas) ---

        # 8. Teste com um número negativo (3 dígitos)
        self.assertEqual(soma(200, -50), 150)

        # 9. Teste com ambos os números negativos (2 e 3 dígitos)
        self.assertEqual(soma(-150, -25), -175)

        # 10. Teste somando zero a um número de 3 dígitos
        self.assertEqual(soma(345, 0), 345)       



if __name__ == "__main__":
    unittest.main()

