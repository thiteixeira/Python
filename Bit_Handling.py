#!/usr/bin/env python


# Flip bit at position N
def flip_bit(number, n):
    mask = (0b1 << n-1)
    result = mask ^ number
    return bin(result)


# Check if bit is ON or OFF
def check_bit4(input_bit):
    mask = 0b1000
    desired = input_bit & mask
    if desired > 0:
        return 'on'
    else:
        return 'off'


# Turn bits ON or OFF
a = 0b10111011
mask = 0b00000100
desired = a | mask
print(bin(desired))
print(check_bit4(desired))

# Flipping all the bits
a = 0b11101110
mask = 0b11111111
desired = a ^ mask
print(bin(desired))
print(flip_bit(desired,2))
