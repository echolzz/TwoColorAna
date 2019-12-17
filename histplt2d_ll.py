import numpy as np
import matplotlib
# matplotlib.use('QT4Agg')
import matplotlib.pyplot as plt
import module
import matplotlib.cm as cm
import matplotlib.colors as colors
from matplotlib.colors import Normalize
import json
import os
import matplotlib.colors as mcolors
from scipy.optimize import minimize
from scipy.optimize import LinearConstraint
from matplotlib.transforms import Affine2D
import matplotlib.patches as patches
from mpl_toolkits.mplot3d import axes3d
import matplotlib.patches as patches
import matplotlib.axis

main_path = "/media/zezhou/Seagate Expansion Drive/McGillResearch/2019Manuscript_Analysis/Analysis/datafterlinearshift/llambda/"
cleanmode = 1 # 1-cleaned data. The roi.json and tot_file_clean.json files have been saved in ./data folder.
              # 0-raw data. Experimental data before shift to zero.
# Read files
handle1, tot_file = module.bashload(main_path)
handle1, tot_vector = module.bashvector(handle1)
handle1, tot_vec_overlay = module.bashoverlay(handle1)

# Data clean
if cleanmode == 0:
    handle1, roi = module.bashroi(handle1) # ROI selection
    handle1, tot_file_clean = module.bashclean(handle1) # Delete points ouside ROI and attach mask to handle1.
    handle1, tot_file_shift = module.allshift(handle1) # Shift data to zero according to YOYO-3 channel
elif cleanmode == 1:
    os.chdir(main_path+'/data')
    tot_file_clean = json.load(open('tot_file_clean.json')) # data is saved in list format
    for filename in tot_file_clean:
        tot_file_clean[filename] = np.array(tot_file_clean[filename]) # Changing format to array
    handle1.tot_file_shift = tot_file_clean

# Cleaned data re-calculate
handle1, tot_vector_clean = module.bashvector(handle1, mode='clean')
handle1, tot_vec_overlay_clean = module.bashoverlay(handle1, mode='clean')
handle1, tot_pos_overlay_shift = module.bashoverlay(handle1, mode='clean', set='position')

################################## Visualization #########################################

###############
# histogram2d #
###############
# Details of the plot data are in function. The unlisted data are directly from datahandle.
##########################
# lambda-lambda
def ecc0_ll():
    x = np.array([])
    y = np.array([])
    x = np.append(x, handle1.tot_file_shift['ecc0_1_y1x'])
    y = np.append(y, handle1.tot_file_shift['ecc0_1_y1y'])

    # x = np.append(x, handle1.tot_file_shift['ecc0_1_y1x'][1000:3000])
    # y = np.append(y, handle1.tot_file_shift['ecc0_1_y1y'][1000:3000])
    # x = np.append(x, -handle1.tot_file_shift['ecc0_1_y1x'][3000:5000])
    # y = np.append(y, handle1.tot_file_shift['ecc0_1_y1y'][3000:5000])
    x = np.append(x, handle1.tot_file_shift['ecc0_2_y1x'])
    y = np.append(y, handle1.tot_file_shift['ecc0_2_y1y'])

    x = np.append(x, handle1.tot_file_shift['ecc0_1_y3x'])
    y = np.append(y, handle1.tot_file_shift['ecc0_1_y3y'])
    # x = np.append(x, handle1.tot_file_shift['ecc0_1_y3x'][1000:3000])
    # y = np.append(y, handle1.tot_file_shift['ecc0_1_y3y'][1000:3000])
    # x = np.append(x, -handle1.tot_file_shift['ecc0_1_y3x'][3000:5000])
    # y = np.append(y, handle1.tot_file_shift['ecc0_1_y3y'][3000:5000])
    x = np.append(x, handle1.tot_file_shift['ecc0_2_y3x'])
    y = np.append(y, handle1.tot_file_shift['ecc0_2_y3y'])
    # x = x - np.mean(x)
    print('tot_pos_overlay_shift ecc0:' + str(np.mean(x)))
    return x, y
def ecc03_ll():
    # ecc03
    x = np.array([])
    y = np.array([])
    x = np.append(x, handle1.tot_file_shift['ecc03_1_y1x'])
    y = np.append(y, -handle1.tot_file_shift['ecc03_1_y1y'])                                # Plot detail. DO NOT delete.!!!!
    x = np.append(x, handle1.tot_file_shift['ecc03_2_y1x'])
    y = np.append(y, handle1.tot_file_shift['ecc03_2_y1y'])
    x = np.append(x, handle1.tot_file_shift['ecc03_3_y1x'])
    y = np.append(y, handle1.tot_file_shift['ecc03_3_y1y'])
    x = np.append(x, handle1.tot_file_shift['ecc03_4_y1x'])
    y = np.append(y, handle1.tot_file_shift['ecc03_4_y1y'])
    x = np.append(x, handle1.tot_file_shift['ecc03_5_y1x'])
    y = np.append(y, handle1.tot_file_shift['ecc03_5_y1y'])
    x = np.append(x, handle1.tot_file_shift['ecc03_6_y1x'])
    y = np.append(y, handle1.tot_file_shift['ecc03_6_y1y'])

    x = np.append(x, handle1.tot_file_shift['ecc03_1_y3x'])
    y = np.append(y, -handle1.tot_file_shift['ecc03_1_y3y'])  # Plot detail. DO NOT delete.!!!!
    x = np.append(x, handle1.tot_file_shift['ecc03_2_y3x'])
    y = np.append(y, handle1.tot_file_shift['ecc03_2_y3y'])
    x = np.append(x, handle1.tot_file_shift['ecc03_3_y3x'])
    y = np.append(y, handle1.tot_file_shift['ecc03_3_y3y'])
    x = np.append(x, handle1.tot_file_shift['ecc03_4_y3x'])
    y = np.append(y, handle1.tot_file_shift['ecc03_4_y3y'])
    x = np.append(x, handle1.tot_file_shift['ecc03_5_y3x'])
    y = np.append(y, handle1.tot_file_shift['ecc03_5_y3y'])
    x = np.append(x, handle1.tot_file_shift['ecc03_6_y3x'])
    y = np.append(y, handle1.tot_file_shift['ecc03_6_y3y'])

    # x = x - np.mean(x)
    print('tot_pos_overlay_shift ecc03:' + str(np.mean(x)))
    return x, y
