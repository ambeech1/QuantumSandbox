import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

from Solvers.SolverTISE import SolverTISE

x = sp.symbols("x")
a = sp.symbols("a")
h = sp.symbols("h")

u = sp.Function('u')

#class u(sp.Function):
    #@classmethod
    #def eval(cls, x):
        #a = np.ones_like(x)
        #for i in range(len(a)):
            #if x[i] < 0:
                #a[i] = 0
        #return a

solver = SolverTISE()
string = input("Enter a potential: ")
    #try:
expr = sp.sympify(string)
expr = expr.subs(u(x), sp.Heaviside(x))
U = sp.lambdify(x, expr, "numpy")
plt.plot(solver.x, U(solver.x))
plt.show()
    #except:
        #print("ERROR")
