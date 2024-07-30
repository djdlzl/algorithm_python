import sys
from itertools import combinations

angle = []
for _ in range(3):
    angle.append(int(sys.stdin.readline().strip()))

if all(n == 60 for n in angle):  # 세 각의 크기가 모두 60이면, Equilateral
    print('Equilateral')
# 세 각의 합이 180이고, 두 각이 같은 경우에는 Isosceles
elif sum(angle) == 180 and any(a == b for a, b in combinations(angle, 2)):
    print('Isosceles')
# 세 각의 합이 180이고, 같은 각이 없는 경우에는 Scalene
elif sum(angle) == 180 and all(a != b for a, b in combinations(angle, 2)):
    print('Scalene')
elif sum(angle) != 180:  # 세 각의 합이 180이 아닌 경우에는 Error
    print('Error')
