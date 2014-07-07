#-------------------------------------------------------------------------------
# Name:        Bit Handling
# Purpose:
#
# Author:      thiteixeira
#
# Created:     22/06/2014
# Copyright:   (c) thiteixeira 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

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

print (bin(desired))

# Flipping all the bits
a = 0b11101110
mask = 0b11111111
desired = a ^ mask

# Flip bit at position N
def flip_bit(number, n):
    mask = (0b1 << n-1)
    result = mask ^ number
    return bin(result)

print (bin(desired))