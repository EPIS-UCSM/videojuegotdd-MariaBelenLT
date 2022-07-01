import turtle
import unittest
import random

from core.snake import Snake


class TestFruta(unittest.TestCase):
    def setUp(self) -> None:
        self.comida = turtle.Turtle()
        self.comida.speed(0)
        self.comida.shape("circle")
        self.comida.color("red")
        self.comida.penup()


    def test_Colision_de_fruta_y_serpiente(self) -> None:
        self.assertTrue(self.head.distance(self.comida) < 20)

    def test_Posicion_de_fruta_dentro_de_margenes(self) -> None:
        self.assertTrue(self.comida.goto(0, 100))


    def test_Posicion_de_fruta_cambia(self) -> None:
        if self.head.distance(self.comida) < 20:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            self.comida.goto(x, y)
            cambio_posicion = 0
        self.assertTrue(cambio_posicion == 0)


if __name__ == '__main__':
    unittest.main()
