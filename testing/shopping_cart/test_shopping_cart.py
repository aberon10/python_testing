from shopping_cart import ShoppingCart
from shopping_cart import Item
from shopping_cart import NotExistsItemError
import unittest
API_VERSION = 17

class TestShoppingCart(unittest.TestCase):

    def setUp(self) -> None:
        """ Este método se ejecuta previo a cada prueba
        """
        self.pan = Item("Pan", 7.0)
        self.jugo = Item("Jugo", 5.0)
        self.shopping_cart = ShoppingCart()
        self.shopping_cart.add_item(self.pan)

    def tearDown(self) -> None:
        pass

    def test_nombre_producto_igual_pan(self):
        self.assertEqual(self.pan.name, "Pan", "Fallo la prueba")

    def test_nombre_producto_diferente_pan(self):
        self.assertNotEqual(self.jugo.name, "Pan")

    def test_contiene_productos(self):
        self.assertTrue(self.shopping_cart.contains_items())
    
    def test_no_contiene_productos(self):
        self.shopping_cart.remove_item(self.pan)
        self.assertFalse(self.shopping_cart.contains_items())

    def test_obtener_producto_pan(self):
        item = self.shopping_cart.get_item(self.pan)
        self.assertIs(item, self.pan)
        self.assertIsNot(item, self.jugo)
    
    def test_exception_al_obtener_jugo(self):
        with self.assertRaises(NotExistsItemError):
            self.shopping_cart.get_item(self.jugo)
    
    def test_total_con_un_producto(self):
        total = self.shopping_cart.total()
        self.assertGreater(total, 0)
        self.assertLess(total, self.pan.price + 1)
        self.assertEqual(total, self.pan.price)
    
    def test_codigo(self):
        self.assertRegex(self.pan.code(), self.pan.name)
    
    def test_fail(self):
        if 2 > 3:
            self.fail("Dos no es mayor que tres!")
    
    # @unittest.skip("Colocamos nuestros motivos")
    # @unittest.skipIf(API_VERSION < 18, "La versión es obsoleta")
    @unittest.skipUnless(3 > 6, "Colocamos nuestros motivos")
    def test_prueba_skip(self):
        pass

if __name__ == "__main__":
    unittest.main()
