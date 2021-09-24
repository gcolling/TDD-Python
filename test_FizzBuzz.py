from fizzBuzz import fizzBuzz

def checkFizzBuzz(value, expected):
    actual = fizzBuzz(value)
    assert actual == expected

def test_canCallFizzBuzz():
    fizzBuzz(1)

def test_passingOne():
    checkFizzBuzz(1, "1")

def test_passingTwo():
    checkFizzBuzz(2, "2")

def test_fizzPassingThree():
    checkFizzBuzz(3, "Fizz")

def test_buzzPassingFive():
    checkFizzBuzz(5, "Buzz")

def test_fizzMultipleOfThree():
    checkFizzBuzz(6, "Fizz")

def test_buzzMultipleOfFive():
    checkFizzBuzz(10, "Buzz")

def test_fizzBuzzMultThreeAndFive():
    checkFizzBuzz(15, "FizzBuzz")