def verify(isbn):
    formatted_isbn = isbn.replace("-", "")

    if len(formatted_isbn) != 10:
        return False

    check_sum = sum(int(formatted_isbn[i]) * (10 - i) for i in range(8))
    check_sum %= 11
    check_digit = 11 - check_sum

    if check_digit == 0:
        return True
    else:
        return False