def square_digits(num):
    sum = ""
    for i in str(num):
        sum += str(int(i) ** 2)
    return int(sum)


# https://www.codewars.com/kata/546e2562b03326a88e000020
