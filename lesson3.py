# frog jump
# def solution(X, Y, D):
#     return (Y - X)//D + ((Y - X) % D != 0)

# find the missing element in a given permutation
# def solution(A):
    # found = [0] * (len(A) + 1)
    # for a in A:
    #     found[a - 1] = a
    # return found.index(0) + 1

# tape equilibrium
def solution(A):
    if not A:
        return 0
    from itertools import  accumulate
    sumsFoward = list(accumulate(A))
    sumsBackward = list(accumulate(A[::-1]))[::-1]
    minimum = float('inf')
    for i in range(len(A) - 1):
        tmp = abs(sumsFoward[i] - sumsBackward[i + 1])
        if minimum > tmp:
            minimum = tmp    
    return minimum
