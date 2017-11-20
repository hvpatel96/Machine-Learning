# Open the original dataset
vehicleFile = open("vehicle.csv", "r")

# Extract instance vectors and convert strings to ints
allArray = vehicleFile.readlines()
header = allArray[0]
allArray = allArray[1:]
commaArray = []
for array in allArray:
    commaArray.append(array.split(",")[0:-1] + [array.split(",")[-1].split("\n")[0]])

for array in commaArray:
    for i in range(len(array) - 1):
        array[i] = int(array[i])

# # Four cluster centers given by kMeans from WEKA with k = 4
# kcluster1 = [85.25,40.7877,65.6509,132.4198,57.9481,7.0755,140.6179,48.3962,18.4575,137.9057,162.6792,292.2217,158.8538,79.316,5.783,10.1651,182.2123,186.3915]
# kcluster2 = [92.8778,45.095,83.4072,174.9729,64.4072,9.6335,165.0679,40.4932,20.1991,149.2036,187.3575,410.1584,175.5973,71.2036,6.6697,11.1991,190.371,197.8507]
# kcluster3 = [91.1034,38.7299,72.7241,160.9828,62.2299,7.454,144.8793,45.977,18.6839,134.8218,167.0575,318.2241,140.1609,66.2414,5.4655,13.9253,195.9655,202.592]
# kcluster4 = [103.7699,52.7238,102.2678,201.5523,62.1172,9.7155,214.8033,31.0502,24.205,165.431,228.5146,687.0209,213.0837,72.0753,7.2971,15.0879,188.4435,196.7113]

# Four cluster center means given by EM from WEKA with numClusters = 4
EMcluster1 = [89.8914,40.1736,73.0989,156.002,61.889,7.4345,143.4449,46.4172,18.5815,137.668,166.0813,309.8319,149.0201,67.7421,5.8907,11.7477,193.4277,200.1137]
EMcluster2 = [84.9653,40.5534,64.1924,127.586,56.4837,6.311,139.5439,48.9223,18.3927,137.3727,160.0496,287.0878,158.6946,80.0584,6.0758,10.197,181.4046,185.3922]
EMcluster3 = [93.1698,44.3999,82.9466,179.0134,65.4057,10.4311,166.9305,39.9254,20.34,147.9342,190.1453,418.6931,171.3498,71.8822,6.1292,12.6349,190.8256,197.9839]
EMcluster4 = [103.613,52.5058,102.0742,201.518,62.1819,9.6823,213.9285,31.174,24.1271,164.8711,227.8741,681.955,211.9411,71.924,7.2283,15.0223,188.5777,196.8154]

outFile = open("vehicle_EM.csv", "w")
outFile.write(header)
import numpy
# Creating new feature vectors composed of distances away from each cluster center
for array in commaArray:
    label = array[-1]
    featureValues = numpy.array(array[:-1])
    dist1 = numpy.linalg.norm(featureValues-numpy.array(EMcluster1))
    dist2 = numpy.linalg.norm(featureValues-numpy.array(EMcluster2))
    dist3 = numpy.linalg.norm(featureValues-numpy.array(EMcluster3))
    dist4 = numpy.linalg.norm(featureValues-numpy.array(EMcluster4))
    # dist1 = numpy.linalg.norm(featureValues-numpy.array(kcluster1))
    # dist2 = numpy.linalg.norm(featureValues-numpy.array(kcluster2))
    # dist3 = numpy.linalg.norm(featureValues-numpy.array(kcluster3))
    # dist4 = numpy.linalg.norm(featureValues-numpy.array(kcluster4))
    outFile.write(str(dist1) + ",")
    outFile.write(str(dist2) + ",")
    outFile.write(str(dist3) + ",")
    outFile.write(str(dist4) + ",")
    outFile.write(str(label) + "\n")