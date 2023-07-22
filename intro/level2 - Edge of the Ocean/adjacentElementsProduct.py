import numpy as np

def solution(inputArray):
    max=-np.inf
    for i in range(len(inputArray)-1):
        if inputArray[i]*inputArray[i+1]>max:
            max=inputArray[i]*inputArray[i+1]
    return max

