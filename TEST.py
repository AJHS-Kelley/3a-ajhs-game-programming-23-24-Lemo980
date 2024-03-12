coordinates = input().split( )
print(coordinates)
x1 = abs(float(coordinates[0]))
y1 = abs(float(coordinates[1]))
x2 = abs(float(coordinates[2]))
y2 = abs(float(coordinates[3]))
xLen = x1 + x2
yLen = y1 + y2
area = xLen * yLen
print(round(area))