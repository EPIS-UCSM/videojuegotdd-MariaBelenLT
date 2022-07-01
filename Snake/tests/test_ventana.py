import turtle
import unittest
from core.snake import Snake


class TestVentana(unittest.TestCase):
    def setUp(self) -> None:
        self.window = turtle.Screen()
        self.window.title('Snake Game')
        self.window.bgcolor('black')
        self.window.setup(width=600, height=600)
        self.window.tracer(0)

    def test_Creacion_de_la_ventana(self) -> None:
        self.assertTrue(turtle.Screen())

    def test_Color_de_Fondo_Ventana_negro(self) -> None:
        self.assertEqual(self.window.bgcolor(), 'black')

    def test_Colision_con_borde_de_ventana(self) -> None:
        if self.head.xcor() > 280 or self.head.xcor() < -290 or self.head.ycor() > 290 or self.head.ycor() < -290:
            colision_borde = True
        self.assertTrue(colision_borde)


if __name__ == '__main__':
    unittest.main()
