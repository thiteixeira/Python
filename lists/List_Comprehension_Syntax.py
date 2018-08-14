#!/usr/bin/env python


doubles_by_3 = [x * 2 for x in range(1, 12) if (x * 2) % 3 == 0]
even_squares = [y ** 2 for y in range(1, 12) if y % 2 == 0]
cubes_by_four = [c ** 3 for c in range(1, 11) if (c ** 3) % 4 == 0]

print(doubles_by_3)
print(even_squares)
print(cubes_by_four)


