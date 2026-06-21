import re


def is_valid_cpf(cpf):
    if not isinstance(cpf, str):
        return False

    digits = re.sub(r"\D", "", cpf)

    if len(digits) != 11 or digits == digits[0] * 11:
        return False

    for i in (9, 10):
        total = sum(int(digits[num]) * (i + 1 - num) for num in range(i))
        check_digit = (total * 10 % 11) % 10
        if check_digit != int(digits[i]):
            return False

    return True
