import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

from Solvers.SolverTISE import SolverTISE

X = sp.symbols("x")
A = sp.symbols("a")
H = sp.symbols("h")

W = sp.exp(A * (X - H) ** (-2))

solver = SolverTISE()
string = input("Enter a potential: ")
try:
    expr = sp.sympify(string)
    U = sp.lambdify(X, expr, "numpy")
    plt.plot(solver.x, U(solver.x))
    plt.show()
except:
    print("ERROR")
