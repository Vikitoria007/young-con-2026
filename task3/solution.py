def solution():
    n, m, k = map(int, input().split())
    p = list(map(int, input().split()))
    s = list(map(int, input().split()))

    base = 0 
    for i in range(n):
        base += s[p[i]]
    dp = [-10**18] * (k + 1)
    dp[0] = 0 

    for i in range(n):
        max_add = m - p[i] 
        gains = [0] * (max_add + 1) 
        for t in range(1, max_add + 1):
            gains[t] = s[p[i] + t] - s[p[i] + t - 1]

        new_dp = dp[:]
        for used in range(k + 1):
            if dp[used] < 0:
                continue 
            add = 0 
            for t in range(1, max_add + 1):
                if used + t <= k:
                    add += gains[t] 
                    new_dp[used + t] = max(new_dp[used + t], dp[used] + add)
        dp = new_dp 
    print(base + max(dp))

if __name__ == "__main__":
    solution()
