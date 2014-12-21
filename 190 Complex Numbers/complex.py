# http://www.reddit.com/r/dailyprogrammer/comments/2nr6c4/20141129_challenge_190_practical_exercise_the/

import math


class Complex(object):
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def get_conjugate(self):
        return Complex(real=self.real, imaginary=-self.imaginary)

    @property
    def modulus(self):
        return math.sqrt(self.real*self.real + self.imaginary*self.imaginary)
    
    @property
    def argument(self):
        if self.real == 0 and self.imaginary == 0:
            return 0
        if self.real == 0:
            return (math.pi/2) * (1 if self.imaginary > 0 else -1)
        if self.real > 0:
            return math.atan(float(self.imaginary)/float(self.real))
        if self.real < 0:
            offset = math.pi * (1 if self.imaginary >= 0 else -1)
            return offset + math.atan(float(self.imaginary)/float(self.real))

    def __str__(self):
        def format_number(f):
            return format(f, '.2f').rstrip('0').rstrip('.')

        if self.real == 0 and self.imaginary == 0:
            return '0'
        if self.real == 0:
            return format_number(self.imaginary) + 'i'
        if self.imaginary == 0:
            return format_number(self.real)
        if self.real != 0 and self.imaginary != 0:
            real_string = format_number(self.real)
            imaginary_string = format_number(self.imaginary) + 'i'
            sign = '+' if self.imaginary > 0 else ''
            return real_string + sign + imaginary_string

    def __eq__(self, other):
        if type(other) is not Complex:
            return False
        return self.real == other.real and self.imaginary == other.imaginary

    def __ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        return Complex(real=self.real + other.real,
                       imaginary=self.imaginary + other.imaginary)

    def __sub__(self, other):
        return Complex(real=self.real - other.real,
                       imaginary=self.imaginary - other.imaginary)

    def __mul__(self, other):
        return Complex(self.real*other.real - self.imaginary*other.imaginary,
                       self.real*other.imaginary + other.real*self.imaginary)

    def __truediv__(self, other):
        numerator = self
        numerator *= other.get_conjugate()
        other *= other.get_conjugate()
        return Complex(numerator.real / other.real,
                       numerator.imaginary / other.real)