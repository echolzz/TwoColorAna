from scipy.optimize import root
import os
import module
import numpy as np
import matplotlib.pyplot as plt
import module
from scipy.optimize import minimize
from mpl_toolkits.mplot3d import Axes3D
import time

def distance_generation():
    filepath = "/home/zezhou/McGillResearch/2019Manuscript_Analysis/femsimulation/t4concentration/"
    os.chdir(filepath)

    # Change this to loop to process all data
    tmp = "/home/zezhou/McGillResearch/2019Manuscript_Analysis/femsimulation/t4concentration/sampling/ecc0995_sampling.txt"
    data = np.loadtxt(tmp, skiprows=2)  # 1st column: x axis; 2nd column: y axis. 3rd column: z axis
    # Read the coordinate lattice
    x = data[:, 0]
    y = data[:, 1]
    a, b = module.ellipse_para(ecc=0.995)
    wall = np.zeros_like(x)
    # Create the depletion z profile
    for i in range(len(x)):
        xtmp = x[i]
        ytmp = y[i]
        rdis = xtmp ** 2 / a ** 2 + ytmp ** 2 / b ** 2
        if rdis > 1:
            continue

        def depletion(r):
            # r: dist to boundary; x,y: current coordinate of the point of interest; a,b: ecc's parameter
            return xtmp ** 2*(b - r) ** 2 + ytmp ** 2 * (a - r) ** 2 - (a - r) ** 2*(b - r) ** 2

        sol = root(depletion, x0=1e-5, method='lm')
        wall[i] = sol.x
    np.savetxt('ecc0995_rdist.txt', wall)
    plt.plot(wall, 'r')
    plt.show()
    return
def wdf(x):
    ## Using the following local variables to avoid loading everytime ## ADD THESE TO THE MAIN CODE BLOCK BEFORE USING THIS FUNCTION #####
    # rdistpath = "/home/zezhou/McGillResearch/2019Manuscript_Analysis/femsimulation/t4concentration/rdist/ecc0_rdist.txt"
    # simpath = "/home/zezhou/McGillResearch/2019Manuscript_Analysis/femsimulation/t4concentration/sampling/ecc0_sampling.txt"
    # simdata = np.loadtxt(simpath, skiprows=2)
    # a, b = module.ellipse_para(ecc=0)
    #########################################################################################################
    #######################
    # Initial guess value #
    A = x[0]
    rc = x[1]
    B = np.abs(x[2])
    #######################
    tgv=1e30
    # Set the outside probability equal to 0. Here I set t4 concentration to 1e30(tgv) to make sure the particle does not penetrate
    simdata[:, 2] = abs(B)*simdata[:, 2]/np.sum(simdata[:, 2])
    for i in range(len(simdata[:,0])):
        xtmp = simdata[i,0]
        ytmp = simdata[i,1]
        rdis = xtmp**2/a**2+ytmp**2/b**2
        if rdis >= 1.0:
            simdata[i,2]=tgv

    rdistdata = np.loadtxt(rdistpath)
    x_sim = np.array(simdata[:, 0]*100-simdata[0, 0]*100+0.04, dtype=int)
    y_sim = np.array(simdata[:, 1]*100-simdata[0, 1]*100-0.01, dtype=int)
    z_mesh = np.zeros([nx+1,ny+1])
    z_mesh[x_sim, y_sim] = A*np.exp(-rdistdata/np.abs(rc)) + B*simdata[:,2]
    z_mesh[-1,:] = tgv
    z_mesh[:,-1] = tgv
    prob = np.exp(-z_mesh)
    prob = np.transpose(prob/np.sum(prob))
    # plt.imshow(prob)
    # plt.show()
    return prob
def feedthrough(prob, xs, ys, h, x, y):
    # Convert the size of simulation to real data size
    probout = np.zeros_like(h)
    # Edge to center
    xsm, ysm = np.meshgrid(xs, ys)
    for i in range(len(x)-1):
        xl = x[i]  # x left edge
        xr = x[i + 1]  # x right edge
        for j in range(len(y)-1):
            yb = y[j] # y bottom edge
            yt = y[j+1] # y top edge
            maskx = (xsm >= xl)*(xsm<xr)
            masky = (ysm >= yb) * (ysm < yt)
            mask = maskx * masky
            noft = max(np.sum(mask), 1)
            probout[j, i] = np.sum(prob[mask])/noft
    return probout/np.sum(probout)

