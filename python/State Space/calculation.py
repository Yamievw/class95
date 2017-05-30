import math

def fac(x):
    return math.factorial(x)

def calc(n, m, x):
    output = fac(m*x)
    output = output/float(fac(x)*fac(m*x-n)*fac(m))
    return output

print calc(3, 2, 10)
