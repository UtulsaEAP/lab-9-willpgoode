# Import student module you would like to test.
# For example:
# from main import add

from intToBin import int_to_reverse_binary, string_reverse

def test_int_to_reverse_binary():
    assert int_to_reverse_binary(19) == "11001"
    assert int_to_reverse_binary(255) == "11111111"
    assert int_to_reverse_binary(122) == "0101111"
    assert int_to_reverse_binary(0) == "0"
    assert int_to_reverse_binary(1) == "1"

def test_string_reverse():
    assert string_reverse("11001") == "10011"
    assert string_reverse("11111111") == "11111111"
    assert string_reverse("0101111") == "1111010"
    assert string_reverse("0") == "0"
    assert string_reverse("1") == "1"

