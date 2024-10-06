from varSwap import swap_values

def test_passed():
    val1 = -1
    val2 = 10
    val3 = 4
    val4 = -6
    
    student_result = swap_values(val1, val2, val3, val4)
    
    assert isinstance(student_result, tuple)
    assert len(student_result) == 4

    test1, test2, test3, test4 = student_result
    
    assert test1 == 10
    assert test2 == -1

def test_passed_2():
    val1 = 9
    val2 = 0
    val3 = 13
    val4 = -5
    
    student_result = swap_values(val1, val2, val3, val4)
    
    assert isinstance(student_result, tuple)
    assert len(student_result) == 4
    
    test1, test2, test3, test4 = student_result
    
    assert test1 == 0
    assert test2 == 9
    assert test3 == -5
    assert test4 == 13

def test_passed_3():
    val1 = 11
    val2 = 11
    val3 = 11
    val4 = 11
    
    student_result = swap_values(val1, val2, val3, val4)
    
    assert isinstance(student_result, tuple)
    assert len(student_result) == 4
    
    test1, test2, test3, test4 = student_result
    
    assert test1 == 11
    assert test2 == 11

def test_passed_4():
    val1 = 3
    val2 = 8
    val3 = 2
    val4 = 4
    
    student_result = swap_values(val1, val2, val3, val4)
    
    assert isinstance(student_result, tuple)
    assert len(student_result) == 4
    
    test1, test2, test3, test4 = student_result
    
    assert test1 == 8
    assert test2 == 3
    assert test3 == 4
    assert test4 == 2

def test_passed_5():
    val1 = 5
    val2 = 7
    val3 = 1
    val4 = 9
    
    student_result = swap_values(val1, val2, val3, val4)
    
    assert isinstance(student_result, tuple)
    assert len(student_result) == 4
    
    test1, test2, test3, test4 = student_result
    
    assert test1 == 7
    assert test2 == 5
    assert test3 == 9
    assert test4 == 1

def test_passed_6():
    val1 = 0
    val2 = 0
    val3 = 0
    val4 = 0
    
    student_result = swap_values(val1, val2, val3, val4)
    
    assert isinstance(student_result, tuple)
    assert len(student_result) == 4
    
    test1, test2, test3, test4 = student_result
    
    assert test1 == 0
    assert test2 == 0
    assert test3 == 0
    assert test4 == 0