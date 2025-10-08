import math

def solution(left, right):
    
    plus = []
    minus = []
    
    for num in range(left, right +1):
        if is_odd(num):
            minus.append(num)
        else:
            plus.append(num)
    answer = sum(plus) - sum(minus)
    return answer

def is_odd(x):
    a = math.isqrt(x)
    return a * a == x