# 11387

import sys
input = sys.stdin.readline


cri = list(map(int, input().split()))
pabu = list(map(int, input().split()))
criWeapon = list(map(int, input().split()))
pabuWeapon = list(map(int, input().split()))


def power(h, w):
  return (h[0]+w[0]) * (100+h[1]+w[1]) * ( 100*(100-min(h[2]+w[2],100)) + min(h[2]+w[2],100) * (h[3]+w[3])) * (100+h[4]+w[4])


for i in range(len(criWeapon)):
    cri[i] =  cri[i] - criWeapon[i] 
    pabu[i] = pabu[i] - pabuWeapon[i]

diff1 = power(cri, pabuWeapon) - power(cri, criWeapon)
diff2 = power(pabu, criWeapon) - power(pabu, pabuWeapon)

if diff1 > 0: print('+')
elif diff1 == 0: print('0')
else: print('-')

if diff2 > 0: print('+')
elif diff2 == 0: print('0')
else: print('-')
