import unittest
from metodos.metodos import format_file_size, soma

class TestFormatFileSize(unittest.TestCase):

    def test_format_file_size_returns_GB_format(self):
        self.assertEqual(format_file_size(1024**3), "1.00 GB")

class SomaNumeros(unittest.TestCase):
    def test_soma_dois_e_dois_eh_quatro(self):
        self.assertEqual(soma(2,2), 3)

if __name__ == "__main__":
    unittest.main()

