class Complex():
    def __init__ (self,real,imaginary):
        self.real = real
        self.imaginary = imaginary
a = Complex(0,1)
b = Complex(1,0)
print(a.real,a.imaginary)
print(b.real,b.imaginary)


#Class fraction Has to have two attributes: Numerator, Denominator ,Create two instances of it. Print out the numerator and denominator of both.

class Fraction():
    def __init__(self,num,den):
        self.num = num
        self.den = den
f1 = Fraction(1,2)
f2 = Fraction(2,3)
print(f"The fraction is (f1.num)/(f1.den)")
print(f"The fraction is (f2.num)/(f2.den)")