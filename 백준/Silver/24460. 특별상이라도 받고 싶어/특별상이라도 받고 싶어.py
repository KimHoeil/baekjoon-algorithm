# 24460번
import sys

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
     arr.append(list(map(int, input().split())))

def recursion(x, y, n):
     
     if n==1:
          return arr[x][y]
     
     elif n==2:
          result = []
          for i in range(x, x+n):
               for j in range(y, y+n):
                    result.append(arr[i][j])
                    result.sort()
          return result[1]
     
     else:
          ans = []
          ans.append(recursion(x, y, n//2))
          ans.append(recursion(x+n//2, y, n//2))
          ans.append(recursion(x, y+n//2, n//2))
          ans.append(recursion(x+n//2, y+n//2, n//2))
          ans.sort()
          return ans[1]


print(recursion(0,0,n))
