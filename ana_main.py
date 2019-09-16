import numpy as np
import matplotlib.pyplot as plt
import module
import matplotlib.cm as cm
import matplotlib.colors as colors
import json
import os

main_path = "D:/McGillResearch/2019Manuscript_Analysis/Analysis/tplasmid"
cleanmode = 1
# Read files
handle, tot_file = module.bashload(main_path)
handle, tot_vector = module.bashvector(handle)
handle, tot_vec_overlay = module.bashoverlay(handle)

# Data clean
if cleanmode == 0:
    # handle, roi = module.bashroi(handle)
    handle, tot_file_clean = module.bashclean(handle)
    handle, tot_file_shift = module.bashshift(handle)
elif cleanmode == 1:
    os.chdir(main_path+'/data')
    tot_file_clean = json.load(open('tot_file_clean.json'))
    for filename in tot_file_clean:
        tot_file_clean[filename] = np.array(tot_file_clean[filename])
    handle.tot_file_clean = tot_file_clean

# Cleaned data re-calculate
handle, tot_vector_clean = module.bashvector(handle, mode='clean')
# handle.tot_vector_clean['ecc03_1_delx'] = handle.tot_vector_clean['ecc03_1_delx']-np.mean(handle.tot_vector_clean['ecc03_1_delx'])
# handle.tot_vector_clean['ecc03_1_dely'] = handle.tot_vector_clean['ecc03_1_dely']-np.mean(handle.tot_vector_clean['ecc03_1_dely'])
handle, tot_vec_overlay_clean = module.bashoverlay(handle, mode='clean')

# Visualization
fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(handle.tot_file_clean['ecc03_1_y1x'], handle.tot_file_clean['ecc03_1_y1y'], '+')
ax.plot(handle.tot_file_clean['ecc03_1_y3x'], handle.tot_file_clean['ecc03_1_y3y'], '+')
ax.legend(['y1', 'y3'])
ax.set_xlim([-12,12])
ax.set_ylim([-12,12])
plt.show()
def temperr():
    ecc09_delx = np.concatenate([handle.tot_vector['ecc09_1_delx'], handle.tot_vector['ecc09_2_delx'],
                                 handle.tot_vector['ecc09_3_delx'], handle.tot_vector['ecc09_4_delx'],
                                 handle.tot_vector['ecc09_5_delx'], handle.tot_vector['ecc09_6_delx'],
                                 handle.tot_vector['ecc09_7_delx'], -handle.tot_vector['ecc09_8_delx'],
                                 handle.tot_vector['ecc09_9_delx']])

    fig = plt.figure()
    ax = fig.add_axes([0.15, 0.15, 0.7, 0.7])
    # ax.hist2d(handle.tot_vec_overlay['ecc09_delx'], handle.tot_vec_overlay['ecc09_dely'], bins = [80, 80], range = [[-10, 10], [-10, 10]])
    # ax.hist2d(np.concatenate([handle.tot_vec_overlay['ecc09_delx'], -handle.tot_vec_overlay['ecc09_delx']]), np.concatenate([handle.tot_vec_overlay['ecc09_dely'],handle.tot_vec_overlay['ecc09_dely']]), bins = [130, 130])
    h, xedges, yedges, img = ax.hist2d(ecc09_delx, handle.tot_vec_overlay['ecc09_dely'], bins = [70, 70], range = [[-10, 10], [-10, 10]])
    # h, xedges, yedges, img = ax.hist2d(handle.tot_vec_overlay['ecc06_delx'], handle.tot_vec_overlay['ecc06_dely'], bins = [70, 70], range = [[-10, 10], [-10, 10]])
    norm = colors.Normalize(vmin = np.amin(h), vmax = np.amax(h))
    cb = fig.colorbar(cm.ScalarMappable(norm=norm), ax = ax)
    cb.set_label('Counts', fontsize = 15, rotation = -90, horizontalalignment = 'center', verticalalignment = 'bottom')
    ax.set_xlabel('Position(pixel)', fontsize = 15)
    ax.set_ylabel('Position(pixel)', fontsize = 15)

    fig2 = plt.figure()
    ax2 = fig2.add_subplot(1,1,1)
    ax2.plot(handle.tot_file['ecc09_1_y3x'], handle.tot_file['ecc09_1_y3y'], '+')
    ax2.plot(handle.tot_file['ecc09_2_y3x'], handle.tot_file['ecc09_2_y3y'], '+')
    # ax2.plot(handle.tot_file['ecc09_3_y3x'], handle.tot_file['ecc09_3_y3y'], '+')
    # ax2.plot(handle.tot_file['ecc09_4_y3x'], handle.tot_file['ecc09_4_y3y'], '+')
    # ax2.plot(handle.tot_file['ecc09_5_y3x'], handle.tot_file['ecc09_5_y3y'], '+')
    # ax2.plot(handle.tot_file['ecc09_6_y3x'], handle.tot_file['ecc09_6_y3y'], '+')
    # ax2.plot(handle.tot_file['ecc09_7_y3x'], handle.tot_file['ecc09_7_y3y'], '+')
    # ax2.plot(handle.tot_file['ecc09_8_y3x'], handle.tot_file['ecc09_8_y3y'], '+')
    ax2.legend(['1', '2'])
    ax2.set_title('T4 shift', fontsize = 15)
    ax2.set_xlabel('Position(pixel)', fontsize = 15)
    ax2.set_ylabel('Position(pixel)', fontsize = 15)

    fig3 = plt.figure()
    ax3 = fig3.add_subplot(1,1,1)
    ax3.plot(handle.tot_file['ecc09_1_y1x'], handle.tot_file['ecc09_1_y1y'], '+')
    ax3.plot(handle.tot_file['ecc09_2_y1x'], handle.tot_file['ecc09_2_y1y'], '+')
    ax3.plot(handle.tot_file['ecc09_3_y1x'], handle.tot_file['ecc09_3_y1y'], '+')
    ax3.plot(handle.tot_file['ecc09_4_y1x'], handle.tot_file['ecc09_4_y1y'], '+')
    ax3.plot(handle.tot_file['ecc09_5_y1x'], handle.tot_file['ecc09_5_y1y'], '+')
    ax3.plot(handle.tot_file['ecc09_6_y1x'], handle.tot_file['ecc09_6_y1y'], '+')
    ax3.plot(handle.tot_file['ecc09_7_y1x'], handle.tot_file['ecc09_7_y1y'], '+')
    ax3.plot(handle.tot_file['ecc09_8_y1x'], handle.tot_file['ecc09_8_y1y'], '+')
    ax3.legend(['1', '2', '3', '4', '5', '6', '7', '8'])
    ax3.set_title('Plasmid shift', fontsize = 15)
    ax3.set_xlabel('Position(pixel)', fontsize = 15)
    ax3.set_ylabel('Position(pixel)', fontsize = 15)
    plt.show()
    return