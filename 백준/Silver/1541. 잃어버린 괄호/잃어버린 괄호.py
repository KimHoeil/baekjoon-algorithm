# 잃어버린 괄호
# 그리디 속성
# = 뺄셈 뒤의 연산을 모두 덧셈으로 바꾸어서 나머지 결과에서 빼준다
# -50+50 = -(50+50) = -50-50

# 입력된 식을 받습니다.
expression = input()
# print(expression)

# 뺄셈 연산자를 기준으로 식을 분리합니다.
sub_expressions = expression.split('-')
# print(sub_expressions)

# 최초의 수식은 그대로 더합니다.
# print(sub_expressions[0])
min_result = sum(map(int, sub_expressions[0].split('+')))
# print(min_result)

# 이후의 수식들은 모두 뺄셈으로 처리합니다.
for sub in sub_expressions[1:]:
    min_result -= sum(map(int, sub.split('+')))

# 결과를 출력합니다.
print(min_result)
