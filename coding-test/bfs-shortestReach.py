__author__ = 'dinesh'


def calculateDistance(start, inputDict, outputDict):
    values = inputDict[start]
    for value in values:
        outputDict[value] = 6
    del inputDict[start]

    for key in values:
        if (key in inputDict.keys()):
            newValues = inputDict[key]
            values += newValues
            for value in newValues:
                if (outputDict[value] == -1):
                    outputDict[value] = outputDict[key] + 6
                else:
                    outputDict[value] = min(outputDict[key] + 6, outputDict[value])
            del inputDict[key]



tests = int(raw_input())
while tests:
    graphInput = raw_input()
    nodeCount, edgeCount = graphInput.split(' ')
    nodeCount = int(nodeCount)
    edgeCount = int(edgeCount)
    outputDict = {}
    inputDict = {}

    for node in range(nodeCount):
        outputDict[node+1] = -1

    while edgeCount:
        graphInput = raw_input()
        input1, input2 = graphInput.split(' ')
        input1 = int(input1)
        input2 = int(input2)
        if (input1 in inputDict.keys()):
            inputDict[input1].append(input2)
        else:
            inputDict[input1] = [input2]
        edgeCount -= 1

    start=int(raw_input())
    calculateDistance(start, inputDict, outputDict)
    del outputDict[start]

    for key in outputDict.keys():
        print str(outputDict[key]) + " "

    tests -= 1