def ecc06_ll():
    x = np.array([])
    y = np.array([])
    x = np.append(x, handle1.tot_file_shift['ecc06_1_y1x'])
    y = np.append(y, handle1.tot_file_shift['ecc06_1_y1y'])  # Plot detail. DO NOT delete.!!!!
    x = np.append(x, handle1.tot_file_shift['ecc06_2_y1x'])
    y = np.append(y, handle1.tot_file_shift['ecc06_2_y1y'])
    x = np.append(x, handle1.tot_file_shift['ecc06_3_y1x'])
    y = np.append(y, handle1.tot_file_shift['ecc06_3_y1y'])
    x = np.append(x, handle1.tot_file_shift['ecc06_4_y1x'])
    y = np.append(y, handle1.tot_file_shift['ecc06_4_y1y'])
    x = np.append(x, handle1.tot_file_shift['ecc06_5_y1x'])
    y = np.append(y, handle1.tot_file_shift['ecc06_5_y1y'])
    x = np.append(x, handle1.tot_file_shift['ecc06_6_y1x'])
    y = np.append(y, handle1.tot_file_shift['ecc06_6_y1y'])
    x = np.append(x, handle1.tot_file_shift['ecc06_7_y1x'])
    y = np.append(y, handle1.tot_file_shift['ecc06_7_y1y'])
    x = np.append(x, handle1.tot_file_shift['ecc06_8_y1x'])
    y = np.append(y, handle1.tot_file_shift['ecc06_8_y1y'])
    x = np.append(x, handle1.tot_file_shift['ecc06_9_y1x'])
    y = np.append(y, handle1.tot_file_shift['ecc06_9_y1y'])

    x = np.append(x, handle1.tot_file_shift['ecc06_1_y3x'])
    y = np.append(y, handle1.tot_file_shift['ecc06_1_y3y'])  # Plot detail. DO NOT delete.!!!!
    x = np.append(x, handle1.tot_file_shift['ecc06_2_y3x'])
    y = np.append(y, handle1.tot_file_shift['ecc06_2_y3y'])
    x = np.append(x, handle1.tot_file_shift['ecc06_3_y3x'])
    y = np.append(y, handle1.tot_file_shift['ecc06_3_y3y'])
    x = np.append(x, handle1.tot_file_shift['ecc06_4_y3x'])
    y = np.append(y, handle1.tot_file_shift['ecc06_4_y3y'])
    x = np.append(x, handle1.tot_file_shift['ecc06_5_y3x'])
    y = np.append(y, handle1.tot_file_shift['ecc06_5_y3y'])
    x = np.append(x, handle1.tot_file_shift['ecc06_6_y3x'])
    y = np.append(y, handle1.tot_file_shift['ecc06_6_y3y'])
    x = np.append(x, handle1.tot_file_shift['ecc06_7_y3x'])
    y = np.append(y, handle1.tot_file_shift['ecc06_7_y3y'])
    x = np.append(x, handle1.tot_file_shift['ecc06_8_y3x'])
    y = np.append(y, handle1.tot_file_shift['ecc06_8_y3y'])
    x = np.append(x, handle1.tot_file_shift['ecc06_9_y3x'])
    y = np.append(y, handle1.tot_file_shift['ecc06_9_y3y'])
    # x = x - np.mean(x)
    print('tot_pos_overlay_shift ecc06:' + str(np.mean(x)))
    return x, y
def ecc09_ll():
    x = np.array([])
    y = np.array([])
    x = np.append(x, handle1.tot_file_shift['ecc09_1_y1x'])
    y = np.append(y, handle1.tot_file_shift['ecc09_1_y1y'])
    x = np.append(x, handle1.tot_file_shift['ecc09_2_y1x'])
    y = np.append(y, handle1.tot_file_shift['ecc09_2_y1y'])
    x = np.append(x, handle1.tot_file_shift['ecc09_3_y1x'])
    y = np.append(y, handle1.tot_file_shift['ecc09_3_y1y'])
    x = np.append(x, handle1.tot_file_shift['ecc09_4_y1x'])
    y = np.append(y, handle1.tot_file_shift['ecc09_4_y1y'])                             # Plot detail. DO NOT delete.!!!!
    x = np.append(x, handle1.tot_file_shift['ecc09_5_y1x'])
    y = np.append(y, handle1.tot_file_shift['ecc09_5_y1y'])
    x = np.append(x, handle1.tot_file_shift['ecc09_6_y1x'])
    y = np.append(y, handle1.tot_file_shift['ecc09_6_y1y'])
    x = np.append(x, handle1.tot_file_shift['ecc09_7_y1x'])
    y = np.append(y, handle1.tot_file_shift['ecc09_7_y1y'])
    # x = np.append(x, handle1.tot_file_shift['ecc09_8_y1x'])
    # y = np.append(y, handle1.tot_file_shift['ecc09_8_y1y'])
    # x = np.append(x, -handle1.tot_file_shift['ecc09_9_y1x'])
    # y = np.append(y, handle1.tot_file_shift['ecc09_9_y1y'])

    x = np.append(x, handle1.tot_file_shift['ecc09_1_y3x'])
    y = np.append(y, handle1.tot_file_shift['ecc09_1_y3y'])
    x = np.append(x, handle1.tot_file_shift['ecc09_2_y3x'])
    y = np.append(y, handle1.tot_file_shift['ecc09_2_y3y'])
    x = np.append(x, handle1.tot_file_shift['ecc09_3_y3x'])
    y = np.append(y, handle1.tot_file_shift['ecc09_3_y3y'])
    x = np.append(x, handle1.tot_file_shift['ecc09_4_y3x'])
    y = np.append(y, handle1.tot_file_shift['ecc09_4_y3y'])  # Plot detail. DO NOT delete.!!!!
    x = np.append(x, handle1.tot_file_shift['ecc09_5_y3x'])
    y = np.append(y, handle1.tot_file_shift['ecc09_5_y3y'])
    x = np.append(x, handle1.tot_file_shift['ecc09_6_y3x'])
    y = np.append(y, handle1.tot_file_shift['ecc09_6_y3y'])
    x = np.append(x, handle1.tot_file_shift['ecc09_7_y3x'])
    y = np.append(y, handle1.tot_file_shift['ecc09_7_y3y'])
    # x = np.append(x, handle1.tot_file_shift['ecc09_8_y3x'])
    # y = np.append(y, handle1.tot_file_shift['ecc09_8_y3y'])
    # x = np.append(x, handle1.tot_file_shift['ecc09_9_y3x'])
    # y = np.append(y, handle1.tot_file_shift['ecc09_9_y3y'])
    return x, y
def ecc095_ll():
    x1 = np.array([])
    y1 = np.array([])
    x1 = np.append(x1, handle1.tot_file_shift['ecc095_1_y1x'])
    y1 = np.append(y1, handle1.tot_file_shift['ecc095_1_y1y'])
    x1 = np.append(x1, handle1.tot_file_shift['ecc095_2_y1x'])
    y1 = np.append(y1, handle1.tot_file_shift['ecc095_2_y1y'])

    x1 = np.append(x1, -handle1.tot_file_shift['ecc095_1_y3x'])
    y1 = np.append(y1, handle1.tot_file_shift['ecc095_1_y3y'])
    x1 = np.append(x1, handle1.tot_file_shift['ecc095_2_y3x'])
    y1 = np.append(y1, handle1.tot_file_shift['ecc095_2_y3y'])
    return  x1, y1
def ecc098_ll():
    x1 = np.array([])
    y1 = np.array([])
    x1 = np.append(x1, handle1.tot_file_shift['ecc098_1_y1x']) #1
    y1 = np.append(y1, handle1.tot_file_shift['ecc098_1_y1y'])

    x1 = np.append(x1, handle1.tot_file_shift['ecc098_1_y3x'])  # 1
    y1 = np.append(y1, handle1.tot_file_shift['ecc098_1_y3y'])
    # x1 = x1 - np.mean(x1)
    print('tot_pos_overlay_shift ecc098:'+str(np.mean(x1)))
    return x1, y1
def ecc0995_ll():
# ecc0995(T4-plasmid)
    x1 = np.array([])
    y1 = np.array([])
    x1 = np.append(x1, -handle1.tot_file_shift['ecc0995_1_y1x'])
    y1 = np.append(y1, handle1.tot_file_shift['ecc0995_1_y1y'])
    x1 = np.append(x1, handle1.tot_file_shift['ecc0995_2_y1x'])
    y1 = np.append(y1, handle1.tot_file_shift['ecc0995_2_y1y'])

    x1 = np.append(x1, -handle1.tot_file_shift['ecc0995_1_y3x'])
    y1 = np.append(y1, handle1.tot_file_shift['ecc0995_1_y3y'])
    x1 = np.append(x1, handle1.tot_file_shift['ecc0995_2_y3x'])
    y1 = np.append(y1, handle1.tot_file_shift['ecc0995_2_y3y'])

    return x1, y1

