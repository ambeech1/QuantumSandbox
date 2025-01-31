# file imports
import numpy as np
import scipy.constants as const
from scipy.sparse import diags
from scipy.linalg import solve_banded
from scipy.sparse.linalg import spsolve
import scipy.linalg as la
from scipy.linalg import eigh_tridiagonal
import sympy as sp

# class definition
class SolverTISE:
    def __init__(self):
        e = const.e
        pi = const.pi
        h_bar = const.hbar # J * s
        q_e = const.elementary_charge # C
        m_e = const.electron_mass # kg
        m_p = const.proton_mass # kg
        eV = const.electron_volt # J

        self.xmin = -10
        self.xmax = 10
        self.N = 501
        self.x = None
        self.x_init_()
        self.U = None
        self.potExpr = None
        self.xSym = sp.symbols("x")

    def x_init_(self):
        self.x = np.linspace(self.xmin, self.xmax, self.N)

    def U_clear_(self):
        self.U = None

    def readPotential(self, potentialString):
        try:
            expr = sp.sympify(potentialString)
            self.U = expr.subs(self.xSym, self.x)
            self.potExpr = expr
        except:
            self.U_clear_()
            self.potExpr = None

    def setXMin(self, min):
        self.xmin = min
        self.x_init_()

    def setXMax(self, max):
        self.xmax = max
        self.x_init_()

    def setXN(self, N):
        self.N = N
        self.x_init_()
        if self.potExpr is not None:
            self.readPotential(self.potExpr)
        else:
            pass

    def defineHamiltonian(self):
        pass

    def solveTISE(self):
        pass






'''

DEFINE POTENTIAL, PARAMETERS

# potential
def V(x):
    return x ** 2

# parameters
xmin = -5
xmax = 5
N = 501

dx = (xmax - xmin) / (N - 1)
x = np.linspace(xmin, xmax, N)


DEFINE HAMILTONIAN MATRIX

hbar = 1
m = 0.5

A = -(hbar ** 2) / (2 * m)
diag = V(x) - ((2 * A / (dx ** 2)) * np.ones_like(x))
off_diag = (A / (dx ** 2)) * np.ones(len(x) - 1)



SOLVE EIGENVALUE PROBLEM

minI = 1
maxI = 5
eval, evec = eigh_tridiagonal(diag, off_diag, select = 'i', select_range = (minI - 1, maxI))

legendList = []
for i in range(0, maxI - minI + 1):
    plt.plot(evec[:, i])
    legendList.append(f'n = {minI + i}')
plt.legend(legendList)
plt.grid()
plt.show()
'''