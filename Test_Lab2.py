import Lab2

def test_calc_min_max_temperature():

    input_numlist = [1,2,3]
    expected = (1,3)
    result = Lab2.calc_min_max_temperature(input_numlist)
    assert result == expected

def test_calc_average_temperature():

    input_numlist = [1,2,3]
    expected = 2
    result = Lab2.calc_average_temperature(input_numlist)
    assert result == expected

def test_calc_median_temperature():

    input_numlist = [1,2,3]
    expected = 2
    result = Lab2.calc_median_temperature(input_numlist)
    assert result == expected