## Cavity overlay
def cav_ecc06():
    a, b = module.ellipse_para(ecc=0)
    n = 1000 # sampling pts
    t = np.linspace(0, 2*np.pi, n)
    x = a * np.cos(t)
    y = b * np.sin(t)
    return x, y

def llhist():
    ###Data setup##########
    x0, y0 = ecc0_ll()
    x1, y1 = ecc03_ll()
    x2, y2 = ecc06_ll()
    x3, y3 = ecc09_ll()

    X = [x0, x1, x2, x3] # Input data array
    Y = [y0, y1, y2, y3]
    # savename = 'Ecc0995_p.eps'


    savename_tot = ['Ecc0_ll.png', 'Ecc03_ll.png', 'Ecc06_ll.png', 'Ecc09_ll.png']
    figtitle_tot = ['Plasmid position distribution Ecc=0', 'Plasmid position distribution Ecc=0.3',
            'Plasmid position distribution Ecc=0.6', 'Plasmid position distribution Ecc=0.9']

    savepath = '/media/zezhou/Se' \
           'agate Expansion Drive/McGillResearch/2019Manuscript_Analysis/Analysis/Plots/llambda/hist/'

    xlim_tot = [10, 10, 10, 10, 10, 10, 10]
    scalebar_tot = np.array(xlim_tot)/10*6.25 # Keep length of the scale bar the same

    # Annotation text
    marker_tot = ['Eccentricity=0', 'Eccentricity=0.3', 'Eccentricity=0.6',
              'Eccentricity=0.9']
    scalelabel_tot = ['1um', '1um', '1um', '1um', '1um', '1um', '1um']

    ###
    bins = 80
    cmap = 'inferno'
    fontsize = 10
    labelsize = 12
    cb_fontsize = 7.5
    ###############
    a = 8
    fig2 = plt.figure(figsize=[a, a]) # figs8ize=[6.4, 4.8]

    #### Do NOT change here. This section changes color ONLY ####
    vmax = 0
    vmin = 1000
    ############################
    for i in range(4):
        x = X[i]
        y = Y[i]
        xlim = xlim_tot[i]

        # Rescaling
        h = np.histogram2d(x, y, bins=[bins, bins], range=[[-xlim, xlim], [-xlim, xlim]], density=True)
        ## scale the color
        sh = h[0][int(bins/2-10):int(bins/2+10), int(bins/2-4):int(bins/2+4)]
        mi = np.min(sh) # smallest probability of the center square
        ma = np.max(h[0]) #largest
        ####################
        if vmin>mi:
            vmin = mi
        if vmax<ma:
            vmax = ma
        print("vmin is:"+str(vmin))
        print("vmax is:" + str(vmax))

    ############################
    xr = [] # xr/yr: xlim and ylim of the red box
    yr = []
    ############################
    for i in range(4):

        ###################
        ## Histgram plot ##
        ###################

        x = X[i]
        y = Y[i]
        xlim = xlim_tot[i]
        figtitle = figtitle_tot[i]
        savename = savename_tot[i]

        width = 0.22
        ax2 = fig2.add_axes([0., 0.7-i*width, width, width])
        ax3 = fig2.add_axes([width, 0.7 - i * width, width, width])
        # Universal plot:
        # norm=mcolors.PowerNorm(0.7)
        if i==0:
            h, xedges, yedges, img = ax2.hist2d(x, y, bins=[bins-15, bins-15], range=[[-xlim, xlim], [-xlim, xlim]],
                                                cmap=cmap, vmin = 0.01, vmax = 0.035, density=True, norm=mcolors.PowerNorm(1))
        else:
            h, xedges, yedges, img = ax2.hist2d(x, y, bins=[bins, bins], range=[[-xlim, xlim], [-xlim, xlim]], cmap=cmap, density=True)
        # axes label
        ax2.set_xlabel(r'Position($\mu$m)', fontsize = fontsize)
        ax2.set_ylabel(r'Position($\mu$m)', fontsize = fontsize)

        # tick location and tick label
        xtick_temp = np.arange(0, xlim, step = 6.25)
        xtick_temp = np.concatenate((-xtick_temp, xtick_temp))
        xtick_temp = np.sort(xtick_temp)
        xtick_temp = np.delete(xtick_temp, len(xtick_temp)/2 - 1 )
        xticks = list(xtick_temp)
        xticklabel = []
        for ticks in xticks:
            xticklabel.append(str(ticks/6.25))
        ax2.set_xticks(xticks)
        ax2.set_yticks(xticks)

        # Tick label. Uncomment below to show unit in um
        ax2.set_xticklabels(xticklabel, fontsize = labelsize)
        ax2.set_yticklabels(xticklabel, fontsize = labelsize)

        # Axis switch
        ax2.axis('off')

        # text comment
        mark = marker_tot[i]
        ax2.text(x = -xlim*0.9, y=xlim*0.8, s=mark, fontsize = labelsize, color='w',weight='bold')

        # scale bar location
        sc = scalebar_tot[i]
        rect = patches.Rectangle((xlim*0.3, -xlim*0.75), width = sc, height=sc/8, fill=True, color = 'w')
        ax2.add_patch(rect)

        ###################
        # scale bar label #
        ###################
        scalelabel = scalelabel_tot[i]
        ax2.text(x=xlim * 0.5, y=-xlim * 0.95, s=scalelabel, fontsize=labelsize)

        ###############
        # Super title #
        ###############
        # fig2.suptitle(r'$\lambda$-DNA distribution in different cavities', fontsize=20, x=0.3)

        #######################
        # Draw the red square #
        #######################
        lc = 0.1
        hc = 0.7
        rect_patch = patches.Rectangle((-lc*xlim, -hc*xlim), lc*2*xlim, hc*2*xlim, linewidth=1, edgecolor='r', facecolor='none', ls='--')
        ax2.add_patch(rect_patch)
        xr.append(lc * xlim)
        yr.append(hc * xlim)

        ########################
        ## cross-section plot ##
        ########################
        xt = xr[i]
        yt = yr[i]
        xmask = (xedges[:-1] > -xt)*(xedges[:-1]<xt)
        ymask = (yedges[:-1] > -yt) * (yedges[:-1] < yt)

        h = np.transpose(h)[ymask,:][:,xmask]
        hsum = np.sum(h, axis=1)
        hrr = np.std(h, axis=1)
        x = np.linspace(-yt, yt, hsum.shape[0])
        # ax3.plot(hsum,x, '-o', color = 'darkviolet')
        ax3.errorbar(hsum, x,xerr=hrr, color='darkviolet', marker='<',capsize=4)
        ax3.set_ylim([-xlim, xlim])
        ax3.set_xlim([0, 0.55])
        #################
        # label setting #
        #################


        ##################
        # position ticks #
        ##################
        xtick = [0, 0.2, 0.4]
        ytick = [-6.25, 0, 6.25]
        ax3.set_xticks(xtick)
        ax3.set_yticks(ytick)
        yticklabels = np.array(ytick)/6.25
        ax3.set_xticklabels(xtick, fontsize = 12)
        ax3.set_yticklabels(yticklabels, fontsize = 12)
        ax3.grid(b=True, linestyle='--')
        ax3.set_ylabel(r'Position($\mu$m)', fontsize = 15, rotation=-90,labelpad=15)

        ##################
        # Set the xlabel #
        ##################
        if i == 0 :
            ax3.set_xlabel('Probability', fontsize = 15)
            ax3.xaxis.set_ticks_position('top')
            ax3.yaxis.set_ticks_position('right')
            ax3.xaxis.set_label_position('top')
            ax3.yaxis.set_label_position('right')
        elif i!=3:
            ax3.xaxis.set_ticks_position('none')
            ax3.yaxis.set_ticks_position('right')
            ax3.yaxis.set_label_position('right')
        elif i==3:
            ax3.xaxis.set_ticks_position('none')
            ax3.xaxis.set_ticklabels(['1','2','3'], visible=False)
            ax3.yaxis.set_ticks_position('right')
            ax3.yaxis.set_label_position('right')
    ######################
    # Universal colorbar #
    ######################
    # cax = fig2.add_axes([0.2, 0.3, 0.025, 0.5])
    # norm = colors.Normalize(vmin=vmin, vmax=vmax)
    # cb = fig2.colorbar(cm.ScalarMappable(norm=norm, cmap=cmap), cax = cax, orientation = 'vertical')
    # cb.ax.tick_params(labelsize=12)
    # cb.set_label('Probability', fontsize = cb_fontsize+5 , horizontalalignment = 'center', rotation=-90, labelpad=15)
    ############################################


    os.chdir(savepath)
    plt.show()
    return
