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

#lesson 4  missing integer
# def solution(A):
#     positive = list(filter(lambda x: x > 0, A))
#     if not positive:
#         return 1
#     max_positive = max(positive)
#     found = [0] * max_positive
#     for i in range(len(A)):
#         if A[i] > 0 and not found[A[i] - 1]:
#             found[A[i] - 1] = A[i]
#     if all(found):
#         return max_positive + 1
#     return found.index(0) + 1

#lesson 4  perm check
def solution(A):
    n = len(A)
    checked = [False] * n
    for a in A:
        if a > n or checked[a - 1]:
            return 0
        checked[a - 1] = True
    return 1
