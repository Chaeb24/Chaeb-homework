import hw3_01 as drate

discount = int(input('할인율은?'))
drate.set_rate(discount)

Amerchandise = int(input('A 상품의 할인된 가격은?'))
Bmerchandise = int(input('B 상품의 할인된 가격은?'))

print('A 상품의 정가는', int(drate.to_Athing(Amerchandise)), '원')
print('B 상품의 정가는', int(drate.to_Bthing(Bmerchandise)), '원')


