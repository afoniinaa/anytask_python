def long_division(dividend, divider):
    dividend_str = str(dividend)
    result = dividend // divider
    result_str = str(result)
    output = f"{dividend_str}{'|'}{str(divider)}\n"

    if result == 0:
        output += f"{dividend_str}{'|0'}"

        return output

    multiplication = int(result_str[0]) * divider
    new_dividend = int(dividend_str[:len(str(multiplication))])
    right_offset = " " * (len(dividend_str) - len(str(multiplication)))
    output += f"{str(multiplication)}{right_offset}{'|'}{result_str}\n"
    result_str = result_str[1:]
    new_dividend -= multiplication
    right_side_of_dividend = dividend_str[len(str(multiplication)):]
    left_offset = ""

    while len(result_str) > 0:
        if result_str[0] == "0":
            result_str = result_str[1:]
            continue

        multiplication = int(result_str[0]) * divider
        right_offset = " " * (len(result_str[1:]))
        left_offset = " " * (len(dividend_str) - len(right_offset) -
                             len(str(multiplication)))

        while new_dividend < divider:
            new_dividend = int(str(new_dividend) +
                               str(right_side_of_dividend[0]))
            right_side_of_dividend = right_side_of_dividend[1:]

        output += f"{left_offset}{str(new_dividend)}\n"
        output += f"{left_offset}{str(multiplication)}\n"
        new_dividend -= multiplication
        result_str = result_str[1:]

    remainder = dividend % divider

    if remainder == 0:
        output += (left_offset + " " * (len(str(multiplication)) - 1))
        output += str(remainder)
    else:
        left_offset = " " * (len(dividend_str) - len(str(remainder)))
        output += left_offset + str(remainder)

    return output


def main():
    print(long_division(123, 123))
    print()
    print(long_division(1, 1))
    print()
    print(long_division(15, 3))
    print()
    print(long_division(3, 15))
    print()
    print(long_division(12345, 25))
    print()
    print(long_division(1234, 1423))
    print()
    print(long_division(87654532, 1))
    print()
    print(long_division(24600, 123))
    print()
    print(long_division(4567, 1234567))
    print()
    print(long_division(246001, 123))
    print()
    print(long_division(100000, 50))
    print()
    print(long_division(123456789, 531))
    print()
    print(long_division(425934261694251, 12345678))


if __name__ == '__main__':
    main()
