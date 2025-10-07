def solution(n):
    answer = 0
    number = n_number(n)
    answer = number % 1234567
    return answer

def n_number(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b