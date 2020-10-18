#실습 1

mine='가위'
yours='바위'
if mine==yours:
    print('비겼습니다.')
elif mine!=yours:
    print('비기지 않았습니다.')

#실습 2

light='켜짐'


if light=='켜짐':
    print('조명이 켜졌습니다.')


elif light=='꺼짐':
    print('조명이 꺼졌습니다')

else:
    print('올바른 조명 상태가 아닙니다.')


#실습 3
mine='가위'
yours='바위'

if mine==yours:
    print('비김')
elif mine=='가위':
        if yours=='보':
            print('이겼다')
        else:
            print('졌다')
elif mine == '바위':
        if yours == '가위':
            print('이겼다')
        else:
            print('졌다')
elif mine == '보':
        if yours == '바위':
            print('이겼다')
        else:
            print('졌다')