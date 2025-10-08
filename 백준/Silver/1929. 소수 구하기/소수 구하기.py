import sys, math
input = sys.stdin.readline

def make_array(M, N):
    return list(range(M, N+1))

def main():
    M, N = map(int, input().split())
    a = make_array(M, N)
    b = make_array(2, int(math.sqrt(N)))
    for x in a:
        if x < 2:
            continue
        is_prime = True
        for i in b:
            if i ** 2 > x:
                break
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            print(x)

if __name__ == "__main__":
    main()
