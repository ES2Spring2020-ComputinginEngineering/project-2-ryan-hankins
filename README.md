Name: Ryan Hankins
ES2 Project 2 - Biomedical Data Analysis

How to use each file:

NearestNeighborClassification.py - Running the code will produce a normalized graph 
with a test case and will print out a classification for the test case data point.

KMeansClustering_functions.py - Running the code does nothing. It contains functions for KMeansClustering_driver.py.

KMeansClustering_driver.py - Running the code will ask for an input for k(number of clusters).
Input an integer and the code will print out k sets of centroid coordinates, both 
normalized and standard, as well as the array of the classification for each data point. If 
k equals 2, the code will also print out tests for True Postives, False Positives, 
True Negatives, and False Negatives. This driver produces the data table of centroid 
coordinates present in the report along with the graph of the centroids and the various statistics tests.

Functions:

normalizeData - Takes 3 arrays and returns normalized arrays for the three observations.

createInitialCentroids - Takes k, and 3 arrays as argument and returns x-coord and y-coord arrays for k centroids.

findDistance - Takes 2 data points as argument and returns an aray of the distance between them.

findMean - Takes k and 3 arrays and returns an array of the coordinates of the mean of 
all values in each classification for k centroids.

graphingKMeans- Takes 2 arrays of coordinates and an array of classes and plots all the datapoints and the centroids.