"""
Pruebas unitarias para la logica matematica y evaluacion de la calculadora cientifica.
"""

import unittest
import math


class TestCalculadoraLogica(unittest.TestCase):
    def safe_math_context(self, angle_mode="DEG"):
        to_radians = math.radians if angle_mode == "DEG" else (lambda x: x)
        return {
            "sin": lambda x: math.sin(to_radians(x)),
            "cos": lambda x: math.cos(to_radians(x)),
            "tan": lambda x: math.tan(to_radians(x)),
            "asin": lambda x: math.degrees(math.asin(x)) if angle_mode == "DEG" else math.asin(x),
            "acos": lambda x: math.degrees(math.acos(x)) if angle_mode == "DEG" else math.acos(x),
            "atan": lambda x: math.degrees(math.atan(x)) if angle_mode == "DEG" else math.atan(x),
            "sinh": math.sinh,
            "cosh": math.cosh,
            "tanh": math.tanh,
            "sqrt": math.sqrt,
            "log": math.log10,
            "ln": math.log,
            "exp": math.exp,
            "pi": math.pi,
            "e": math.e,
        }

    def eval_expr(self, expr, angle_mode="DEG"):
        return eval(expr, {"__builtins__": {}}, self.safe_math_context(angle_mode))

    def test_operaciones_aritmeticas_basicas(self):
        self.assertEqual(self.eval_expr("2+3*4"), 14)
        self.assertEqual(self.eval_expr("(10-4)/2"), 3.0)
        self.assertEqual(self.eval_expr("2**8"), 256)

    def test_trigonometria_grados(self):
        self.assertAlmostEqual(self.eval_expr("sin(90)", "DEG"), 1.0)
        self.assertAlmostEqual(self.eval_expr("cos(0)", "DEG"), 1.0)
        self.assertAlmostEqual(self.eval_expr("tan(45)", "DEG"), 1.0)

    def test_trigonometria_radianes(self):
        self.assertAlmostEqual(self.eval_expr("sin(pi/2)", "RAD"), 1.0)
        self.assertAlmostEqual(self.eval_expr("cos(pi)", "RAD"), -1.0)

    def test_funciones_avanzadas(self):
        self.assertEqual(self.eval_expr("sqrt(144)"), 12.0)
        self.assertEqual(self.eval_expr("log(1000)"), 3.0)
        self.assertAlmostEqual(self.eval_expr("ln(e)"), 1.0)


if __name__ == "__main__":
    unittest.main()
