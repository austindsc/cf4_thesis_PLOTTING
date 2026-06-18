import pandas as pd
import numpy as np
import os

os.chdir('/Users/austindestcroix/Desktop/school_holders/THESIS/PLOTTING')

optics = pd.read_csv('data/optics_HPK-VUV4_noWindow_17nmOxide_defaultData_globalPar_160k.csv')
pde = pd.read_csv('data/internalPDE_HPK-VUV4_noWindow_17nmOxide_defaultData_globalPar_160k.csv')
filt = pd.read_csv('data/LP_500nm.csv')

op0 = optics[optics['angle']==0.0].head(3)
print("optics 0deg sample:\n", op0.to_string())

uv = np.loadtxt('data/cf4Scint_5bar_UV.txt', comments='#')
vis = np.loadtxt('data/cf4Scint_5bar_Vis.txt', comments='#')
print('UV scint shape:', uv.shape, 'wl:', uv[:,0].min(), uv[:,0].max())
print('Vis scint shape:', vis.shape, 'wl:', vis[:,0].min(), vis[:,0].max())

gern_x, gern_y = np.loadtxt('oldStitching/literature_data/gernhauser_cf4_05bar.csv', skiprows=2, delimiter=',', unpack=True)
print('Gern wl range:', gern_x.min(), gern_x.max())

mor_x, mor_y = np.genfromtxt('oldStitching/literature_data/morozov_2010_spectrum.csv', skip_header=2, usecols=(0,1), delimiter=',', unpack=True)
print('Mor wl range:', mor_x.min(), mor_x.max())

uv_x, uv_y, uv_ey = np.genfromtxt('oldStitching/literature_data/morozov_UV_yields.csv', skip_header=2, usecols=(0,1,3), delimiter=',', unpack=True)
print('Mor UV yields (0.5bar):', uv_x[0], uv_y[0])

vis_x2, vis_y2, vis_ey2 = np.genfromtxt('oldStitching/literature_data/morozov_VIS_yields.csv', skip_header=2, usecols=(0,1,3), delimiter=',', unpack=True)
print('Mor Vis yields:', vis_x2, vis_y2)

# Check filter 
print("Filter head:\n", filt.head(5).to_string())
