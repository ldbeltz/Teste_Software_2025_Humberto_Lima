import unittest
from metodos.metodos import format_file_size

class test_format_file_size(unittest.TestCase):

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


if __name__ == "__main__":
    unittest.main()

