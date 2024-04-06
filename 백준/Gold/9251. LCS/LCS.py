# LCS     

import sys

stringA = list(input())
stringB = list(input())

dp = [[0 for j in range(len(stringA)+1)] for i in range(len(stringB)+1)] 

def LCS():
     global dp

     for i in range(1, len(stringB)+1):
          for j in range(1, len(stringA)+1):
               if stringA[j-1] == stringB[i-1]:
                    dp[i][j] = dp[i-1][j-1] +1
               else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
     

     print(dp[len(stringB)][len(stringA)])

LCS()
