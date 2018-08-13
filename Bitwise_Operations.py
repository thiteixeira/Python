#!/usr/bin/env python


print(0b1),    #1
print(0b10),   #2
print(0b11),   #3
print(0b100),  #4
print(0b101),  #5
print(0b110),  #6
print(0b111)   #7
print('\n')
print(0b1 + 0b11)
print(0b11 * 0b11)
print('\n')

print(bin(1))
print(bin(2))
print(bin(3))
print(bin(4))
print(bin(5))
print('\n')

print(oct(20))
print(hex(65))
print('\n')

print(int("1",2))
print(int("10",2))
print(int("111",2))
print(int("0b100",2))
print(int(bin(5),2))
print(int("11001001", 2))
print('\n')

shift_right = 0b1100
shift_left = 0b1

shift_right = shift_right >> 2
shift_left = shift_left << 2

print(bin(shift_right))
print(bin(shift_left))
print('\n')

print(bin(0b1110 & 0b101))     # AND operator
print(bin(0b1110 | 0b101))     # OR operator
print(bin(0b1110 ^ 0b101))     # XOR operator
print(~123)                    # NOT operator
