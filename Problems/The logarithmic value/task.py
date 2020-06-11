import math


value, base = int(input()), int(input())
if base < 1:
    print(round(math.log(value), 2))
else:
    print(round(math.log(value, base), 2))
