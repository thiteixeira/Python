#!/usr/bin/env python

'''
  Discrete Fourier Transform (DFT)
  
  Usage: ./dft.py 
         ./dft.py --samples 1024

'''
import random
import math
import cmath
import argparse

parser = argparse.ArgumentParser(description='DFT algorithm analysis.')
parser.add_argument('--samples', type=int, default=1024,
                   help='number of samples')
args = parser.parse_args()
if args:
    N = args.samples
print('Number of samples is ' + str(N))

pi2 = cmath.pi * 2.0


def DFT(fnList):
    N = len(fnList)
    FmList = []
    for m in range(N):
        Fm = 0.0
        for n in range(N):
            Fm += fnList[n] * cmath.exp(- 1j * pi2 * m * n / N)
        FmList.append(Fm / N)
    return FmList


# Testing the DFT function
print('Input Sine Wave Signal:')
a = float(random.randint(1, 100))
f = float(random.randint(1, 100))
p = float(random.randint(0, 360))
print('Frequency = ' + str(f))
print('Amplitude = ' + str(a))
print('Phase = ' + str(p) + '\n')

fnList = []
for n in range(N):
    t = float(n) / N * pi2
    fn = a * math.sin(f * t + p / 360 * pi2)
    fnList.append(fn)

print("DFT Calculation Results:")
FmList = DFT(fnList)
threshold = 0.001
for (i, Fm) in enumerate(FmList):
    if abs(Fm) > threshold:
        print('Frequency = ' + str(i))
        print('Amplitude = ' + str(abs(Fm) * 2.0))
        p = int(((cmath.phase(Fm) + pi2 + pi2 / 4.0) % pi2) / pi2 * 360 + 0.5)
        print('Phase = ' + str(p) + '\n')


