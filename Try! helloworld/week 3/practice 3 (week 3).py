#실습 1
if False:
    print('블록에 속한 코드')
    if True:
        print('조건이 맞는 코드')

    print('어쨋든 실행되지 않는 코드')
print('다시 바깥에 있는 코드')

#실습 2
if True:
    print('블록에 속한 코드')

    if False:
        print('한 줄 더')
    if True:
        print('또 한 줄 더')
        if True:
            print('블록 하나 더')
    print('블록의 끝 코드')
print('바깥에 있는 코드')