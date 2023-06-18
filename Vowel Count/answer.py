def get_count(sentence):
    sum = 0
    for char in sentence:
        if char in "aeiou":
            sum += 1

    return sum


# https://www.codewars.com/kata/54ff3102c1bad923760001f3
