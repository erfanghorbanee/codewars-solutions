def duplicate_count(text):
    num = 0
    text = text.lower()
    text_without_duplicates = "".join(set(text))

    for i in text_without_duplicates:
        if text.count(i) > 1:
            num += 1

    return num


# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
