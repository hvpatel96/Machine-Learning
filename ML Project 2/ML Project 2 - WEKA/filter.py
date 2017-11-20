myFile = open("vehicle.csv", "r")
allLines = myFile.readlines()

commaLines = []

for line in allLines:
    commaLines.append(line.split(","))

print(commaLines[0:10])

# for i in range(len(commaLines)):
#     commaLines[i][-1] = commaLines[i][-1].split("\n")[0]

splitRatio = 0.0

for i in range(9):
    splitRatio += 0.1
    outStringTrain = "vehicleTrain_" + str(splitRatio) + ".csv"
    outStringTest = "vehicleTest_" + str(splitRatio) + ".csv"
    outFileTrain = open(outStringTrain, "w")
    outFileTest = open(outStringTest, "w")
    for item in commaLines[0][:-1]:
        outFileTrain.write(item + ",")
        outFileTest.write(item + ",")
    outFileTrain.write(commaLines[0][-1])
    outFileTest.write(commaLines[0][-1])

    trainingExamples = commaLines[1:int(splitRatio * 846)]
    testingExamples = commaLines[len(trainingExamples): len(commaLines)]
    for i in range(len(trainingExamples)):
        for item in trainingExamples[i][:-1]:
            outFileTrain.write(item + ",")
        outFileTrain.write(trainingExamples[i][-1])
    for i in range(len(testingExamples)):
        for item in testingExamples[i][:-1]:
            outFileTrain.write(item + ",")
        outFileTrain.write(testingExamples[i][-1])
