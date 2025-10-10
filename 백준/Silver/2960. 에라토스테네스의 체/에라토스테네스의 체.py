import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(range(2, N+1))
count = 0

for i in range(2, N+1):
    for x in nums[:]:
        if x % i == 0:
            nums.remove(x)
            count += 1
            if count == K:
                print(x)
                exit()
