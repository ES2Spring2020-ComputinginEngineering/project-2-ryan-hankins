#Name: Ryan Hankins
#KMeansClustering_functions.py

import numpy as np
import matplotlib.pyplot as plt
import random

#-----------------------------------Functions----------------------------------

def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(glucose, hemoglobin, classification):
#Takes 3 arrays and returns normalized arrays for the three observations
    glucose_scaled = np.array([])
    hemoglobin_scaled = np.array([])
    glucose_scaled = (glucose-70)/420
    hemoglobin_scaled = (hemoglobin-3.1)/15.7
    return glucose_scaled, hemoglobin_scaled, classification

def createInitialCentroids(k, glucose, hemoglobin, classification):
#Takes k, and 3 arrays as argument and returns x-coord and y-coord arrays for k centroids
    centroids_x = np.array([])
    centroids_y = np.array([]) 
    for i in range(k):  
        x_test = round(random.uniform(np.amin(hemoglobin),np.amax(hemoglobin)),1)
        y_test = float(random.randint(np.amin(glucose),np.amax(glucose)))
        centroids_x = np.append(centroids_x, x_test)
        centroids_y = np.append(centroids_y, y_test)      
    centroids_y, centroids_x = normalizeData(centroids_y, centroids_x, classification)[0:2]    
    return centroids_x, centroids_y

def findDistance(point1, point2, ax=1):
#Takes 2 data points as argument and returns an aray of the distance between them
    return np.linalg.norm(point1-point2, axis=ax)
        
def findMean(k, data, centroids_coords, cluster_class):
#Takes k and 3 arrays and returns an array of the coordinates of the mean of 
#all values in each classification for k centroids
    for i in range(k):
        points = [data[j] for j in range(len(data)) if cluster_class[j] == i]
        centroids_coords[i] = np.mean(points, axis=0)
    return centroids_coords

def graphingKMeans(glucose, hemoglobin, assignment, centroids):
#Takes 2 arrays of coordinates and an array of classes and plots all the datapoints and the centroids
    plt.figure()
    for i in range(len(centroids)):
        rcolor = np.random.rand(3,)
        plt.plot(hemoglobin[assignment==i],glucose[assignment==i], ".", label = "Class " + str(i), color = rcolor)
        plt.plot(centroids[i, 0], centroids[i, 1], "D", label = "Centroid " + str(i), color = rcolor)
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()

 

    



