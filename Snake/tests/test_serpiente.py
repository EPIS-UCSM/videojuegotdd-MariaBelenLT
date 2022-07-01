import turtle
import unittest
from core.snake import Snake


class TestSerpiente(unittest.TestCase):
    def setUp(self) -> None:
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("white")
        self.head.penup()
        self.head.direction = "stop"
    def test_Posicion_inicial_de_serpiente_es_0_0(self) -> None:
        self.assertTrue(self.head.goto(0, 0))

    def test_Posicion_de_serpiente_varia(self) -> None:
        self.assertNotEqual(self.head.goto(), (0,0))


if __name__ == '__main__':
    unittest.main()
