import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    def lcm(a,b):
        return abs(a*b) // math.gcd(a,b)
    
    lcm = lcm(denom1, denom2)
    
    multiple1 = lcm // denom1
    multiple2 = lcm // denom2
    numer1 = numer1 * multiple1
    numer2 = numer2 * multiple2
    numer = numer1+numer2
    
    # 기약 분수로 만들기
    gcd = math.gcd(numer, lcm)
    
    answer.append(numer // gcd)
    answer.append(lcm // gcd)
    
    return answer