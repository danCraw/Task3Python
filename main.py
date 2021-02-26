class Triangle:
    def triangle(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3


class Point:
    def point(self, x, y):
        self.x = x
        self.y = y


xo = False
ox = False
yo = False
oy = False


def createTriangle(p1, p2, p3):
    t = Triangle()
    t.triangle(p1, p2, p3)
    return t


def readLineFromFile(fileName):
    data = []
    with open(fileName) as f:
        for line in f:
            data.append([float(x) for x in line.split()])
    return data

def clear():
    global xo
    xo = False

    global ox
    ox = False

    global yo
    yo = False

    global oy
    oy = False


def readTriangle(line):
    p1 = Point()
    p1.point(line[0][0], line[0][1])
    p2 = Point()
    p2.point(line[0][2], line[0][3])
    p3 = Point()
    p3.point(line[0][4], line[0][5])

    return createTriangle(p1, p2, p3)


# def checkTriangle(triangle):
#    if (triangle)

def intersectionExist(p1, p2):
    p1p2 = axisIntersection(p1, p2)

    if (min(p1.x, p2.x) <= p1p2.x and p1p2.x <= max(p1.x, p2.x)):

        if (p1p2.x >= 0):
            global ox
            ox = True
        if (p1p2.x <= 0):
            global xo
            xo = True

    if (min(p1.y, p2.y) <= p1p2.y and p1p2.y <= max(p1.y, p2.y)):

        if (p1p2.y >= 0):
            global oy
            oy = True
        if (p1p2.y <= 0):
            global yo
            yo = True


def axisIntersection(p1, p2):
    # Ax + By + C = 0 - уравнение прямой
    # A = y1 - y2;
    # B = x2 - x1;
    # C = x1 * y2 - x2 * y1;

    a = p1.y - p2.y
    b = p2.x - p1.x
    c = p1.x * p2.y - p2.x * p1.y

    # x = 0 - уравнение оси oy, тогда:
    # A * 0 + By + C = 0;
    # By = -C;
    # y = -C / B; -> точка
    # пересечения с оу Мy(0;у)
    # аналогично:
    # x = -C / A; -> Mx(x;0)  можем записать в 1 точку(условно) = > Mxy(x;y)

    if (a == 0):
        x = 0
    else:
        x = -c / a
    if (a == 0):
        y = 0
    else:
        y = -c / b

    newPoint = Point()
    newPoint.point(x, y)

    return newPoint


def findTriangles(triangles):
    k = 0

    for i in triangles:
        k = k + 1
        clear()
        intersectionExist(i.point1, i.point2)
        intersectionExist(i.point2, i.point3)
        intersectionExist(i.point3, i.point1)

        if ((xo == True and ox == True and yo == True and oy == True)):
            print("треугольник", k, "лежит в четырех четвертях")
        else:
            print("треугольник", k, "не лежит в четырех четвертях")

if __name__ == '__main__':
    t1 = Triangle()
    t2 = Triangle()
    t3 = Triangle()
    t4 = Triangle()
    t5 = Triangle()
    line1 = readLineFromFile("input01.txt")
    line2 = readLineFromFile("input02.txt")
    line3 = readLineFromFile("input03.txt")
    line4 = readLineFromFile("input04.txt")
    line5 = readLineFromFile("input05.txt")
    t1 = readTriangle(line1)
    t2 = readTriangle(line2)
    t3 = readTriangle(line3)
    t4 = readTriangle(line4)
    t5 = readTriangle(line5)

    findTriangles([t1, t2, t3, t4, t5])
