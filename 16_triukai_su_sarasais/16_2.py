from statistics import mean, median
from typing import List, Any

new_range = list(range(50))

a = ([x*10 for x in new_range])
print(a)

b = [x for x in new_range if x % 7 == 0]
print(b)

new = [x**2 for x in new_range]
print(new)

print(sum(new))
print(min(new))
print(max(new))
print(mean(new))
print(median(new))
atbulai = sorted(new, reverse=True)
print(atbulai)