def denplt():
    # Density plot. The bottom two figures
    bins = 80
    fontsize = 13
    labelsize = 7.5
    cb_fontsize = 7.5
    ###############
    width = 0.4
    a = 6
    fig2 = plt.figure(figsize=[a, a / 1.3333])  # figs8ize=[6.4, 4.8]
    ax3 = fig2.add_axes([0.15, 0.1, width, width/1.3333])
    ax4 = fig2.add_axes([0.15, 0.1+ width/1.3333+0.2, width, width/1.3333])

    dataset = [ecc0_ll(), ecc03_ll(), ecc06_ll(), ecc09_ll()]
    r_density = []
    r_edge = []
    theta_density = []
    theta_edge = []
    ### Density calculation ###
    for file in dataset:
        x, y = file
        module.densitycal(handle1, dataset='position', bins=bins, x=x, y=y, debug=True)
        r_density.append(handle1.tot_density_hist['test_density'])
        r_edge.append(handle1.tot_density_hist['test_edge'])
        theta_density.append(handle1.tot_density_hist['test_degdensity'])
        theta_edge.append(handle1.tot_density_hist['test_degedge'])

    ### Plot1 set-up ###
    legend = ['ecc0', 'ecc0.3', 'ecc0.6', 'ecc0.9']
    ## Counting total data number ##
    n_datapts = []
    for file in dataset:
        x, y = file
        n_datapts.append(len(x))
    ################################

    ## Radius/Theta density plot
    for i in range(len(dataset)):
        ### Overlap -pi-0 with 0-pi.
        tmp = theta_density[i] #current density
        tmp[-1] = tmp[0]# off-set the edge(otherwise the boundry will be zero)
        ind = int(3*len(tmp)/4) # off-set the density to -pi/2--3pi/2
        tmp = np.concatenate((tmp[ind:], tmp[:ind]))
        mid_ind = int(len(tmp)/2) ##prepare reverse
        tmp_swap = tmp[:mid_ind][::-1]+tmp[mid_ind:] ## adding tmp(theta)+tmp(pi-theta)
        ############################
        ax3.plot(theta_edge[i][:mid_ind]+np.pi/2, tmp_swap) ##shift x ticks to -pi/2 to pi/2. 0 is center
        ax4.plot(r_edge[i], r_density[i])

    ax3.legend(legend, loc=1)
    ax4.set_ylabel('Probability density', fontsize=fontsize)
    ax4.set_xlabel('Effective radius', fontsize=fontsize)
    ax3.set_xlabel('Theta(rad)', fontsize=fontsize)
    ax3.set_ylabel('Probability density', fontsize=fontsize)
    plt.show()
    return

# TODO: confirm dataset. ecc09 movie.
def swappingplt():
    dataset = ['ecc0', 'ecc03','ecc06','ecc09']
    tot_vector = handle1.tot_vec_overlay_clean
    a = 6.4 # figure size
    # Create a figure and axis
    fig = plt.figure(figsize=[a, a/1.3333333])

    ind = 0
    bins = [8, 7, 9, 9]
    maxrange = [500, 900, 1200, 1800]
    maxtime = np.array(maxrange)/17
    legend = ['Ecc=0', 'Ecc=0.3', 'Ecc=0.6', 'Ecc=0.9']
    threshold = [0.5, 0.5, 0.5, 0.5]
    width = np.array(maxrange)/np.array(bins)*0.9 # bar width
    tot_fit = []
    tot_cov=[]
    for item in dataset:
        r = ind//2
        c = ind%2
        ax = fig.add_axes([0.1+c*0.4, 0.6-r*0.4, 0.3, 0.3])
        data = tot_vector[item+'_dely'] # Have been check. Correct.
        state, time, upthre = module.swapcounter(data, threshhold=threshold[ind])

        # plt.plot(data/np.max(np.abs(data))*1.5)
        # plt.plot(state)
        # plt.plot(upthre*np.ones_like(data)/np.max(np.abs(data))*1.5, '--')
        # plt.plot(-upthre * np.ones_like(data)/np.max(np.abs(data))*1.5, '--')
        # plt.show()

        hist, bin_edge = np.histogram(time, bins=bins[ind], range = [0, maxrange[ind]])
        ax.bar(bin_edge[:-1], hist, align = 'center', width=width[ind], color = 'r', edgecolor = 'k', label=legend[ind])

        # Exp fitting
        if item == 'ecc03':
            fitx_x = bin_edge[:-1]
            fit_para = np.polyfit(fitx_x[:6], np.log(hist[:6]), deg=int(1), full=False, cov=True) # TODO: confinm. Zero has an effect on fitting.
        elif item == 'ecc09':
            fitx_x = bin_edge[:-1]
            fit_para = np.polyfit(fitx_x[:5], np.log(hist[:5]), deg=int(1), full=False, cov=True)
        elif item =='ecc0':
            fitx_x = bin_edge[:-2]
            fit_para = np.polyfit(fitx_x, np.log(hist[:-1]), deg=int(1), full=False, cov=True)
        elif item == 'ecc06':
            fitx_x = bin_edge[:-1]
            fit_para = np.polyfit(fitx_x, np.log(hist), deg=int(1), full=False, cov=True)

        tot_fit.append(fit_para[0])
        tot_cov.append(fit_para[1])
        # plot exponential fitting
        ax.plot(fitx_x, np.exp(fit_para[0][0] * fitx_x + fit_para[0][1]), '--', color='k')

        ax.legend()
        xticklabel = np.arange(0, maxtime[ind],np.floor(maxtime[ind]/3))
        xtick = xticklabel*17
        ax.set_xticks(xtick)
        ax.set_xticklabels(xticklabel)
        ax.set_yscale('log')
        ax.set_xlabel('Dwell time (s)', fontsize=13)
        ax.set_ylabel('Counts', fontsize=13)
        ind += 1
    plt.show()
    ############
    # tau plot #
    ############
    fig = plt.figure(figsize=[6.4, 6.4/1.333])
    ax = fig.add_axes([0.2,0.2,0.3,0.3])
    labelsize = 13
    ticklabelsize = 11
    time = []
    error = []
    for i in range(len(tot_fit)):
        time.append(-1/tot_fit[i][0]/17)
        error.append(1/(tot_fit[i][0]**2)*np.sqrt(tot_cov[i][0][0])/17)
    x = [0,1,2,3]
    y = [0,10,20,30]
    ax.errorbar(x, time, yerr=error, linestyle= 'None',marker = '.', ms=13, capsize=8, color='r')
    ax.set_xlabel('Cavity eccentricity', fontsize=labelsize)
    ax.set_ylabel(r'$\tau$(s)', fontsize=labelsize)
    ax.set_xticks(x)
    ax.set_yticks(y)
    ax.set_xticklabels(['0', '0.3', '0.6', '0.9'])
    ax.tick_params(axis='both', which='both', labelsize=ticklabelsize)
    plt.show()
    ################
    # end tau plot #
    ################
