import unittest
from retos.reto1_stack import validate_expression

class TestChallenge1Stack(unittest.TestCase):
    def test_simple_balanced_expression(self):
        # Arrange
        expresion = "({[]})"
        # Act
        resultado = validate_expression(expresion)
        # Assert
        self.assertTrue(resultado)

    # TODO: agrega más casos:
    # - desbalance por cierre extra
    def test_desbalance_por_cierre_extra(self):
        expresion = "({[]})}"
        resultado = validate_expression(expresion)
        self.assertFalse(resultado)

    # - orden incorrecto "{[}]"
    def test_orden_incorrecto(self):
        expresion = "{[}]"
        resultado = validate_expression(expresion)
        self.assertFalse(resultado)
        
    # - cadena vacía -> True
    def test_cadena_vacia(self):
        expresion = ""
        resultado = validate_expression(expresion)
        self.assertTrue(resultado)

    # - solo aperturas -> False
    def test_solo_aperturas(self):
        expresion = "({["
        resultado = validate_expression(expresion)
        self.assertFalse(resultado)

if __name__ == "__main__":
    unittest.main()
