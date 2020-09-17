# lesson 1 binary gap
# def solution(N):
#     n = str(bin(N))[2:]
#     indexes_one = [i for i in range(len(n)) if n[i] == '1']
   
#     if len(indexes_one) <= 1:
#         return 0
   
#     return max([indexes_one[i] - indexes_one[i - 1] for i in range(1, len(indexes_one))]) - 1

# lesson 2 cyclic rotation
# def solution(A, K):
#     k = K % len(A)
#     a = A[len(A) - k:] + A[:len(A) - k]
#     return a

# lesson 2 odd occurrences in array
def solution(A):
    if not A:
        return 0
    
    from collections import Counter
    counter = Counter(A)
    odd = [e[0] for e in counter.items() if e[1] % 2 == 1]
    return odd.pop()
