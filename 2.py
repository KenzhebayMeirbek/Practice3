class Point:
    def __init__(self , x1 , y1):
        self.x1 = x1
        self.y1 = y1

    def show(self):
        print(self.x1 , self.y1)

    def move(self, x2 , y2):
        self.x1 = x2
        self.y1 = y2

    def dist(self , other_point):
        return {self.x1 - other_point.x1 + self.y1 - other_point.y1}


x1 , y1 = list(map( int ,input().split()))
x2 , y2 = list(map( int ,input().split()))
x3 , y3 = list(map( int ,input().split()))
point1 = Point(x1 , y1)
point1.move( x2 , y2)
point2 = Point(x3 , y3)

print(f"{point1.dist(point2)}")