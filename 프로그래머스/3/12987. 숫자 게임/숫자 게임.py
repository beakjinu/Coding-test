def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    i=j=0
    answer = 0
    n = len(A)
    while i <n and j<n:
        if B[j] > A[i]:
            answer += 1
            i += 1
            j +=1
        else:
            i +=1
    return answer