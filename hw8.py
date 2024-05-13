def buy():
    while True:
        item = input('상품명? ')
        if item == '':
            break
        m = input('수량은? ')
        shopping_bag[item] = m
        print(f'장바구니에 {item} {shopping_bag[item]}개가 담겼습니다.\n')

def show(shopping_bag):
    print(f'{shopping_bag}')

def find(shopping_bag):
    m = shopping_bag.get('item')
    if m in shopping_bag:
        print(f'{item}(는) {m}개 담겨 있습니다.')
    else:
        return None
    
shopping_bag = {}

print('[구입]')
thing = buy()
#while True:
    #if buy(shopping_bag) == False:
        #break

print(f'\n>>> 장바구니 보기: ',end='')
show(shopping_bag)

print('\n[검색]')
a = input('장바구니에서 확인하고자 하는 상품은? ')
if a in shopping_bag:
    find(shopping_bag)
else:
    print(f'장바구니에 {a}은(는) 없습니다.')
    