def swappingdemonstration():
    scaletone = True # flag to scale the position value to -1-1 and threshold line, state line
    dataset = ['ecc03']
    tot_vector = handle1.tot_vec_overlay_clean
    a = 4.5  # figure size
    threshlinecolor = 'k'
    statecolor ='b'
    positioncolor = 'r'
    labelsize=15
    ticklabelsize=12
    xticks = [0,50,100,150]
    yticks = [-1,0,1]
    # Create a figure and axis
    fig = plt.figure(figsize=[a, a / 1.3333333])

    width = 0.3
    scale = 1

    data = tot_vector[dataset[0] + '_dely'][:2600]
    if scaletone == True:
        scale = np.max(np.abs(data))
    state, time, thup = module.swapcounter(data, threshhold=0.7)

    timelapse = np.arange(0, len(data))*57.22*1e-3

    ax = fig.add_axes([0.15,0.2,0.7,0.7])
    ax.plot(timelapse, data/scale, color=positioncolor)
    ax.plot(timelapse,state*thup/scale*0.8, color=statecolor, linestyle='--')
    ax.plot(timelapse,thup*np.ones_like(data)/scale, ':', color=threshlinecolor)
    ax.plot(timelapse,-thup * np.ones_like(data)/scale, ':', color=threshlinecolor)
    ax.set_xlabel('Time (s)', fontsize=labelsize)
    ax.set_ylabel('Normalized position', fontsize=labelsize)
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.tick_params(axis='both', which='both', labelsize=ticklabelsize)
    plt.show()
def FreeEnergy():
    def ecc0_ll_del():
        x = np.array([])
        y = np.array([])
        x = np.append(x, handle1.tot_vector_clean['ecc0_1_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc0_1_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc0_2_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc0_2_dely'])
        return x, y
    def ecc03_ll_del():
        # ecc03
        x = np.array([])
        y = np.array([])
        x = np.append(x, handle1.tot_vector_clean['ecc03_1_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc03_1_dely'])  # Plot detail. DO NOT delete.!!!!
        x = np.append(x, handle1.tot_vector_clean['ecc03_2_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc03_2_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc03_3_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc03_3_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc03_4_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc03_4_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc03_5_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc03_5_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc03_6_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc03_6_dely'])

        return x, y
    def ecc06_ll_del():
        x = np.array([])
        y = np.array([])
        x = np.append(x, handle1.tot_vector_clean['ecc06_1_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_1_dely'])  # Plot detail. DO NOT delete.!!!!
        x = np.append(x, handle1.tot_vector_clean['ecc06_2_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_2_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc06_3_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_3_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc06_4_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_4_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc06_5_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_5_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc06_6_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_6_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc06_7_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_7_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc06_8_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_8_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc06_9_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_9_dely'])
        return x, y
    def ecc09_ll_del():
        x = np.array([])
        y = np.array([])
        x = np.append(x, handle1.tot_vector_clean['ecc09_1_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc09_1_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc09_2_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc09_2_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc09_3_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc09_3_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc09_4_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc09_4_dely'])  # Plot detail. DO NOT delete.!!!!
        x = np.append(x, handle1.tot_vector_clean['ecc09_5_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc09_5_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc09_6_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc09_6_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc09_7_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc09_7_dely'])

        return x, y

    dataset = [ecc0_ll_del(), ecc03_ll_del(), ecc06_ll_del(), ecc09_ll_del()]
    xlim_tot = [13, 13, 13, 13, 13, 13, 13]
    scalebar_tot = np.array(xlim_tot) / 10 * 6.25  # Keep length of the scale bar the same

    # Annotation text
    marker_tot = ['Eccentricity=0', 'Eccentricity=0.3', 'Eccentricity=0.6',
                  'Eccentricity=0.9']
    scalelabel_tot = ['1um', '1um', '1um', '1um', '1um', '1um', '1um']

    ###
    bins = 80
    labelsize = 20
    ticklabelsize = 18
    width =0.2
    widthscale = 4 # width = widthscale*height
    zlim = [5,8]
    ###############
    a = 6
    fig2 = plt.figure(figsize=[a*widthscale, a ])  # figs8ize=[6.4, 4.8]

    ############################
    epsilon=2e-3 #To adress the infi problem
    # epsilon = 1e-16
    colormap = ['Reds_r', 'Reds_r', 'Reds_r', 'Reds_r']
    for i in range(4):
        x,y= dataset[i]
        xlim = xlim_tot[i]
        # Universal plot:
        weights = np.ones_like(x) / len(x)
        h, xedges, yedges, = np.histogram2d(y, x, bins=[bins, bins], range=[[-xlim, xlim], [-xlim, xlim]], weights=weights)
        fe = -np.log(h+epsilon)
        X, Y = np.meshgrid(xedges[:-1], yedges[:-1])
        ax3 = fig2.gca(projection='3d', position=[0.05+i*width*1.1,0.3,width,width*widthscale/2], azim=-50, elev=12)
        ax3.zaxis._axinfo['juggled'] = (1, 2, 0)# change the position of zaxis. 1:left, 0:right. I don't know why.
        ax3.set_zticks([5, 6, 7])
        if i==0:
            ax3.set_zticklabels(['5', '6', '7'])
            tt = ax3.set_zlabel('Free energy\n'
                                r'($k_B$T)', fontsize=labelsize)
            tt.set_rotation(s=0) # Seems not working

        xwall = np.min(fe+1.5, axis=0)
        ywall = np.min(fe+1.5, axis=1)
        #############################
        # Surf and plot on the wall #
        #############################
        surf = ax3.plot_surface(X,Y,fe+0.5,cmap=colormap[i], alpha=0.8)
        ax3.contourf(X, Y, fe+0.6, zdir='z', cmap=colormap[i], offset=zlim[0])
        ax3.plot3D(xs=xedges[5:-5], ys=xlim*np.ones_like(yedges[5:-5]), zs=xwall[5:-4], color='r',ls='--',marker='.')
        ax3.plot3D(xs=-xlim * np.ones_like(yedges[5:-5]), ys=yedges[5:-5], zs=ywall[5:-4], color='r', ls='--', marker ='.')
        ###############
        # end plot ####
        ###############
        # axes label
        xticklabels = [-1, 0, 1]
        xticks = np.array(xticklabels) * 6.25
        ax3.set_xticks(xticks)
        ax3.set_yticks(xticks)
        ax3.set_zlim(zlim)
        test=ax3.zaxis.get_ticks_position()
        ax3.zaxis.set_ticks_position('top')
        ax3.set_xticklabels(xticklabels)
        ax3.set_yticklabels(xticklabels)
        ax3.set_zticklabels([''], visible=False)
        ax3.set_xlabel("X-Position \n"
                       r"($\mu$m)", fontsize=labelsize, labelpad=25)
        ax3.set_ylabel("Y-Position \n "
                       r"($\mu$m)", fontsize=labelsize, labelpad=25)

        ax3.tick_params(axis='x', labelsize=ticklabelsize)
        ax3.tick_params(axis='y', labelsize=ticklabelsize)
        # tick location and tick label

    plt.show()
