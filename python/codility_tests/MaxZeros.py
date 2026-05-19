def solution(A):
    N = len(A)
    M = len(A[0])

    if N == 0:
        return 0
    if M == 0:
        return 0

    rPre2 = [[0] * (M+1) for _ in range(N+1)]
    rPre5 = [[0] * (M+1) for _ in range(N+1)]
    cPre2 = [[0] * (M+1) for _ in range(N+1)]
    cPre5 = [[0] * (M+1) for _ in range(N+1)]

    for i in range(N):
        for j in range(M):
            v = A[i][j]
            
            c2 = 0
            while v % 2 == 0:
                c2 += 1
                v //= 2

            c5 = 0
            while v % 5 == 0:
                c5 += 1
                v //= 5

            rPre2[i+1][j+1] = c2 + rPre2[i+1][j]
            rPre5[i+1][j+1] = c5 + rPre5[i+1][j]

            cPre2[i+1][j+1] = c2 + cPre2[i][j+1]
            cPre5[i+1][j+1] = c5 + cPre5[i][j+1]

    max_zeros = 0

    for i in range(N):
        for j in range(M):
            
            c2 = rPre2[i+1][j+1] - rPre2[i+1][j]
            c5 = rPre5[i+1][j+1] - rPre5[i+1][j]

            left2 = rPre2[i+1][j+1]
            left5 = rPre5[i+1][j+1]

            right2 = rPre2[i+1][M] - rPre2[i+1][j]
            right5 = rPre5[i+1][M] - rPre5[i+1][j]

            up2 = cPre2[i+1][j+1]
            up5 = cPre5[i+1][j+1]

            down2 = cPre2[N][j+1] - cPre2[i][j+1]
            down5 = cPre5[N][j+1] - cPre5[i][j+1]

            max_zeros = max(max_zeros,
                min(left2 + up2 - c2, left5 + up5 - c5),
                min(left2 + down2 - c2, left5 + down5 - c5),
                min(right2 + up2 - c2, right5 + up5 - c5),
                min(right2 + down2 - c2, right5 + down5 - c5)
            )
            
    return max_zeros
