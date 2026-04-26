N, K = map(int, input().split())
least = K * (K + 1) // 2

if N >= least:
    if (N - least) % K == 0:
        print(K - 1)
    else:
        print(K)
else:
    print(-1)