def rthetaplt():
    vec = handle1.tot_vec_overlay_clean
    dataset = ['ecc0', 'ecc03', 'ecc06', 'ecc09']
    width = 0.22
    labelsize = 15
    ticklabelsize = 12
    startheight = 0.7  # start point of plotting
    color = 'r'
    edgecolor = 'k'

    abins = 10
    alpha = 1
    ahistylim = [0, 0.4]
    axticklabels = ['0', r'$\pi$']
    axticks = [0, np.pi]
    ayticks = np.linspace(0,ahistylim[1],3) # 2 ticks

    rbins = 15
    rhistylim = [0, 0.3]
    rhist_xlim = 1.2
    rxticks = np.linspace(0, rhist_xlim ,2)
    rxextend = 0.12
    rxlim = 1.5+rxextend
    ryticks = np.linspace(0, rhistylim[1], 3)  # 2 ticks
    rlpha = 0.6

    fig = plt.figure()
    idx = 0
    rtot = []
    xtot = []
    xrr = []
    ytot = []
    yrr = []
    rrr = []
    for item in dataset:
        delx = vec[item+'_delx']
        dely = vec[item + '_dely']
        angle = np.arctan2(abs(dely), delx)
        axa = fig.add_axes([0.1+idx*width, startheight,  width, width])


        #############################
        # Angular distribution plot #
        weights = np.ones_like(angle)/float(len(angle))
        axa.hist(angle, bins=abins, alpha=alpha, weights=weights, color=color, ec=edgecolor)
        if idx != 0:
            axa.tick_params(axis='y', which='both', labelleft=False)
        if idx ==0:
            axa.set_ylabel('Probability', fontsize = labelsize)
            axa.set_yticks(ayticks)
            axa.tick_params(axis='y', which='both', labelright=False, labelsize=ticklabelsize)
        axa.set_xlabel(r'$\theta$(rad)', fontsize = labelsize)
        axa.set_xticks(axticks)
        axa.set_xticklabels(axticklabels, fontsize = ticklabelsize)
        axa.set_ylim(ahistylim)

        # end #
        #######

        ############################
        # Radius distribution plot #
        axr = fig.add_axes([0.102 + idx * width, startheight-width-0.12, width, width])
        weights = np.ones_like(delx) / float(len(delx))
        r = np.sqrt(delx**2+dely**2)/6.25
        rrr.append(np.std(r)/np.sqrt(len(r)))
        rtot.append(np.mean(r))
        xtot.append(np.mean(np.abs(delx)/6.25))
        xrr.append(np.std(np.abs(delx))/np.sqrt(len(delx)))
        ytot.append(np.mean(np.abs(dely)/6.25))
        yrr.append(np.std(np.abs(dely)) / np.sqrt(len(dely)))
        if idx != 0:
            axr.tick_params(axis='y', which='both', labelleft=False)
            axr.set_ylabel('Probability', visible=False)
        axr.hist(np.abs(delx)/6.25, bins=rbins, range= [rxticks[0], 1.5], alpha=rlpha, weights=weights, color=color, ec=edgecolor)
        axr.hist(np.abs(dely)/6.25, bins=rbins, range=[rxticks[0], 1.5], alpha=rlpha, weights=weights, color='b', ec=edgecolor)
        axr.hist(r, bins=rbins, range=[rxticks[0], 1.5], alpha=rlpha, weights=weights, color='y', ec=edgecolor)

        axr.set_xticks(rxticks)
        axr.tick_params(axis='x', which='both', labelsize=ticklabelsize)
        axr.set_yticks(ryticks)
        axr.set_xlim([-rxextend, rxlim])
        axr.set_xlabel(r'Length($\mu$m)',fontsize=labelsize)
        if idx==0:
            axr.legend(['Short axis', 'Long axis', 'Full length'], loc=2, labelspacing=0.1)
        axr.set_ylabel('Probability', fontsize=labelsize)
        # end #
        #######
        idx += 1
    plt.show()
    # x = [0, 0.3, 0.6, 0.9]
    # plt.errorbar(x, xtot, yerr=xrr)
    # plt.errorbar(x, ytot, yerr=yrr)
    # plt.errorbar(x, rtot, yerr=rrr)
    # plt.legend(['short axis', 'long axis', 'length'])
    # plt.ylabel('Length(um)')
    # plt.xlabel('Eccentricity')
    # plt.show()
