# lesson 2 cyclic rotation
def solution(A, K):
    k = K % len(A)
    a = A[len(A) - k:] + A[:len(A) - k]
    return a