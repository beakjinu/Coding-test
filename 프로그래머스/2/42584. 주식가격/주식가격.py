def solution(prices):
    n = len(prices)
    ans = [0]*n
    for i in range(n):
        for j in range(i+1, n):
            ans[i] += 1
            if prices[j] < prices[i]:
                break
    return ans
