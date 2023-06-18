def create_phone_number(numbers):
    phone_number = ""

    for i in range(len(numbers)):
        phone_number += str(numbers[i])

    return "(" + phone_number[0:3] + ") " + phone_number[3:6] + "-" + phone_number[6:]


# https://www.codewars.com/kata/525f50e3b73515a6db000b83
