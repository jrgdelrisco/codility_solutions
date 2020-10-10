# cyclic rotation
# def solution(A, K):
#     k = K % len(A)
#     a = A[len(A) - k:] + A[:len(A) - k]
#     return a

# odd occurrences in array
def solution(A):
    if not A:
        return 0
    
    from collections import Counter
    counter = Counter(A)
    odd = [e[0] for e in counter.items() if e[1] % 2 == 1]
    return odd.pop()
