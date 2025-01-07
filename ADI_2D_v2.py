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

colors = [(1, 1, 1), (1, 0.8, 0), (0, 0, 0), (0, 1, 0), (1, 1, 1)]
cmap_name = 'black_green_yellow'
cmap = LinearSegmentedColormap.from_list(cmap_name, colors)


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
t_1 = 2
n_t = 1001

xy_0 = -5
xy_1 = 5
n_xy = 601

# step sizes
h = (xy_1 - xy_0) / (n_xy - 1)
dt = (t_1 - t_0) / (n_t - 1)

# coordinates
t = np.linspace(t_0, t_1, n_t)
x = y = np.linspace(xy_0, xy_1, n_xy)
xcoord, ycoord = np.meshgrid(x, y, indexing = 'ij')

'''
INITIAL CONDITIONS, BOUNDARY CONDITIONS, POTENTIAL
'''
# initial state
psi0 = np.exp(i * 3 * pi * xcoord) * np.exp(-(xcoord + 2.5) ** 2) * np.exp(-(ycoord / 2) ** 2)

# boundary condition
# multiply B by each step to force boundary to 0
BC = np.ones_like(xcoord)
BC[xcoord >= -abs(ycoord) + 5] = 0
BC[0, :] = BC[-1, :] = BC[:, 0] = BC[:, -1] = 0
BC_flat = BC.flatten()

# boundary
BND = np.zeros_like(xcoord)
BND[-abs(ycoord) + 4.99 <= xcoord] = 1
BND[-abs(ycoord) + 5.05 <= xcoord] = 0

# potential
V = np.zeros_like(xcoord)


'''
DEFINE MATRICES
'''
# define constants
A = i * hbar / (2 * m)
B = 1 / (i * hbar)
a = A * dt / (h ** 2)
b = B * dt

Xp1 = 1 - (b / 2) * V.flatten()
Xp2 = 1 - (b / 2) * V.flatten('F')
Xm1 = 1 + (b / 2) * V.flatten()
Xm2 = 1 + (b / 2) * V.flatten('F')

l = len(x) ** 2

# step 1
# matA * psi(t + 1/2) = matB * psi(t)
diagA = np.ones(l) * ((Xp1 + a) / np.sqrt(Xp1))
offDiagAup = np.ones(l - 1) * -a / (2 * np.sqrt(Xp1[: -1]))
offDiagAdo = np.ones(l - 1) * -a / (2 * np.sqrt(Xp1[1 :]))
offDiagAup[np.arange(n_xy - 1, l, n_xy)[: -1]] = 0
offDiagAdo[np.arange(n_xy - 1, l, n_xy)[: -1]] = 0
bandsA = np.array([np.concatenate((np.array([0]), offDiagAup)),
                   diagA,
                   np.concatenate((offDiagAdo, np.array([0])))])

diagB = np.ones(l) * ((Xm2 - a) / np.sqrt(Xm2))
offDiagBup = np.ones(l - n_xy) * a / (2 * np.sqrt(Xm2[: -n_xy]))
offDiagBdo = np.ones(l - n_xy) * a / (2 * np.sqrt(Xm2[n_xy :]))
diagsB = [diagB, offDiagBup, offDiagBdo]
offsetsB = [0, n_xy, -n_xy]
sparse_matrixB = diags(diagsB, offsetsB)

# step 2
# matC * psi(t + 1) = matD * psi(t + 1/2)
diagC = np.ones(l) * ((Xp2 + a) / np.sqrt(Xp2))
offDiagCup = np.ones(l - 1) * -a / (2 * np.sqrt(Xp2[: -1]))
offDiagCdo = np.ones(l - 1) * -a / (2 * np.sqrt(Xp2[1 :]))
offDiagCup[np.arange(n_xy - 1, l, n_xy)[: -1]] = 0
offDiagCdo[np.arange(n_xy - 1, l, n_xy)[: -1]] = 0
bandsC = np.array([np.concatenate((np.array([0]), offDiagCup)),
                   diagC,
                   np.concatenate((offDiagCdo, np.array([0])))])

diagD = np.ones(l) * ((Xm1 - a) / np.sqrt(Xm1))
offDiagDup = np.ones(l - n_xy) * a / (2 * np.sqrt(Xm1[: -n_xy]))
offDiagDdo = np.ones(l - n_xy) * a / (2 * np.sqrt(Xm1[n_xy :]))
diagsD = [diagD, offDiagDup, offDiagDdo]
offsetsD = [0, n_xy, -n_xy]
sparse_matrixD = diags(diagsD, offsetsD)


'''
SOLVE THE TDSE
'''
# flatten the initial state
psi0_flat = np.transpose(psi0.flatten() * BC_flat)

# list to store time steps
psi_flat = [psi0_flat]

# loop
for i in t:
    # step 1
    # matrixA * psi(t + 1/2) = matrixB * psi(t)
    psi0_flat = sparse_matrixB.dot(psi0_flat)
    psi0_flat = solve_banded((1, 1), bandsA, psi0_flat) * BC_flat
    # reshape
    psi0_flat = psi0_flat.reshape((n_xy, n_xy))
    psi0_flat = psi0_flat.flatten('F')
    # step 2
    # matrixC * psi(t + 1) = matrixD * psi(t + 1/2)
    psi0_flat = sparse_matrixD.dot(psi0_flat)
    psi0_flat = solve_banded((1, 1), bandsC, psi0_flat)
    # reshape
    psi0_flat = psi0_flat.reshape((n_xy, n_xy), order = 'F')
    psi0_flat = psi0_flat.flatten() * BC_flat
    # append solution
    psi_flat.append(psi0_flat)

# reshape solution
psi = []
for i in psi_flat:
    psi.append(i.reshape((n_xy, n_xy)))
psiRe = np.real(psi)

'''
ANIMATE THE SOLUTION
'''
# speed multiplier
M = 3

# create animation window
fig, ax = plt.subplots()
img = ax.imshow(psiRe[0], cmap = cmap, origin = 'upper')

# animation function
def update(frame):
    img.set_data(psiRe[round(M * frame)] + BND)
    return [img],

# call animation function
anim = FuncAnimation(fig, update, frames = round(n_t / M) - 1, interval = dt)

# show animation
plt.show()