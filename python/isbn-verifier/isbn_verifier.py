def verify(isbn):
    formatted_isbn = isbn.replace("-", "")

    if len(formatted_isbn) != 10:
        return False

    if not formatted_isbn[:-1].isdigit():
        return False

    check_sum = formatted_isbn[-1]
    if not check_sum.isdigit() and check_sum != 'X':
        return False
    
    isbn_data = zip(range(10, 0, -1), formatted_isbn)
    return 0 == sum([index * (int(number) if number != 'X' else 10) for index, number in isbn_data]) % 11