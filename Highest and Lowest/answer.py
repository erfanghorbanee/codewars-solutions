def high_and_low(numbers):
    list_of_strings = numbers.split(" ")
    list_of_integers = list(map(int, list_of_strings))
    return f"{max(list_of_integers)} {min(list_of_integers)}"


# https://www.codewars.com/kata/554b4ac871d6813a03000035/
