import math
def solution(n):
    answer = 0
    def Lcm(a,b):
        lcm = abs(a*b) // math.gcd(a,b)
        return lcm
    
    answer = Lcm(n,6)
    return answer // 6