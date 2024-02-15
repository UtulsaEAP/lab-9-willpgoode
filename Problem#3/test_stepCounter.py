

from stepCounter import feet_to_steps

def test_passed():
    
    # Test case 1 
    student_result = feet_to_steps(11)
 
    
   
    # Ensure correct return type
    if student_result is None:
        return False
   
    if student_result == (int)(11 / 2.5):
        pass
    else:
        return False
    # If all tests pass, return True
    return True
def test2_passed():    
    # Test case 2
    student_result = feet_to_steps(79.25)
   
    # Ensure correct return type
    if student_result is None:
        return False
   
    if student_result == (int)(79.25 / 2.5):
        pass
    else:
        return False

    # If all tests pass, return True
    return True

def test3_passed():
     # Test case 3
    student_result = feet_to_steps(150.5)
   
    # Ensure correct return type
    if student_result is None:
        return False
   
    if student_result == (int)(150.5 / 2.5):
        pass
    else:
        return False

    # If all tests pass, return True
    return True
    
result = test_passed()
result2=test2_passed()
result3=test3_passed()
print(result)
print(result2)
print(result3)
