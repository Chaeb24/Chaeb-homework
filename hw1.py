def get_radius(prompt):
    r = int(input(prompt))
    return r

r = get_radius('넓이를 구하고자 하는 원의 반지름은? ')
print('반지름', r, '인 원의 넓이 = 3.14 X', r, 'X', r,'=', end=' ')
print(3.14*r*r)

def get_circle_area(radius):
    area = 3.14*radius*radius
    return area

result = get_circle_area(r)
print(result)
    



