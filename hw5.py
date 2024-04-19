def read_single_digit(a):
    if a ==0 :
        print('영', end=' ')
    elif a == 1:
        print('일', end=' ')
    elif a == 2:
        print('이', end=' ')
    elif a == 3:
        print('삼', end=' ')
    elif a ==  4:
         print('사', end=' ')
    elif a == 5:
         print('오', end=' ')
    elif a == 6:
         print('육', end=' ')
    elif a == 7:
         print('칠', end=' ')
    elif a ==8:
         print('팔', end=' ')
    else:
         print('구', end=' ')

def read_number(n):
    d1 = n%10
    n //=10
    d10 = n%10
    n //=10
    read_single_digit(n)
    read_single_digit(d10)
    read_single_digit(d1)
    
n = int(input('세 자리 정수 입력:'))
read_number(n)










