from Genetic.population import population
import math

def main():
    population.maximize_function(f5, 100)

def f1(x, y, z):
    return (2*x) - y - (z**2)

def f2(x1, x2, x3, x4, x5):
    return x1 + 2*x2 + 3*x3 + 4*x4 + 5*x5

def f3(a, b, c, d, e, f):
    return a + b + c + d + e + f

def f4(x, y):
    return math.sin(x) + 3*math.cos(y)

def f5(a, b, c):
    return 10 - math.fabs(a) - math.fabs(b) - math.fabs(c)

def pi(x):
    return math.sin(x)

if __name__ == '__main__':
    try:
        main()
    except:
        raise