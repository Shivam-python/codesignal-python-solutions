def solution(statues):
    statues=sorted(statues)
    diff=0
    for i in range(len(statues)-1):
        if statues[i+1]-statues[i]>1:
            diff+=statues[i+1]-statues[i]-1
    return diff