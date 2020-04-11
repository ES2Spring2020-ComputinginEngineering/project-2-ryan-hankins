#Please put your code for Step 2 and Step 3 in this file.


import numpy as np
import matplotlib.pyplot as plt
import random


# -----------------------------------FUNCTIONS----------------------------------


def openckdfile():
    glucose, hemoglobin, classification = np.loadtxt('ckd.csv', delimiter=',', skiprows=1, unpack=True)
    return glucose, hemoglobin, classification

def normalizeData(glucose,hemoglobin):
    normglucose = (glucose-70)/420
    normhemoglobin = (hemoglobin-3.1)/(17.8-3.1)
    return normglucose, normhemoglobin

def graphData():
    plt.figure()
    plt.plot(hemoglobin_scaled[classification==1],glucose_scaled[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin_scaled[classification==0],glucose_scaled[classification==0], "r.", label = "Class 0")
    plt.suptitle('Normalized Glucose vs Hemoglobin')
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
    
def createTestCase():
    newhemoglobin = round(random.uniform(3.1,17.8),1)
    newglucose = float(random.randint(70,490))
    return newglucose, newhemoglobin

def calculateDistanceArray(newglucose, newhemoglobin):
    distances = np.array([])
    if newglucose > 1:
        newglucose = (newglucose-70)/420
        newhemoglobin = (newhemoglobin-3.1)/15.7
    for i in range(len(glucose)):
        dist = np.sqrt((glucose_scaled[i]-newglucose)**2+(hemoglobin_scaled[i]-newhemoglobin)**2)
        distances = np.append(distances, dist)
    return distances

def nearestNeighborClassifier(newglucose, newhemoglobin):
    min_index = np.argmin(calculateDistanceArray(newglucose,newhemoglobin))
    nearest_class = classification[min_index]
    return nearest_class

def graphTestCase (newglucose, newhemoglobin):
    newglucose, newhemoglobin = normalizeData(newglucose,newhemoglobin)
    plt.figure()
    plt.plot(hemoglobin_scaled[classification==1],glucose_scaled[classification==1], "k.", label = "Class 1")
    plt.plot(hemoglobin_scaled[classification==0],glucose_scaled[classification==0], "r.", label = "Class 0")
    plt.plot(newhemoglobin,newglucose, 'gx', markersize = 10, label = 'Test Case')
    plt.suptitle('Normalized Glucose vs Hemoglobin and Test Case')
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
    
def kNearestNeighborClassifier(k, newglucose, newhemoglobin):
    distances = calculateDistanceArray(newglucose,newhemoglobin)
    sorted_indices = np.argsort(distances)
    k_indices = sorted_indices[:k]
    k_classification = classification[k_indices]
    if np.count_nonzero(k_classification==1) >= int((k//2)+1):
        return 1.
    else:
        return 0.
# -----------------------------------MAIN SCRIPT--------------------------------
glucose, hemoglobin, classification = openckdfile()

glucose_scaled = np.array([])
hemoglobin_scaled = np.array([])

for i in range (len(glucose)):
    normglucose, normhemoglobin = normalizeData(glucose[i],hemoglobin[i])
    glucose_scaled = np.append(glucose_scaled,normglucose)
    hemoglobin_scaled = np.append(hemoglobin_scaled,normhemoglobin)

x = createTestCase()[0]
y = createTestCase()[1]

graphData()
graphTestCase(x,y)
print(kNearestNeighborClassifier(1,x,y))