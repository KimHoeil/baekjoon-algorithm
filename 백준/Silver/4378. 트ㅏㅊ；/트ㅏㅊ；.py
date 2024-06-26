# https://www.acmicpc.net/problem/4378

import sys
# input = sys.stdin.readline


while True:
    try:
        sentence = input()
        # print(sentence)
        for word in sentence:
            if word == 'W':
                print('Q',end='')
            elif word == 'E':
                print('W', end='')
            elif word == 'R':
                print('E',end='')
            elif word == 'T':
                print('R',end='')
            elif word == 'Y':
                print('T',end='')
            elif word == 'U':
                print('Y',end='')
            elif word == 'I':
                print('U', end='')
            elif word == 'O':
                print('I', end='')
            elif word == 'P':
                print('O', end='')
            elif word == '[':
                print('P',end='')
            elif word == ']':
                print('[',end='')
            elif word == '\\':
                print(']', end='')

            elif word == 'S':
                print('A',end='')
            elif word == 'D':
                print('S', end='')
            elif word == 'F':
                print('D',end='')
            elif word == 'G':
                print('F',end='')
            elif word == 'H':
                print('G',end='')
            elif word == 'J':
                print('H',end='')
            elif word == 'K':
                print('J', end='')
            elif word == 'L':
                print('K', end='')
            elif word == ';':
                print('L', end='')
            elif word == '\'':
                print(';',end='')

            elif word == 'X':
                print('Z',end='')
            elif word == 'C':
                print('X', end='')        
            elif word == 'V':
                print('C',end='')
            elif word == 'B':
                print('V', end='')
            elif word == 'N':
                print('B',end='')
            elif word == 'M':
                print('N',end='')
            elif word == ',':
                print('M',end='')
            elif word == '.':
                print(',',end='')
            elif word == '/':
                print('.', end='')

            elif word == '1':
                print('`',end='')
            elif word == '2':
                print('1', end='')
            elif word == '3':
                print('2',end='')
            elif word == '4':
                print('3',end='')
            elif word == '5':
                print('4',end='')
            elif word == '6':
                print('5',end='')
            elif word == '7':
                print('6', end='')
            elif word == '8':
                print('7', end='')
            elif word == '9':
                print('8', end='')
            elif word == '0':
                print('9',end='')
            elif word == '-':
                print('0',end='')
            elif word == '=':
                print('-', end='')  
            else:
                print(word, end='')

        print()
    except EOFError:
        break
# print(sentence)
#     print(word, end='')
# print()