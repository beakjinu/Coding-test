def solution(n):
    answer = []
    hanoi(n, 1, 2, 3, answer)
    return answer

def hanoi(n, one, two, three, result):
    if n == 1:
        result.append((one, three))
        return
    hanoi(n - 1, one, three, two, result)
    result.append((one, three))
    hanoi(n - 1, two, one, three, result)