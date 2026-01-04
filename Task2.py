import random
import numpy as np
import scipy.integrate as spi

def f(x):
    return x ** 2

a, b = 0, 2
N = 1_000_000

x_rand = np.random.uniform(a, b, N)
y_rand = f(x_rand)

integral_mc = (b - a) * np.mean(y_rand)

integral_quad, error = spi.quad(f, a, b)

print(f"Метод Монте-Карло: {integral_mc}")
print(f"Quad (SciPy): {integral_quad}")
print(f"Абсолютна різниця: {abs(integral_mc - integral_quad)}")
