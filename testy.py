import unittest
import main as m

class Sprawdzanie(unittest.TestCase):
    def test_wygranie_x(self):
        m.ruch('X', 0)
        m.ruch('O', 1)
        m.ruch('X', 3)
        m.ruch('O', 8)
        m.ruch('X', 6)
        assert m.wygranie_x() == 'X'
    def test_wygranie_o(self):
        m.ruch('O', 0)
        m.ruch('X', 1)
        m.ruch('O', 3)
        m.ruch('X', 8)
        m.ruch('O', 6)
        assert m.wygranie_o() == 'O'

if __name__ == "__main__":
    unittest.main()