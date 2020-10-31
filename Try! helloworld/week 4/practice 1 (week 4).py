#변수 만들기
number = 20
greeting = '안녕하세요'
place = '문자열 포맷의 세계'
welcome = '환영합니다'

#기존의 방식
print (number, '번 손님', greeting, '.', place,'에 오신 것을', welcome, '!')

#새로운 방법
base='{}번 손님, {}, {}에 오신 것을 {}!'
new_way = base.format(number,greeting,place,welcome)

print(base)
print(new_way)



#변수
mine = '가위'
yours = '바위'
result = '졌다...'

#case 1
base='나는 {}, 너는 {}, 그래서 {} '

print(base.format(mine, yours, result))


#case 2
base='나는 {}, 너는 {}, 그래서 '

print(base.format(mine, yours, result))

'''
#case 3
base='나는 {}, 너는 {}, 그래서 {} {}'

print(base.format(mine, yours, result))
'''

#pracrice 1
name='김나령'
color='노란색'

base = '안녕하세요. 제 이름은 {}이고 좋아하는 색상은 {}입니다.'
a=base.format(name, color)

print(a)