def vecrosscorr_cut(avg_frames):
    # cross correlation of delx and dely.
    def ecc0_ll_del():
        x = np.array([])
        y = np.array([])
        x = np.append(x, handle1.tot_vector_clean['ecc0_1_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc0_1_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc0_2_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc0_2_dely'])
        return x, y
    def ecc03_ll_del():
        # ecc03
        x = np.array([])
        y = np.array([])
        x = np.append(x, handle1.tot_vector_clean['ecc03_1_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc03_1_dely'])  # Plot detail. DO NOT delete.!!!!
        x = np.append(x, handle1.tot_vector_clean['ecc03_2_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc03_2_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc03_3_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc03_3_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc03_4_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc03_4_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc03_5_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc03_5_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc03_6_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc03_6_dely'])

        return x, y
    def ecc06_ll_del():
        x = np.array([])
        y = np.array([])
        x = np.append(x, handle1.tot_vector_clean['ecc06_1_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_1_dely'])  # Plot detail. DO NOT delete.!!!!
        x = np.append(x, handle1.tot_vector_clean['ecc06_2_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_2_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc06_3_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_3_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc06_4_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_4_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc06_5_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_5_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc06_6_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_6_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc06_7_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_7_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc06_8_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_8_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc06_9_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_9_dely'])
        return x, y
    def ecc09_ll_del():
        x = np.array([])
        y = np.array([])
        x = np.append(x, handle1.tot_vector_clean['ecc09_1_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc09_1_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc09_2_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc09_2_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc09_3_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc09_3_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc09_4_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc09_4_dely'])  # Plot detail. DO NOT delete.!!!!
        x = np.append(x, handle1.tot_vector_clean['ecc09_5_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc09_5_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc09_6_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc09_6_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc09_7_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc09_7_dely'])

        return x, y

    def ecc0(frames):
        frames = avg_frames
        y1x = []
        y1y = []
        y3x = []
        y3y = []
        iter = 0
        for item in handle1.tot_file_shift:
            if 'ecc0_' in item:
                iter += 1
        iter = int(iter / 4)
        for k in range(iter):
            y1x_tmp = 'ecc0_' + str(k + 1) + '_y1x'
            y1y_tmp = 'ecc0_' + str(k + 1) + '_y1y'
            y3x_tmp = 'ecc0_' + str(k + 1) + '_y3x'
            y3y_tmp = 'ecc0_' + str(k + 1) + '_y3y'
            tot = np.floor_divide(len(handle1.tot_file_shift[y1x_tmp]), frames)
            for i in range(tot):
                y1x.append(handle1.tot_file_shift[y1x_tmp][i * frames:(i + 1) * frames])
                y1y.append(handle1.tot_file_shift[y1y_tmp][i * frames:(i + 1) * frames])
                y3x.append(handle1.tot_file_shift[y3x_tmp][i * frames:(i + 1) * frames])
                y3y.append(handle1.tot_file_shift[y3y_tmp][i * frames:(i + 1) * frames])
        return y1x, y1y, y3x, y3y
    def ecc0cross():
        y1x, y1y, y3x, y3y = ecc0(avg_frames)
        cross = []
        for i in range(len(y1x)):
            a = corr_fix(np.correlate(np.abs(y1x[i]-y3x[i])-np.mean(np.abs(y1x[i]-y3x[i])), np.abs((y1y[i]-y3y[i]))-np.mean(np.abs((y1y[i]-y3y[i]))), mode='full'))
            cross.append(a)
        return cross
    def ecc03(frames):
        frames = avg_frames
        y1x = []
        y1y = []
        y3x = []
        y3y = []
        iter = 0
        for item in handle1.tot_file_shift:
            if 'ecc03_' in item:
                iter += 1
        iter = int(iter / 4)
        for k in range(iter):
            y1x_tmp = 'ecc03_' + str(k + 1) + '_y1x'
            y1y_tmp = 'ecc03_' + str(k + 1) + '_y1y'
            y3x_tmp = 'ecc03_' + str(k + 1) + '_y3x'
            y3y_tmp = 'ecc03_' + str(k + 1) + '_y3y'
            tot = np.floor_divide(len(handle1.tot_file_shift[y1x_tmp]), frames)
            for i in range(tot):
                y1x.append(handle1.tot_file_shift[y1x_tmp][i * frames:(i + 1) * frames])
                y1y.append(handle1.tot_file_shift[y1y_tmp][i * frames:(i + 1) * frames])
                y3x.append(handle1.tot_file_shift[y3x_tmp][i * frames:(i + 1) * frames])
                y3y.append(handle1.tot_file_shift[y3y_tmp][i * frames:(i + 1) * frames])
        return y1x, y1y, y3x, y3y
    def ecc03cross():
        y1x, y1y, y3x, y3y = ecc03(avg_frames)
        cross = []
        for i in range(len(y1x)):
            a = corr_fix(np.correlate(np.abs(y1x[i]-y3x[i])-np.mean(np.abs(y1x[i]-y3x[i])), np.abs((y1y[i]-y3y[i]))-np.mean(np.abs((y1y[i]-y3y[i]))), mode='full'))
            cross.append(a)
        return cross
    def ecc06(frames):
        frames = avg_frames
        y1x = []
        y1y = []
        y3x = []
        y3y = []
        iter = 0
        for item in handle1.tot_file_shift:
            if 'ecc06_' in item:
                iter += 1
        iter = int(iter / 4)
        for k in range(iter):
            y1x_tmp = 'ecc06_' + str(k + 1) + '_y1x'
            y1y_tmp = 'ecc06_' + str(k + 1) + '_y1y'
            y3x_tmp = 'ecc06_' + str(k + 1) + '_y3x'
            y3y_tmp = 'ecc06_' + str(k + 1) + '_y3y'
            tot = np.floor_divide(len(handle1.tot_file_shift[y1x_tmp]), frames)
            for i in range(tot):
                y1x.append(handle1.tot_file_shift[y1x_tmp][i * frames:(i + 1) * frames])
                y1y.append(handle1.tot_file_shift[y1y_tmp][i * frames:(i + 1) * frames])
                y3x.append(handle1.tot_file_shift[y3x_tmp][i * frames:(i + 1) * frames])
                y3y.append(handle1.tot_file_shift[y3y_tmp][i * frames:(i + 1) * frames])
        return y1x, y1y, y3x, y3y
    def ecc06cross():
        y1x, y1y, y3x, y3y = ecc06(avg_frames)
        cross = []
        for i in range(len(y1x)):
            a = corr_fix(np.correlate(np.abs(y1x[i]-y3x[i])-np.mean(np.abs(y1x[i]-y3x[i])), np.abs((y1y[i]-y3y[i]))-np.mean(np.abs((y1y[i]-y3y[i]))), mode='full'))
            cross.append(a)
        return cross

    def ecc09(frames):
        frames = avg_frames
        y1x = []
        y1y = []
        y3x = []
        y3y = []
        iter = 0
        for item in handle1.tot_file_shift:
            if 'ecc09_' in item:
                iter += 1
        iter = int(iter / 4)
        for k in range(iter):
            y1x_tmp = 'ecc09_' + str(k + 1) + '_y1x'
            y1y_tmp = 'ecc09_' + str(k + 1) + '_y1y'
            y3x_tmp = 'ecc09_' + str(k + 1) + '_y3x'
            y3y_tmp = 'ecc09_' + str(k + 1) + '_y3y'
            tot = np.floor_divide(len(handle1.tot_file_shift[y1x_tmp]), frames)
            for i in range(tot):
                y1x.append(handle1.tot_file_shift[y1x_tmp][i * frames:(i + 1) * frames])
                y1y.append(handle1.tot_file_shift[y1y_tmp][i * frames:(i + 1) * frames])
                y3x.append(handle1.tot_file_shift[y3x_tmp][i * frames:(i + 1) * frames])
                y3y.append(handle1.tot_file_shift[y3y_tmp][i * frames:(i + 1) * frames])
        return y1x, y1y, y3x, y3y
    def ecc09cross():
        y1x, y1y, y3x, y3y = ecc09(avg_frames)
        cross = []
        for i in range(len(y1x)):
            a = corr_fix(np.correlate(np.abs(y1x[i]-y3x[i])-np.mean(np.abs(y1x[i]-y3x[i])), np.abs((y1y[i]-y3y[i]))-np.mean(np.abs((y1y[i]-y3y[i]))), mode='full'))
            cross.append(a)
        return cross
    def corr_fix(corr):
        m = len(corr)
        u = np.arange(1, (m + 1) / 2 + 1)
        n = np.concatenate((u, np.arange((m + 1) / 2 - 1, 0, -1)))
        return corr / n
    def corr_crop(corr, ftot):
        # crop certain number of frames in correlation
        m = len(corr)
        mid = (m+1)/2.0
        return corr[int(mid-ftot):int(mid+ftot)]
    def corr_sz(corr):
        #set the lag time to zero by average the two arms
        m = len(corr)
        mid = int(m/2)
        return 0.5*(np.flip(corr[:mid])+corr[mid:])

    ##################
    # Setting section#
    ##################
    avg_frames = avg_frames # number of lag point in correlation
    figsize = 6.4
    labelsize = 15
    ticklabelsize = 13
    width = 0.4
    mag = 1e1
    err = []
    ###############
    # end setting #
    ###############
    dataset = [ecc0cross(), ecc03cross(), ecc06cross(), ecc09cross()] #
    fig = plt.figure(figsize=[figsize, figsize/1.333333])
    ax = fig.add_axes([0.15, 0.15, width, width])
    for i, item in enumerate(dataset):
        cross = item
        m_cross = np.mean(cross, axis=0)
        err.append(np.std(cross, axis=0)/np.sqrt(len(cross)))
        m_cross = m_cross/np.max(np.abs(m_cross))*mag
        ax.plot(m_cross, label=str(i))
    ax.legend()

    ax.set_yscale( value="symlog")
    plt.show()
    return err

