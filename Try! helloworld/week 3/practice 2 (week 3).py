#실습 1
from datetime import datetime
hour=datetime.now().hour

if hour<12:
    print("오전입니다.")

if hour>12:
    print("오후입니다")


#실습 2

number = 15
if number % 3 == 0:
    print("{}는 3의 배수입니다." .format(number)) #이 코드는 실행된다

number = 16
if number % 3 == 0:
    print('{}는 3의 배수입니다.' .format(number)) #이 코드는 실행 되지 않는다.

#실습 3

from datetime import datetime
hour = datetime.now(). hour

if hour % 6 == 0:
    print ('종이 울립니다')