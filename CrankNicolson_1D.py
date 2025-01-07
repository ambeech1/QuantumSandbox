# import libraries
import numpy as np
import scipy.constants as const
from scipy.sparse import diags
from scipy.linalg import solve_banded
from scipy import linalg as la
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.animation import FuncAnimation
matplotlib.use('TkAgg')

from scipy.sparse.linalg import bicgstab

'''
IMPORTANT VALUES
'''

# constants
hbar = 1
m = 0.5
i = 1j
pi = const.pi

# space-time parameters
t_0 = 0
t_1 = 1
n_t = 1001

x_0 = -5
x_1 = 5
n_x = 10001

# step sizes
h = (x_1 - x_0) / (n_x - 1)
dt = (t_1 - t_0) / (n_t - 1)

# coordinates
t = np.linspace(t_0, t_1, n_t)
x = np.linspace(x_0, x_1, n_x)

'''
INITIAL CONDITIONS, BOUNDARY CONDITIONS, POTENTIAL
'''
# initial state
psi0 = (0.1 * (np.exp(i * 10 * pi * x)) * np.exp(-3 * x ** 2))

# boundary condition
# multiply B by each step to force boundary to 0
BC = np.ones_like(x)
BC[0] = BC[-1] = 0

# potential
V = 200 * x ** 2

'''
DEFINE MATRICES
'''
# define constants
A = i * hbar / (4 * m)
B = 1 / (2 * i * hbar)
a = 1 + (2 * A * dt / (h ** 2))
b = 1 - (2 * A * dt / (h ** 2))
r = A * dt / (h ** 2)
a0 = B * dt
l = len(x)

# step 1
# matA * psi(t + 1) = matB * psi(t)
diagA = (np.ones(l) * a) - (a0 * V)
offDiagA = np.ones(l - 1) * -r
offDiagA[np.arange(n_x - 1, l, n_x)[ : -1]] = 0
bandsA = np.array([np.concatenate((np.array([0]), offDiagA)),
                   diagA,
                   np.concatenate((offDiagA, np.array([0])))])

diagB = (np.ones(l) * b) + (a0 * V)
offDiagB = np.ones(l - 1) * r
diagsB = [diagB, offDiagB, offDiagB]
offsetsB = [0, 1, -1]
sparse_matrixB = diags(diagsB, offsetsB)


'''
SOLVE THE TDSE
'''
# list to store time steps
psi = [psi0 * BC]

# loop
for i in t:
    # matrixA * psi(t + 1/2) = matrixB * psi(t)
    psi0 = sparse_matrixB.dot(psi0)
    psi0 = solve_banded((1, 1), bandsA, psi0) * BC
    # append solution
    psi.append(psi0)

# get real part of solution
psiRe = np.real(psi)


'''
ANIMATE THE SOLUTION
'''
# slowness multiplier
M = 1

# create animation window
fig = plt.figure()
axis = plt.axes(xlim = (x_0, x_1))
curve, = axis.plot(psiRe[0], color = 'blue', lw = 2)

# animation function
def update(frame):
    curve.set_data(x, psiRe[M * frame])
    return curve,

# call animation function
anim = FuncAnimation(fig, update, frames = n_t, interval = dt)

# show animation
plt.show()