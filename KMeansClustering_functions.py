#Please place your FUNCTION code for step 4 here.

import numpy as np
import matplotlib.pyplot as plt
import random
import NearestNeighborClassification as nnc


#-----------------------------------Functions----------------------------------

def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(x_obs,y_obs):
    x_obs_scaled = np.array([])
    y_obs_scaled = np.array([])
    xmin = np.amin(x_obs)
    xmax = np.amax(x_obs)
    ymin = np.amin(y_obs)
    ymax = np.amax(y_obs)
    for x in x_obs:
        x_scale = (x-xmin)/(xmax-xmin)
        x_obs_scaled = np.append(x_obs_scaled,x_scale)
    for y in y_obs:
        y_scale = (y-ymin)/(ymax-ymin)
        y_obs_scaled = np.append(y_obs_scaled,y_scale)
    return x_obs_scaled, y_obs_scaled

def plotter(x_obs,y_obs):
    
    plt.figure()
    plt.plot(x_obs,y_obs,'r.')
    plt.suptitle('Normalized Glucose vs Hemoglobin')
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()

#-------------------------------------Main-------------------------------------
    
