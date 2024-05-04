shopping_bag = []
d = {'사과':10,'바나나':2}

print('[구입]')
while True:
    item = input('상품명? ')
    if item == '':
        break
    shopping_bag.append(item)
    print(f'수량은? {d.get(item)}')
    print(f'장바구니에 {item} {d[item]}개가 담겼습니다.\n')

print(f'\n >>> 장바구니 보기:',end='')
print(d)

print(f'\n[검색]')
m = input('장바구니에서 확인하고자 하는 상품은? ')
print(f'{m}은(는) {d[m]}개 담겨 있습니다.')
    
