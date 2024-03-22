def exchange(amount):
    n500 = amount // 500
    n100 = amount % 500
    a100 = n100 // 100
    n50 = n100 // 50
    n10 = n100 // 10
    print('500원 동전의 개수:',n500)
    print('100원 동전의 개수:',a100)
    print('50원 동전의 개수:', n50)
    print('10원 동전의 개수:', n10)

def get_integer(prompt):
    return int(input(prompt))

n = get_integer('동전으로 교환하고자 하는 금액은?')
exchange(n)          
    
