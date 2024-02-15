# Import student module you would like to test.
# For example:
# from main import add
from intToBin import int_to_reverse_binary
from intToBin import string_reverse

def test_passed():
    studentResultBinary = int_to_reverse_binary(19)
    correctResultBinary = "11001"
    if studentResultBinary is None:
        return False

    studentResultReverse = string_reverse(studentResultBinary)
    correctResultReverse = "10011"
    if studentResultReverse is None:
        return False

    if studentResultBinary == correctResultBinary and studentResultReverse == correctResultReverse:
        return True
    elif studentResultBinary != correctResultBinary:
        return False
    elif studentResultReverse != correctResultReverse:
        return False
def test2_passed():    
    # Test case 2
    studentResultBinary = int_to_reverse_binary(255)
    correctResultBinary = "11111111"
    if studentResultBinary is None:
        return False

    studentResultReverse = string_reverse(studentResultBinary)
    correctResultReverse = "11111111"
    if studentResultReverse is None:
        return False

    if studentResultBinary == correctResultBinary and studentResultReverse == correctResultReverse:
        return True
    elif studentResultBinary != correctResultBinary:
        return False
    elif studentResultReverse != correctResultReverse:
        return False
    
    # Test case 3
def test3_passed(): 
    studentResultBinary = int_to_reverse_binary(122)
    correctResultBinary = "0101111"
    if studentResultBinary is None:
        return False

    studentResultReverse = string_reverse(studentResultBinary)
    correctResultReverse = "1111010"
    if studentResultReverse is None:
        return False

    if studentResultBinary == correctResultBinary and studentResultReverse == correctResultReverse:
        return True
    elif studentResultBinary != correctResultBinary:
        return False
    elif studentResultReverse != correctResultReverse:
        return False

# Example usage
result = test_passed()
result2=test2_passed()
result3 = test3_passed()
print(result)
print(result2)
print(result3)
