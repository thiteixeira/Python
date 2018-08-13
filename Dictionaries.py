#!/usr/bin/env python


def main():
    my_dict = {
        "Name": "James",
        "Age": 23,
        "Student": True
    }

    print(my_dict.items())  # Return an array of key/value pair
    print(my_dict.keys())  # Return an array of dictionary keys
    print(my_dict.values())  # Return an array of dictionary values

    for key in my_dict:
        print(my_dict[key], key)  # Print the key and the value of the key


if __name__ == '__main__':
    main()

