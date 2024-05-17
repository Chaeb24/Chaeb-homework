class Rectangle:
    def __init__(self,x1=0,y1=0,x2=0,y2=0):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        
    def show(self):
        print(f'({self._x1},{self._y1}),({self._x2},{self._y2})')

    def getWidth(self):
        w = (self._x2 - self._x1)
        return w

    def getHeight(self):
        h = (self._y1 - self._y2)
        return h

    def getArea(self):
        a = (self._x2 - self._x1) * (self._y1 - self._y2)
        return a

    def getPerimeter(self):
        p = 2 * (self._x2 - self._x1) + 2 * (self._y1 - self._y2)
        return p

def main():
    r1 = Rectangle(5,5,20,10)
    a = r1.getArea()
    p = r1.getPerimeter()

    r1.show()
    print(f'\n넓이는 {a}, 둘레는 {p}')
    print(f'좌측 상단 꼭지점이')
    print(f'넓이는 {a}, 둘레는 {p}')

if __name__ == '__main__':
    main()
