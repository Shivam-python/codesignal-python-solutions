def bad_pairs(seq):
    for i in range(len(seq)-1):
        if seq[i]>=seq[i+1]:
            return i
    return -1
def solution(s):
    j=bad_pairs(s)
    if j ==-1:
        return True
    if bad_pairs(s[:j]+s[j+1:])==-1:
        return True
    if bad_pairs(s[:j+1] + s[j+2:])==-1:
        return True
    return False