datapath = "/home/zezhou/McGillResearch/2019Manuscript_Analysis/femsimulation/t4concentration/data/Ecc0995h.txt"
xpath = "/home/zezhou/McGillResearch/2019Manuscript_Analysis/femsimulation/t4concentration/data/Ecc0995x.txt"
ypath = "/home/zezhou/McGillResearch/2019Manuscript_Analysis/femsimulation/t4concentration/data/Ecc0995y.txt"
rdistpath = "/home/zezhou/McGillResearch/2019Manuscript_Analysis/femsimulation/t4concentration/rdist/ecc0995_rdist.txt"
simpath = "/home/zezhou/McGillResearch/2019Manuscript_Analysis/femsimulation/t4concentration/sampling/ecc0995_sampling.txt"
ecc = 0.995 # Eccentricity
xsample = 3.16426 # simulation xlim
ysample = 0.31603		 # simulation ylim
nx = 633 # nofp in x dir.
ny = 64 # nofp in y dir.
sol_ini = [1, 0.1, 1e3] # Initial guess of the solution
wdf_pltflag = 1 # if want to see the check plt of simulation
scale = 6.25 # 6.25pixel/um

# Real data & mesh
h = np.loadtxt(datapath)
h = np.transpose(h/np.sum(h))
x = np.loadtxt(xpath)/scale # xedge from hist
y = np.loadtxt(ypath)/scale # yedge from

# Simulation data & mesh

simdata = np.loadtxt(simpath, skiprows=2)
a, b = module.ellipse_para(ecc=ecc)

xs = np.linspace(-xsample,xsample,nx+1)
ys = np.linspace(-ysample,ysample,ny+1)

# Loss function definition
def lossfunc(ini):
    # Loss function define by 2-norm integration. Can be modified.
    prob = wdf(ini) # Input is initial guess. Sim data loading is manually loaded by changing the filepath in wdf.
    prob = feedthrough(prob, xs, ys, h, x, y)
    global wdf_pltflag
    # Check plot of discrete sim result and data
    if wdf_pltflag == 1:
        plt.imshow(prob, cmap='inferno', aspect='equal')
        print('simu prob sum:'+str(np.sum(prob)))
        plt.show()
        plt.imshow(h, cmap='inferno', aspect='equal')
        print('real data prob sum:' + str(np.sum(h)))
        plt.show()
        wdf_pltflag = 0
    prob_flat = prob.flatten()
    h_flat = h.flatten()
    err = -np.inner(prob_flat, h_flat)/np.sqrt(np.dot(prob_flat, prob_flat))/np.sqrt(np.dot(h_flat,h_flat))
    print('current err:'+str(err))
    print('current norm:'+str(np.sum(prob)))
    return err
# Fitting by scipy.optimize.minimize
def fitting(sol_ini):
    # Initial guess of the solution
    method = 'Nelder-Mead'
    tic = time.clock()
    sol = minimize(lossfunc, x0=sol_ini, method=method)
    toc = time.clock()
    print(sol)
    print(method+"Optimizing time:"+str(toc-tic))
    return
def plt_t4():
    # plt T4 concentration
    t4labelsize=18
    fig1, ax1 = plt.subplots()
    ax1.set_aspect('equal')
    tcf = ax1.tricontourf(simdata[:, 0], simdata[:, 1], simdata[:, 2]/np.max(simdata[:, 2]), cmap='inferno')
    cb = fig1.colorbar(tcf,ticks=[0,0.5,1], shrink = 0.8)
    cb.ax.tick_params(labelsize=t4labelsize)
    cb.set_label('Normalized T4\nconcentration', fontsize = t4labelsize+3 , horizontalalignment = 'center', rotation=-90, labelpad=40)
    ax1.set_xticks([-1, 0, 1])
    ax1.set_xticklabels([-1, 0, 1], fontdict={'fontsize':t4labelsize})
    ax1.set_yticks([-0.8, 0, 0.8])
    ax1.set_yticklabels([-0.8, 0, 0.8], fontdict={'fontsize': t4labelsize})
    ax1.set_xlabel('X-position '
                   r'$(\mu m)$', fontsize=t4labelsize+3)
    ax1.set_ylabel('Y-position '
                   r'$(\mu m)$', fontsize=t4labelsize+3)
    plt.tight_layout()
    plt.show()
    return
