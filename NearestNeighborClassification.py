#Name: Ryan Hankins
#NearestNeighborClassification.py

import numpy as np
import matplotlib.pyplot as plt
import random


# -----------------------------------FUNCTIONS----------------------------------

def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(glucose, hemoglobin, classification):
#Takes 3 arrays and returns normalized arrays for the three observations
    glucose_scaled = np.array([])
    hemoglobin_scaled = np.array([])
    glucose_scaled = (glucose-70)/420
    hemoglobin_scaled = (hemoglobin-3.1)/(17.8-3.1)
    return glucose_scaled, hemoglobin_scaled, classification

def graphData(glucose, hemoglobin, classification):
#Takes three arrays and plots them
    plt.figure()
    plt.plot(hemoglobin[classification==1],glucose[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin[classification==0],glucose[classification==0], "r.", label = "Class 0")
    plt.suptitle('Normalized Glucose vs Hemoglobin')
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
    
def createTestCase():
#Takes no arguments and returns a random test case point
    newhemoglobin = round(random.uniform(3.1,17.8),1)
    newglucose = float(random.randint(70,490))
    return newglucose, newhemoglobin

def calculateDistanceArray(newglucose, newhemoglobin, glucose, hemoglobin):
#Takes 2 arrays  and 1 data point as arguments and reutnrs an array of the 
#distances between the data point and every point in the two arrays
    distances = np.array([])
    if newglucose > 1:
        newglucose = (newglucose-70)/420
        newhemoglobin = (newhemoglobin-3.1)/15.7
    glucose_scaled, hemoglobin_scaled = normalizeData(glucose,hemoglobin, classification)[0:2]
    for i in range(len(glucose)):
        dist = np.sqrt((glucose_scaled[i]-newglucose)**2+(hemoglobin_scaled[i]-newhemoglobin)**2)
        distances = np.append(distances, dist)
    return distances

def nearestNeighborClassifier(newglucose, newhemoglobin, glucose, hemoglobin, classification):
#Takes a data point and 3 arrays as arguments and returns a classification for the data point
    min_index = np.argmin(calculateDistanceArray(newglucose,newhemoglobin, glucose, hemoglobin))
    nearest_class = classification[min_index]
    return nearest_class

def graphTestCase (newglucose, newhemoglobin, glucose, hemoglobin, classification):
#Takes a data point and three arrays as arugment and plots all of them
    glucose_scaled, hemoglobin_scaled = normalizeData(glucose, hemoglobin, classification)[0:2]
    plt.figure()
    plt.plot(hemoglobin_scaled[classification==1],glucose_scaled[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin_scaled[classification==0],glucose_scaled[classification==0], "r.", label = "Class 0")
    plt.plot((newhemoglobin-3.1)/15.7,(newglucose-70)/420, 'gx', markersize = 15 ,label = 'Test Case')
    plt.suptitle('Normalized Glucose vs Hemoglobin and Test Case')
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
    
def kNearestNeighborClassifier(k, newglucose, newhemoglobin, glucose, hemoglobin, classification):
#Takes k, a data point, and 3 arrays as arguments and returns a classification of the 
#data point based on #k nearby points
    distances = calculateDistanceArray(newglucose,newhemoglobin, glucose, hemoglobin)
    sorted_indices = np.argsort(distances)
    k_indices = sorted_indices[:k]
    k_classification = classification[k_indices]
    if np.count_nonzero(k_classification==1) >= int((k//2)+1):
        return 1.
    else:
        return 0.
# -----------------------------------MAIN SCRIPT--------------------------------
glucose, hemoglobin, classification = openckdfile()

x = createTestCase()[0]
y = createTestCase()[1]

distances = calculateDistanceArray(x,y,glucose, hemoglobin)

graphTestCase(x,y,glucose, hemoglobin, classification)

print('K Nearest Classification: ' +str(kNearestNeighborClassifier(9, x, y, glucose, hemoglobin, classification)))

