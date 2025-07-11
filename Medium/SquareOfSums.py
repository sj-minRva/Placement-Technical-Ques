'''
You are given a number N. You must find the minimum number of perfect squares
(like 1, 4, 9, 16, 25, ...) whose sum is exactly N.

Example
If N = 100:
    100 = 10² → uses 1 square
    100 = 25 + 25 + 25 + 25 → uses 4 squares
So the answer is 1, because 1 square (10²) is enough.

'''

import math

def minSquares(N):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0

    for i in range(1, N + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
    return dp[N]

N = int(input("Enter the number: "))
print("Minimum number of squares:", minSquares(N))
