def solution(inputArray):
    max_length = 0
    for i in inputArray:
        max_length = max(max_length,len(i))
    return [i for i in inputArray if len(i)==max_length]

