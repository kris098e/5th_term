import numpy as np

def f(n, i):
   return 1/(n-2*i-1) - 1/(n-2*i)

def trapezoidal_rule(n, a, b, N):
   h = (b - a) / N
   x = np.linspace(a, b, N)
   y = f(n, x)
   return h * (np.sum(y) + 0.5 * y[0] + 0.5 * y[-1])

n = 10 # example value
a = 0
b = n / 2
N = 1000 # number of intervals

S = trapezoidal_rule(n, a, b, N)
print(S)
