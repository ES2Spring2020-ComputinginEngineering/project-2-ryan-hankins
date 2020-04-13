#Name: Ryan Hankins
#KMeansClustering_driver.py

#Please place your FUNCTION code for step 4 here.
import KMeansClustering_functions as kmc #Use kmc to call your functions
import numpy as np
import matplotlib.pyplot as plt
import random
import copy

#--------------------------------MAIN------------------------------------------
k = int(input('K (Number of Clusters): '))

glucose, hemoglobin, classification = kmc.openckdfile() 
glucose_scaled, hemoglobin_scaled, classification = kmc.normalizeData(glucose, hemoglobin, classification)
#Use normaizeData to normalize the glucose, hemoglobin, and classification arrays

centroids_x, centroids_y = kmc.createInitialCentroids(k, glucose, hemoglobin, classification)
centroids_coords = np.array(list(zip(centroids_x, centroids_y)))
data = np.array(list(zip(hemoglobin_scaled, glucose_scaled)))
#Uses createInitialCentroids to create 

old_centroid = np.zeros(centroids_coords.shape)
cluster_class = np.zeros(len(data))
difference = kmc.findDistance(centroids_coords,old_centroid,None) 
#Differnce is calculated so that the kmeans clustering porcess keeps repeating 
#until there is no more change between iterations

while difference != 0:   
    for i in range(len(data)):
        #Assigns classification to each point based on proximity to centroids
        distances = kmc.findDistance(data[i], centroids_coords)
        cluster = np.argmin(distances)
        cluster_class[i] = cluster
    old_centroid = copy.deepcopy(centroids_coords)    
    kmc.findMean(k, data, centroids_coords, cluster_class)
#Finds the mean values for all the points in each class and makes a new centroid at the mean of the points
    difference = kmc.findDistance(centroids_coords, old_centroid, None)
#------------------------------------TESTS--------------------------------------

#Prints the normalized centroid coordinates   
print('\n'+'Normalized Centroid Coordinates: ')
for i in range(k):
    print(str(round(centroids_coords[i][0],3))+ ', ' + str(round(centroids_coords[i][1],3)))

#Prints the centroid coordinates
print('\n'+'Centroid Coordinates: ')
centroids_coords2 = np.copy(centroids_coords)
for i in range(k):
    centroids_coords2[i][0] = centroids_coords2[i][0]*15.7+3.1
    centroids_coords2[i][1] = centroids_coords2[i][1]*420+70
    print(str(round(centroids_coords2[i][0],3))+ ', ' + str(round(centroids_coords2[i][1],3)))
 
#Since the class assignment is random, this swaps all 1's and 0's if the classes on k=2 are reversed   
if k==2:
    if np.all(cluster_class[150:len(cluster_class)])==1:
        cluster_class[cluster_class==1.]=2.
        cluster_class[cluster_class==0.]=1.
        cluster_class[cluster_class==2.]=0.

#Prints the array of all the classifications
print('\n'+'Class Array: ')
print(cluster_class)

if k==2: #Only calculates the tests if k=2
    #True Postives Test
    count = 0
    for i in range(len(cluster_class)):
        if cluster_class[i]==1 and classification[i]==1:
            count+=1
    percent = round(count/np.count_nonzero(classification==1),2)
    print('True Positives Rate: '+str(100*percent)+'%')
    
    #False Positives Test
    count = 0
    for i in range(len(cluster_class)):
        if cluster_class[i]==1 and classification[i]==0:
            count+=1
    percent = round(count/np.count_nonzero(classification==0),2)
    print('False Positives Rate: '+str(100*percent)+'%')
    
    #True Negatives Test
    count = 0
    for i in range(len(cluster_class)):
        if cluster_class[i]==0 and classification[i]==0:
            count+=1
    percent = round(count/np.count_nonzero(classification==0),2)
    print('True Negatives Rate: '+str(100*percent)+'%')
    
    #False Negatives Test
    count = 0
    for i in range(len(cluster_class)):
        if cluster_class[i]==0 and classification[i]==1:
            count+=1
    percent = round(count/np.count_nonzero(classification==1),2)
    print('False Negatives Rate: '+str(100*percent)+'%')
 
#Graphs the centroids and data points together                       
kmc.graphingKMeans(glucose, hemoglobin, cluster_class, centroids_coords2)

kmc.graphingKMeans(glucose_scaled, hemoglobin_scaled, cluster_class, centroids_coords)