def vecrosscorr_together():
    def ecc0_ll_del():
        x = np.array([])
        y = np.array([])
        x = np.append(x, handle1.tot_vector_clean['ecc0_1_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc0_1_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc0_2_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc0_2_dely'])
        return x, y
    def ecc03_ll_del():
        # ecc03
        x = np.array([])
        y = np.array([])
        x = np.append(x, handle1.tot_vector_clean['ecc03_1_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc03_1_dely'])  # Plot detail. DO NOT delete.!!!!
        x = np.append(x, handle1.tot_vector_clean['ecc03_2_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc03_2_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc03_3_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc03_3_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc03_4_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc03_4_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc03_5_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc03_5_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc03_6_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc03_6_dely'])

        return x, y
    def ecc06_ll_del():
        x = np.array([])
        y = np.array([])
        x = np.append(x, handle1.tot_vector_clean['ecc06_1_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_1_dely'])  # Plot detail. DO NOT delete.!!!!
        x = np.append(x, handle1.tot_vector_clean['ecc06_2_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_2_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc06_3_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_3_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc06_4_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_4_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc06_5_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_5_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc06_6_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_6_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc06_7_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_7_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc06_8_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_8_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc06_9_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc06_9_dely'])
        return x, y
    def ecc09_ll_del():
        x = np.array([])
        y = np.array([])
        x = np.append(x, handle1.tot_vector_clean['ecc09_1_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc09_1_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc09_2_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc09_2_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc09_3_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc09_3_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc09_4_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc09_4_dely'])  # Plot detail. DO NOT delete.!!!!
        x = np.append(x, handle1.tot_vector_clean['ecc09_5_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc09_5_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc09_6_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc09_6_dely'])
        x = np.append(x, handle1.tot_vector_clean['ecc09_7_delx'])
        y = np.append(y, handle1.tot_vector_clean['ecc09_7_dely'])

        return x, y

    def corr_fix(corr):
        m = len(corr)
        u = np.arange(1, (m + 1) / 2 + 1)
        n = np.concatenate((u, np.arange((m + 1) / 2 - 1, 0, -1)))
        return corr / n
    def corr_crop(corr, ftot):
        # crop certain number of frames in correlation
        m = len(corr)
        mid = (m+1)/2.0
        return corr[int(mid-ftot):int(mid+ftot)]
    def corr_sz(corr):
        #set the lag time to zero by average the two arms
        m = len(corr)
        mid = int(m/2)
        return 0.5*(np.flip(corr[:mid])+corr[mid:])

    ##################
    # Setting section#
    ##################
    ftot = 220 # number of lag point in correlation
    figsize = 6.4
    labelsize = 15
    ticklabelsize = 13
    width = 0.6
    mag = 1
    markers =['o', 'v', '^', 's']
    markersize = 5
    errcapsize = 2
    fit_frame_ini = [7, 19, 27, 21] #initial of the first hal exp fitting
    fit_frame_total_s = [20, 45, 70, 155] # entire frames for two-exp fitting
    fps = 17.5
    dashwidth = 2
    alpha_err = 0.8
    label = ['Ecc=0', 'Ecc=0.3', 'Ecc=0.6', 'Ecc=0.9']
    datacolor =['red', 'limegreen', 'royalblue', 'mediumorchid']
    fitcolor = ['darkred', 'darkgreen', 'darkblue', 'purple']
    fontsize = 20
    yticks = [-1, -0.5, 0, 0.5]
    ext = 0.2
    # epsilon = 1e-6
    # tgv = 1e16 # penalty for constraint(fit_ini have to smaller than fit_total)
    ###############
    # end setting #
    ###############
    dataset = [ecc0_ll_del(), ecc03_ll_del(), ecc06_ll_del(), ecc09_ll_del()] #
    err = vecrosscorr_cut(ftot)
    fig = plt.figure(figsize=[figsize, figsize/1.333333])
    ax = fig.add_axes([0.2, 0.2, width, width])
    ax2 = fig.add_axes([0.2+width/1.8, 0.2+width/10, width/2.5, width/2.5])
    for i, item in enumerate(dataset):
        x, y = item
        cross = corr_fix(np.correlate(np.abs(x)-np.mean(np.abs(x)), np.abs(y)-np.mean(np.abs(y)), mode='full'))
        cross = corr_crop(cross, ftot)
        cross = corr_sz(cross)

        cross = cross/np.max(np.abs(cross))*mag
        er = corr_sz(np.append(err[i],0))
        x = np.arange(0, ftot)/fps
        ax.errorbar(x, cross, yerr=er*mag,zorder=0, color = datacolor[i], label=label[i], errorevery=5, linestyle = '-', marker='None',capsize=errcapsize, markersize=markersize, alpha=alpha_err)
        ax2.errorbar(x, -cross, yerr=er * mag, zorder=0, color=datacolor[i], label=label[i], errorevery=1, linestyle='None',
                    marker=markers[i], capsize=errcapsize, markersize=markersize, alpha=alpha_err)

        ################
        # 2exp fitting #
        ################
        # first part
        fit_frame = int(fit_frame_ini[i])
        xt = x[:fit_frame]
        yt = cross[:fit_frame]
        fit = np.polyfit(xt, np.log(np.abs(yt)), deg=int(1))

        ax.plot(xt, -np.exp(fit[0]*xt+fit[1]), '--', linewidth = dashwidth, zorder=2, color=fitcolor[i])
        ax2.plot(xt, np.exp(fit[0] * xt + fit[1]), '--', linewidth=dashwidth, zorder=2, color=fitcolor[i])
        # second part
        if i ==2:
            xt = x[fit_frame + 2: fit_frame_total_s[i]]
            yt = cross[fit_frame + 2: fit_frame_total_s[i]]
        else:
            xt = x[fit_frame + 1: fit_frame_total_s[i]]
            yt = cross[fit_frame+1: fit_frame_total_s[i]]
        fit2 = np.polyfit(xt, np.log(np.abs(yt)), deg=int(1))

        ax.plot(xt, -np.exp(fit2[0] * xt+fit2[1]), '-', linewidth = dashwidth, zorder=2,color=fitcolor[i] )
        ax2.plot(xt, np.exp(fit2[0] * xt + fit2[1]), '-', linewidth=dashwidth, zorder=2, color=fitcolor[i])
        ####################
        # end 2exp fitting #
        ####################



        # def loss(fit_frame):                    # for testing the proper frame_ini value
        #     fit_frame = int(fit_frame)
        #     xt = x[:fit_frame]
        #     yt = cross[:fit_frame]
        #     fit = np.polyfit(xt, np.log(np.abs(yt)), deg=int(0))
        #     res = np.sum((np.polyval(fit, xt)-np.log(np.abs(yt)))**2)
        #     xt = x[fit_frame:fit_frame_total]
        #     yt = cross[fit_frame:fit_frame_total]
        #     fit2 = np.polyfit(xt, np.log(np.abs(yt)), deg=int(1))
        #     res2 = np.sum((np.polyval(fit2, xt) - np.log(np.abs(yt))) ** 2)
        #     return res+res2
    # ax.plot(x,-np.ones_like(x) * 0.1*mag, 'k--')
    # ax.legend()
    # ax.set_yscale( value="symlog")
    ax.set_xlabel('Lag time (s)', fontsize=fontsize)
    ax.set_ylabel('Normalize correlation \nfunction (A.U.)', fontsize=fontsize)
    ax.set_ylim([yticks[0]-ext, yticks[-1]+ext])
    ax.set_yticks(yticks)
    ax.legend(loc=2)
    ax.tick_params(axis='both', labelsize=ticklabelsize)
    rect = patches.Rectangle((0, -0.75), width=2, height=(yticks[-1]-yticks[0])*0.4, fill=False, linestyle='--', color='r', linewidth =dashwidth-0.5)
    ax.add_patch(rect)

    ax2.set_ylim([0.1, 1])
    ax2.set_xlim([-0.1, 2.1])
    ax2.set_yscale('log')
    ax2.invert_yaxis()
    ax2.set_yticks([0.1, 1])
    ax2.set_yticklabels(['-0.1', '-1.0'])
    ax2.tick_params(axis='both', labelsize=ticklabelsize)
    ax2.set_xlabel('Lag time (s)',fontsize=labelsize-1, labelpad=-15)
    ax2.set_ylabel('Correlation', fontsize=labelsize-1, labelpad=-10)
    plt.show()
vecrosscorr_together()