import turtle
import unittest

from core.snake import Snake


class TestScore(unittest.TestCase):
    def setUp(self) -> None:
        self.tablero = turtle.Turtle()
        self.tablero.speed(0)
        self.tablero.color('white')
        self.tablero.penup()
        self.tablero.hideturtle()
        self.tablero.goto(0, 260)
        self.tablero.write('Current Score: 0            High score: 0',
                           align='center', font=('Courier', 26, 'normal'))

    def test_aumento_de_current_score_con_colision(self) -> None:
        self.score +- 10
        self.tablero.write('Current Score: {}            High score: {}'.format(self.score, self.high_score),
                           align='center', font=('Courier', 26, 'normal'))

    def test_actualiza_high_score_cuando_current_score_lo_supera(self) -> None:
        if self.high_score < self.score:
            high_score = self.score
        self.assertGreaterEqual(self.high_score, self.score)


if __name__ == '__main__':
    unittest.main()
