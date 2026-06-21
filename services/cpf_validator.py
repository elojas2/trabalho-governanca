import re

_INVALID_SEQUENCES = {str(d) * 11 for d in range(10)}


def _only_digits(value):
    return re.sub(r"\D", "", value or "")


def _check_digit(partial):
    weight = len(partial) + 1
    total = sum(int(digit) * w for digit, w in zip(partial, range(weight, 1, -1)))
    remainder = total % 11
    return "0" if remainder < 2 else str(11 - remainder)


def is_valid_cpf(cpf):
    digits = _only_digits(cpf)

    if len(digits) != 11 or digits in _INVALID_SEQUENCES:
        return False

    first_check = _check_digit(digits[:9])
    second_check = _check_digit(digits[:9] + first_check)

    return digits[9:] == first_check + second_check


def mask_cpf(cpf):
    digits = _only_digits(cpf)
    if len(digits) != 11:
        return "***.***.***-**"
    return f"***.***.{digits[6:9]}-{digits[9:11]}"
