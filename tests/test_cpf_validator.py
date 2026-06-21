from services.cpf_validator import is_valid_cpf, mask_cpf

# CPFs fictícios: satisfazem o algoritmo de dígitos verificadores,
# mas não correspondem a pessoas reais.
FICTITIOUS_VALID_CPFS = [
    "835.291.647-55",
    "246.897.531-64",
    "918.273.645-64",
]


def test_accepts_fictitious_valid_cpfs():
    for cpf in FICTITIOUS_VALID_CPFS:
        assert is_valid_cpf(cpf)


def test_accepts_unformatted_valid_cpf():
    assert is_valid_cpf("83529164755")


def test_rejects_wrong_checksum():
    assert not is_valid_cpf("835.291.647-00")


def test_rejects_repeated_digit_sequences():
    for digit in "0123456789":
        assert not is_valid_cpf(digit * 11)


def test_rejects_wrong_length():
    assert not is_valid_cpf("123456789")


def test_rejects_non_numeric_garbage():
    assert not is_valid_cpf("abc.def.ghi-jk")


def test_rejects_empty_or_missing_value():
    assert not is_valid_cpf("")
    assert not is_valid_cpf(None)


def test_mask_keeps_only_last_group_and_check_digits():
    assert mask_cpf("835.291.647-55") == "***.***.647-55"


def test_mask_handles_invalid_input_safely():
    assert mask_cpf("123") == "***.***.***-**"
