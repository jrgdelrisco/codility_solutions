# binary gap
def solution(N):
    n = str(bin(N))[2:]
    indexes_one = [i for i in range(len(n)) if n[i] == '1']
   
    if len(indexes_one) <= 1:
        return 0
   
    return max([indexes_one[i] - indexes_one[i - 1] for i in range(1, len(indexes_one))]) - 1
