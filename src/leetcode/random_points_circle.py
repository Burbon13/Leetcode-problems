import random
from typing import List
import matplotlib.pyplot as plt


class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        while True:
            x = random.uniform(self.x - self.r, self.x + self.r)
            y = random.uniform(self.y - self.r, self.y + self.r)
            if self.inCircle(x, y):
                return [x, y]

    def inCircle(self, x, y) -> bool:
        return self.distance(x, y, self.x, self.y) <= self.r ** 2

    def distance(self, x1, y1, x2, y2) -> float:
        return (x1 - x2) ** 2 + (y1 - y2) ** 2


sol = Solution(5, 0, 0)

x = []
y = []

for _ in range(10000):
    new_x, new_y = sol.randPoint()
    x.append(new_x)
    y.append(new_y)

plt.figure(figsize=(12, 12))
plt.axis([-6, 6, -6, 6])
plt.scatter(x, y)
plt.show()
