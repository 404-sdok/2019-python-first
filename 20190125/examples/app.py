# 형변환
# int -> 숫자
# str -> 문자
# int() -> 괄호 안에 있는 문자를 숫자로 바꿈, 단 문자안에 숫자 외에 다른 내용이 들어있으면 오류.
# str() -> 괄호 안에 있는 숫자를 문자로 바꿈.

friends = 5
# conv = '친구가 ' + friends + '명 온라인입니다.' << 오류 발생.
# * 문자와 숫자는 그대로 합칠 수 없음.
conv = '친구가 ' + str(friends) + '명 온라인입니다.'
print(conv)

# ==================================================================

# 할당 연산자
# += -= *= /= 가 해당함
# 왼쪽에 있는 데이터에 왼쪽의 데이터를 (더함/뺌/곱함/나눔)



friends += 1    # 기존 friends에 있던 숫자에 1을 더 더함.
print(friends)
friends += 5    # 기존 friends에 있던 숫자에 5를 더 더함.
print(friends)
friends -= 8    # 기존 friends에 있던 숫자에 8을 뺌.
print(friends)
friends *= 3    # 기존 friends에 있던 숫자에 3을 곱함.
print(friends)
friends /= 3    # 기존 friends에 있던 숫자에 3을 나눔.
print(friends)

conv += ' 친구가 많이 없네요.'  # 문자도 가능.

# ==================================================================

# 문자열 포맷팅

# '친구가 ' + str(friends) + '명 온라인입니다.' 가 많아지면 복잡해지기 때문에 ' + str(friends) + '를 대체하기 위해 만들어짐.

conv = '친구가 %d명 온라인입니다.' % (friends)      # 문자열 안에 %d를 입력하면 그 자리를 숫자로 대체할 수 있음.
print(conv)

conv = '친구가 {}명 온라인입니다.'.format(friends)  # 문자열 안에 {}를 입력하면 그 자리를 다른 데이터로 대체할 수 있음.
print(conv)

conv = '{name}의 {food}는 {target}이다.'.format(name='종혁이', food='주식', target='바나나')
# {}를 사용한 문자열 포맷팅은 {}안에 대체할 데이터의 이름을 지정해줄 수 있음

# ==================================================================

# 과제 예시

plus_friends_num = 2
plus = '플러스친구 {plus_friends}'.format(plus_friends = plus_friends_num)
print(plus)
plus_friends_num += 1
plus = '플러스친구 {plus_friends}'.format(plus_friends = plus_friends_num)
print(plus)
