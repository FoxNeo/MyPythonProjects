# Unittest - Sirve para crear pruebas dentro del propio código

def multiplicar(num1, num2):
    return num1 * num2

result = multiplicar(2, 4)
print(result)

import unittest


class pruebas(unittest.TestCase):

    def test(self):
        self.assertEqual(multiplicar(2,4), 8)

if __name__ == '__main__':
    unittest.main()