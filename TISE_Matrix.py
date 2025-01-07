# import libraries
import numpy as np
import scipy.constants as const
from scipy.sparse import diags
from scipy.linalg import solve_banded
from scipy.sparse.linalg import spsolve
from scipy import linalg as la
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.animation import FuncAnimation
matplotlib.use('TkAgg')
from scipy.linalg import eigh_tridiagonal


'''
DEFINE POTENTIAL, PARAMETERS
'''
# potential
def V(x):
    return x ** 2

# parameters
xmin = -5
xmax = 5
N = 501

dx = (xmax - xmin) / (N - 1)
x = np.linspace(xmin, xmax, N)

'''
DEFINE HAMILTONIAN MATRIX
'''
hbar = 1
m = 0.5

A = -(hbar ** 2) / (2 * m)
diag = V(x) - ((2 * A / (dx ** 2)) * np.ones_like(x))
off_diag = (A / (dx ** 2)) * np.ones(len(x) - 1)


'''
SOLVE EIGENVALUE PROBLEM
'''
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
