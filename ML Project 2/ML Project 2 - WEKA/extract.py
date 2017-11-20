myFile = open("cities.txt", "r")

allLines = myFile.readlines()

for i in range(len(allLines)):
    allLines[i] = allLines[i].split("\n")[0]

print(allLines[:10])

cities = []
RHC = []
SA = []
GA = []

for i in range(len(allLines)):
    if i % 4 == 0:
        cities.append(allLines[i])
    elif i % 4 == 1:
        RHC.append(allLines[i])
    elif i % 4 == 2:
        SA.append(allLines[i])
    elif i % 4 == 3:
        GA.append(allLines[i])

for i in range(len(RHC)):
    RHC[i] = float(RHC[i])
    SA[i] = float(SA[i])
    GA[i] = float(GA[i])

print(GA)