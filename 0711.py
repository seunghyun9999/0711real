입력 = int(input("3의 배수면 ok 입니다."))

계산 = 입력 % 3

if 계산 == 0 :
    print('ok')
else :
    print('no')

# 사용자가 입력

data = input('입력하세요')

# 3의 배수

th = data%3
if th == 0 :
    # 3의 배수면 ok
    print('ok')
    # 아니면 no
else :
    print('no')
