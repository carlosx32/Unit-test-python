import unittest

class componente2Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("crear mock, iniciar objetos para las pruebas")

    """se establecen las preciondiciones"""
    def setUp(self):
        self.variable1=4
        self.variable2=0
        precondicion=True
        if(precondicion==True):
            self.correr=True
        else:
            self.correr=False



    def test_suma(self):
        self.assertEqual(self.variable1, 4)
        self.assertTrue(self.correr)
    def test_resta(self):
        self.assertTrue(self.variable2==0)
        self.assertTrue(self.correr)
    
    def test_validar_siverdadero(self):
        a=True

        #verifica un valor verdadero
        self.assertTrue(a,"Se esperaba un valor true en la variable a")

    def test_ValidarconassertEqual(self):
        a=False
        self.assertFalse(a,"Se esperaba un valor false en la variable a")
    def test_verificarEquls(self):
        self.assertEqual(3,1+1+1,"se esperaba 1+1+1 =  3")

    def test_verificarnotEquls(self):
        self.assertNotEqual(4,1+1+1,"se esperaba 1+1+1 !=  4")

    def test_valorDiffNull(self):
        perro=None
        self.assertIsNone(perro,"el objeto perro debe ser none")


    """se establecen las condiciones finales"""
    @classmethod
    def tearDown(self):
        print("fin de la pruebas")
