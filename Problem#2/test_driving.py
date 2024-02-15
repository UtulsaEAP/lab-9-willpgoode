# from main import add
from driving import driving_cost

def test_passed():
    
    # Test case 1
    student_result = driving_cost(20.0, 3.1599, 10.0)
    
    # Ensure correct return type
    if student_result is None:
        print("driving_cost(20.0, 3.1599, 10.0) did not return a value.\nYour function may be missing a return statement.")
        return False
        
    diff_amount = student_result - 1.57995
    
    if diff_amount < 0:
        diff_amount = -diff_amount

    if diff_amount < 0.001:  # Close enough
        print("driving_cost(20.0, 3.1599, 10.0) correctly returned " + str(student_result))
        return True
    else:
        print("driving_cost(20.0, 3.1599, 10.0) incorrectly returned " + str(student_result))
        return False
    
    # Test case 2
def Test2_passed():
    student_result = driving_cost(20.0, 3.1599, 50.0)
    
    # Ensure correct return type
    if student_result is None:
        print("driving_cost(20.0, 3.1599, 50.0) did not return a value.\nYour function may be missing a return statement.")
        return False
    
    diff_amount = student_result - 7.89975

    if diff_amount < 0:
        diff_amount = -diff_amount

    if diff_amount < 0.001:  # Close enough
        print("driving_cost(20.0, 3.1599, 50.0) correctly returned " + str(student_result))
        return True
    else:
        print("driving_cost(20.0, 3.1599, 50.0) incorrectly returned " + str(student_result))
        return False
def test3_passed():
     # Test case 3
    student_result = driving_cost(20.0, 3.1599, 400.0)
    
    # Ensure correct return type
    if student_result is None:
        print("driving_cost(20.0, 3.1599, 400.0) did not return a value.\nYour function may be missing a return statement.")
        return False
    
    diff_amount = student_result - 63.198

    if diff_amount < 0:
        diff_amount = -diff_amount

    if diff_amount < 0.001:  # Close enough
        print("driving_cost(20.0, 3.1599, 400.0) correctly returned " + str(student_result))
    else:
        print("driving_cost(20.0, 3.1599, 400.0) incorrectly returned " + str(student_result))
        return False
    
    return True
test_passed()
Test2_passed()
test3_passed()
