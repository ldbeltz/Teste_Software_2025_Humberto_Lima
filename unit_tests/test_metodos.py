import unittest
from metodos.metodos import format_file_size, soma


class teste_SomaNumeros(unittest.TestCase):

    def test_format_file_size(self):
        # 1. Testa o valor zero. É o caso mais básico.
        self.assertEqual(format_file_size(0), "0B")

        # 2. Testa um valor em Bytes que não chega a 1 KB.
        self.assertEqual(format_file_size(789), "789.00 B")

        # 3. Testa o valor exato de 1 Kilobyte (KB).
        self.assertEqual(format_file_size(1024), "1.00 KB")

        # 4. Testa um valor quebrado em KB para verificar o cálculo e formatação decimal.
        self.assertEqual(format_file_size(1536), "1.50 KB") # (1024 * 1.5)

        # 5. Testa o valor exato de 1 Megabyte (MB).
        self.assertEqual(format_file_size(1024**2), "1.00 MB")

        # 6. Testa um valor quebrado em MB, que resulta em arredondamento.
        self.assertEqual(format_file_size(2621440), "2.50 MB") # (1024**2 * 2.5)

        # 7. Testa um valor alto em MB para garantir que a unidade não mude para GB prematuramente.
        self.assertEqual(format_file_size(999 * 1024**2), "999.00 MB")

        # 8. Testa um valor quebrado em GB que não seja o original.
        self.assertEqual(format_file_size(5.75 * 1024**3), "5.75 GB")

        # 9. Testa o valor exato de 1 Terabyte (TB) para verificar unidades maiores.
        self.assertEqual(format_file_size(1024**4), "1.00 TB")

        # 10. Testa o valor exato de 1 Petabyte (PB) para testar o limite superior da função.
        # Nesse caso, o teste retorna uma falha.
        # self.assertEqual(format_file_size(1024**5), "1.00 PB")


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

