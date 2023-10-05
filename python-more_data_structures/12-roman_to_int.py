#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    a_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number_list = []
    for roman_char in roman_string:
        number_list.append(a_dict[roman_char])
    long = len(number_list) - 1
    for i in range(long):
        if i == long:
            break
        elif number_list[i] < number_list[i + 1]:
            number_list[i] = number_list[i] * -1
        else:
            continue
    sum_numbers = 0
    for c in number_list:
        sum_numbers += c
    return sum_numbers