def wall_deplt():
    # plt wall_dep concentration
    A = 1
    tau=0.4
    t4labelsize=18
    rdistdata = np.loadtxt(rdistpath)
    fig1, ax1 = plt.subplots()
    ax1.set_aspect('equal')
    tcf = ax1.tricontourf(simdata[:, 0], simdata[:, 1], A*np.exp(-rdistdata/tau), cmap='inferno')
    cb = fig1.colorbar(tcf,ticks=[0,0.5,1], shrink = 0.8)
    cb.ax.tick_params(labelsize=t4labelsize)
    cb.set_label('Normalized potential of \nwall-depletion', fontsize = t4labelsize+3 , horizontalalignment = 'center',
                 rotation=-90, labelpad=50)
    ax1.set_xticks([-1, 0, 1])
    ax1.set_xticklabels([-1, 0, 1], fontdict={'fontsize':t4labelsize})
    ax1.set_yticks([-0.8, 0, 0.8])
    ax1.set_yticklabels([-0.8, 0, 0.8], fontdict={'fontsize': t4labelsize})
    ax1.set_xlabel('X-position '
                   r'$(\mu m)$', fontsize=t4labelsize+3)
    ax1.set_ylabel('Y-position '
                   r'$(\mu m)$', fontsize=t4labelsize+3)
    plt.tight_layout()
    plt.show()
    return

# solu = [4.05125020e+03, 1.81111881e-02, 1.59253676e+02](msq) #ecc0 [2.76774457e+02, 2.56671845e-02, 1.78330790e+02] cosine powell(ini[5.64771037e+02, 2.58437871e-02, 1.75742861e+02])
# solu = [7.10077090e+01, 3.62173229e-02, 1.65740348e+02](msq) #ecc06 [9.44478545e+01, 3.45849684e-02, 1.25645661e+02] cosine
# solu = [ 7.64150614e+01,  3.84291713e-02, 8.58294196e+01] #ecc08 similarity cosine seems fine
# solu = [9.34453036e+01, 2.85212431e-02, 2.26827276e+02] #ecc09 similarity cosine seems fine NM(ini[2.76774457e+02, 2.56671845e-02, 1.78330790e+02])
# solu = [8.28234507e+01, 4.03489311e-02, 9.02669984e+01] #ecc095 NM(ini[9.34453036e+01, 2.85212431e-02, 2.26827276e+02])
# solu = [8.51716326e+01, 3.33622623e-02, 1.18913580e+02] #ecc098 NM(ini[8.28234507e+01, 4.03489311e-02, 1.82669984e+02])
# solu = [1.07219057e+01, 6.36032881e-02, 2.04914741e+02] #ecc0995 NM(solu = [5.07219091e+01, 3.36032794e-02, 1.68160212e+02])
solu = [1.07219057e+01, 6.36032881e-02, 2.04914741e+02]

solution_set = [[2.76774457e+02, 2.56671845e-02, 1.78330790e+02],
                [9.44478545e+01, 3.45849684e-02, 1.25645661e+02],
                [ 7.64150614e+01,  3.84291713e-02, 8.58294196e+01],
                [9.34453036e+01, 2.85212431e-02, 2.26827276e+02],
                [8.28234507e+01, 4.03489311e-02, 9.02669984e+01],
                [8.51716326e+01, 3.33622623e-02, 1.18913580e+02],
                [1.07219057e+01, 6.36032881e-02, 2.04914741e+02]]
# lossfunc(solu)
# prob = wdf(sol_ini)
# prob = feedthrough(prob, xs, ys, h, x, y)
# plt.imshow(prob, cmap='inferno')
# plt.show()
# plt.imshow(h, cmap='inferno')
# plt.show()