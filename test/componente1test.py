    
import unittest

class componente2Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("crear mock, iniciar objetos para las pruebas")

    def test_es_dif_null(self):
        perro={"raza":"labrador"}
        self.assertIsNotNone(perro,"se espera que perro tenga un valor")
    def test_es(self):
        a=5
        b=5#5.00 es diferente
        self.assertIs(a,b,"no son iguales")#valida que a==b
    def test_noes(self):
        a=5
        b=5.00
        self.assertIsNot(a,b,"no son iguales")#valida que a==b

    """se establecen las condiciones finales"""
    @classmethod
    def tearDown(self):
        print("fin de la prueba")
