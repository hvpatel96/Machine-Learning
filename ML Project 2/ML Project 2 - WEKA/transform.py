myFile = open("vehicle.csv", "r")

allTheLines = myFile.readlines()

print(allTheLines[0:10])

commaSplit = []
for line in allTheLines:
    commaSplit.append(line.split(","))

for array in commaSplit:
    array[-1] = array[-1].split("\n")[0]

filteredArray = []
filteredArray.append(commaSplit[0])

for array in commaSplit[1:]:
    if array[-1] not in ['van', 'bus']:
        filteredArray.append(array)

for array in filteredArray[1:]:
    if array[-1] == 'opel':
        array[-1] = '0'
    else:
        array[-1] = '1'

outFile = open("vehicle_modified.txt", "w")
for array in filteredArray:
    for i in range(len(array) - 1):
        outFile.write(array[i] + ",")
    outFile.write(str(array[-1]) + "\n")
