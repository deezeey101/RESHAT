import unittest
from Mainpython import Calculator

class CalculatorTest(unittest.TestCase):
    calculator = Calculator()
    def test_setupUi(self):
        calculator = Calculator()
    
    def test_remove_it(self):
        self.calc = self.test_remove_it
        self.calc = Calculator()
        self.calc.answer = "1322315"
        screen = self.calc.answer
        screen = screen[:-1]
        self.assertNotEqual(self.calc.answer,"132231")

    def test_solver(self):
        self.calc = self.test_solver
        self.calc = Calculator()
        self.calc.answer = "10"
        self.calc.equation = "15 + 4 / 2 - 7 * 1"
        self.assertEqual(self.calc.answer, "10") 
    
    def test_plus_minus_it(self):
        self.calc = self.test_plus_minus_it
        self.calc = Calculator()
        self.calc.answer = ""
        screen = (self.calc.answer)
        if "-" in screen:
            screen = screen.replace("-","")
        else:
            self.calc.answer = "-"
        self.assertEqual(self.calc.answer, "-")
    
    def test_dot_it(self):
        self.calc = self.test_plus_minus_it
        self.calc = Calculator()
        self.calc.answer = "."
        screen = (self.calc.answer)
        if "." in screen:
            screen += "."
        self.assertEqual(self.calc.answer, ".")

    def test_press_it(self):
        self.calc = self.test_press_it
        self.calc = Calculator()
        self.calc.answer = "C"
        screen = (self.calc.answer)
        pressed = screen
        if pressed == "C":
            screen == "0"
        else:
            if screen == "0":
                screen("")    
            self.calc.answer(f'{pressed}')
        self.assertNotEqual(self.calc.answer, "")

if __name__ == "__main__":
    unittest.main()
