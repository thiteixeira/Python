#!/usr/bin/env python


def main():
    # Create squares from 1 to 10
    # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    alist = [i ** 2 for i in range(1, 11)]

    print(alist[2:9:2])  # [start:end:stride]
    print(alist[::-1])  # Print list in a reverse way


if __name__ == '__main__':
    main()

