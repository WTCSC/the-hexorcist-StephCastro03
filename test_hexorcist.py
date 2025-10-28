from hexorcist import to_decimal, from_decimal

def test_to_decimal_binary():
    assert to_decimal("1100", 2) == 12

def test_to_decimal_hex():
    assert to_decimal("1A3", 16) == 419

def test_to_decimal_octal():
    assert to_decimal("755", 8) == 493

def test_to_decimal_lowercase_hex():
    assert to_decimal("ff", 16) == 255

def test_to_decimal_base36():
    assert to_decimal("AB", 36) == 371

def test_to_decimal_invalid_char():
    assert to_decimal("19", 8) == None

def test_to_decimal_zero():
    assert to_decimal("0", 2) == 0

def test_from_decimal_binary():
    assert from_decimal(12, 2) == "1100"

def test_from_decimal_hex():
    assert from_decimal(419, 16) == "1A3"

def test_from_decimal_octal():
    assert from_decimal(493, 8) == "755"

def test_from_decimal_base36():
    assert from_decimal(371, 36) == "AB"

def test_from_decimal_zero():
    assert from_decimal(0, 8) == "0"

def test_round_trip_binary_to_hex():
    decimal_value = to_decimal("11110000", 2)
    converted_value = from_decimal(decimal_value, 16)
    assert converted_value == "F0"

def test_round_trip_hex_to_binary():
    decimal_value = to_decimal("F0", 16)
    converted_value = from_decimal(decimal_value, 2)
    assert converted_value == "11110000"

def test_round_trip_octal_to_base36():
    decimal_value = to_decimal("77", 8)
    converted_value = from_decimal(decimal_value, 36)
    assert converted_value == "25"
