import math
import unittest
from complex import Complex


class ComplexAttributesTestCase(unittest.TestCase):
    def test_constructor_set_get(self):
        c = Complex(real=10.0, imaginary=15.0)
        self.assertEqual(10.0, c.real)
        self.assertEqual(15.0, c.imaginary)

    def test_set_get(self):
        c = Complex()
        c.real = 10.0
        c.imaginary = 20.0
        self.assertEqual(10.0, c.real)
        self.assertEqual(20.0, c.imaginary)


class ComplexConjugateTestCase(unittest.TestCase):
    def test_conjugate_construction(self):
        c = Complex(real=15.0, imaginary=10.0)
        conjugate = c.get_conjugate()
        self.assertEqual(15.0, conjugate.real)
        self.assertEqual(-10.0, conjugate.imaginary)


class ComplexModulusTestCase(unittest.TestCase):
    def test_modulus_positive_attributes(self):
        c = Complex(real=3.0, imaginary=4.0)
        self.assertEqual(5.0, c.modulus)

    def test_modulus_negative_attributes(self):
        c = Complex(real=-3.0, imaginary=-4.0)
        self.assertEqual(5.0, c.modulus)

    def test_modulus_zero(self):
        c = Complex(real=0.0, imaginary=0.0)
        self.assertEqual(0.0, c.modulus)


class ComplexArgumentTestCase(unittest.TestCase):
    def test_argument_quadrant_1(self):
        c = Complex(real=1.0, imaginary=1.0)
        self.assertEqual(0.25 * math.pi, c.argument)

    def test_argument_quadrant_2(self):
        c = Complex(real=-1.0, imaginary=1.0)
        self.assertEqual(0.75 * math.pi, c.argument)

    def test_argument_quadrant_3(self):
        c = Complex(real=-1.0, imaginary=-1.0)
        self.assertEqual(-0.75 * math.pi, c.argument)

    def test_argument_quadrant_4(self):
        c = Complex(real=1.0, imaginary=-1.0)
        self.assertEqual(-0.25 * math.pi, c.argument)

    def test_argument_zero(self):
        c = Complex(real=0.0, imaginary=0.0)
        self.assertEqual(0.0, c.argument)

    def test_argument_1(self):
        c = Complex(real=1.0, imaginary=0.0)
        self.assertEqual(0.0, c.argument)

    def test_argument_i(self):
        c = Complex(real=0.0, imaginary=1.0)
        self.assertEqual(math.pi/2.0, c.argument)

    def test_argument_minus_1(self):
        c = Complex(real=-1.0, imaginary=0.0)
        self.assertEqual(math.pi, c.argument)

    def test_argument_minus_i(self):
        c = Complex(real=0.0, imaginary=-1.0)
        self.assertEqual(-math.pi/2.0, c.argument)


class ComplexStrTestCase(unittest.TestCase):
    def test_zero_string(self):
        c = Complex(real=0.0, imaginary=0.0)
        self.assertEqual('0', str(c))

    def test_real_string(self):
        c = Complex(real=1.5, imaginary=0.0)
        self.assertEqual('1.5', str(c))

    def test_imaginary_string(self):
        c = Complex(real=0.0, imaginary=5.5)
        self.assertEqual('5.5i', str(c))

    def test_complex_string(self):
        c = Complex(real=2.3, imaginary=-4.54)
        self.assertEqual('2.3-4.54i', str(c))


class ComplexEqualityTestCase(unittest.TestCase):
    def test_complex_equal(self):
        c1 = Complex(real=1.3, imaginary=2.6)
        c2 = Complex(real=1.3, imaginary=2.6)
        self.assertTrue(c1 == c2)

    def test_complex_not_equal(self):
        c1 = Complex(real=2.6, imaginary=3.4)
        c2 = Complex(real=2.6, imaginary=3.5)
        self.assertFalse(c1 == c2)


class ComplexOperationsTestCase(unittest.TestCase):
    def test_complex_add(self):
        c1 = Complex(real=2.0, imaginary=3.1)
        c2 = Complex(real=1.5, imaginary=2.6)
        c_add = c1 + c2
        self.assertEqual(3.5, c_add.real)
        self.assertEqual(5.7, c_add.imaginary)

    def test_complex_subtraction(self):
        c1 = Complex(real=2.0, imaginary=3.1)
        c2 = Complex(real=1.5, imaginary=2.6)
        c_sub = c1 - c2
        self.assertEqual(0.5, c_sub.real)
        self.assertEqual(0.5, c_sub.imaginary)

    def test_complex_multiplication(self):
        c1 = Complex(real=3.4, imaginary=2.6)
        c2 = Complex(real=1.5, imaginary=2.9)
        c1_mul = c1 * c2
        self.assertEqual(-2.44, round(c1_mul.real, 2))
        self.assertEqual(13.76, round(c1_mul.imaginary, 2))

    def test_complex_division(self):
        c1 = Complex(real=3.4, imaginary=2.6)
        c2 = Complex(real=1.5, imaginary=2.9)
        c1_div = c1 / c2
        self.assertEqual(1.19, round(c1_div.real, 2))
        self.assertEqual(-0.56, round(c1_div.imaginary, 2))