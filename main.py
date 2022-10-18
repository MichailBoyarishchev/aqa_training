import numpy as np

a = np.random.randint(-100, 100, size=50)
for el in a:
    if el < 0:
        print(el, "negative")
    if el > 0:
        print(el, "positive")
    if el == 0:
        print(el, "null")
