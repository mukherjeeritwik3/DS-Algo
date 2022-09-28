def firsRecurringNumber(arr):
    trackerDict = dict()
    for i in arr:
        if i == trackerDict.get(i):
            return i
        trackerDict[i] = i
    return "Undefined"    
test = [1,2,4,4,5,6,7,5]
print(firsRecurringNumber(test))