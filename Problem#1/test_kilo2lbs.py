from kilo2lbs import kilo_to_pounds

def tests_passed():
    # Test case 1: kilo_to_pounds(0)
    student_pounds_0 = kilo_to_pounds(0)
    if abs(student_pounds_0 - 0) < 0.00000001:
        print("kilo_to_pounds(0) correctly returned 0.")
    else:
        print("kilo_to_pounds(0) incorrectly returned " + str(student_pounds_0) + ".")
        return False

    # Test case 2: kilo_to_pounds(10)
    student_pounds_10 = kilo_to_pounds(10)
    if abs(student_pounds_10 - 22.040) < 0.00000001:
        print("kilo_to_pounds(10) correctly returned 22.040.")
    else:
        print("kilo_to_pounds(10) incorrectly returned " + str(student_pounds_10) + ".")
        return False

    return True

if __name__ == "__main__":
    result = tests_passed()

   
