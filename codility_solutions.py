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
# def solution(A):
#     if not A:
#         return 0
    
#     from collections import Counter
#     counter = Counter(A)
#     odd = [e[0] for e in counter.items() if e[1] % 2 == 1]
#     return odd.pop()

# lesson 3 frog jump
# def solution(X, Y, D):
#     return (Y - X)//D + ((Y - X) % D != 0)

# lesson 3 find the missing element in a given permutation
# def solution(A):
    # found = [0] * (len(A) + 1)
    # for a in A:
    #     found[a - 1] = a
    # return found.index(0) + 1

#lesson 3 tape equilibrium
# def solution(A):
#     if not A:
#         return 0
#     from itertools import  accumulate
#     sumsFoward = list(accumulate(A))
#     sumsBackward = list(accumulate(A[::-1]))[::-1]
#     minimum = float('inf')
#     for i in range(len(A) - 1):
#         tmp = abs(sumsFoward[i] - sumsBackward[i + 1])
#         if minimum > tmp:
#             minimum = tmp    
#     return minimum

#lesson 4  frog river one
# def solution(X, A):
#     positions_set = set(A)
#     valid_pos_count = 0
#     for second, a in enumerate(A):
#         if a <= X and a in positions_set:
#             positions_set.remove(a)
#             valid_pos_count+=1
#         if valid_pos_count == X:
#             return second
#     return -1

#lesson 4  max counters
# def solution(N, A):
#     counters = [0] * N
#     max_counter = 0
#     last_fill = 0
#     for a in A:
#         if a <= N:
#             if counters[a - 1] < last_fill:
#                 counters[a - 1] = last_fill
#             counters[a - 1] += 1
#             if max_counter < counters[a - 1]:
#                 max_counter = counters[a - 1]
#         else:
#             last_fill = max_counter
#     return list(map(lambda c: max(c, last_fill), counters))

#lesson 4  max counters
def solution(A):
    positive = list(filter(lambda x: x > 0, A))
    if not positive:
        return 1
    max_positive = max(positive)
    found = [0] * max_positive
    for i in range(len(A)):
        if A[i] > 0 and not found[A[i] - 1]:
            found[A[i] - 1] = A[i]
    if all(found):
        return max_positive + 1
    return found.index(0) + 1
