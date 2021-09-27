from fizzBuzz import fizzBuzz

class Test_FizzBuzz:
    def checkFizzBuzz(self, value, expected):
        actual = fizzBuzz(value)
        assert actual == expected

    def test_canCallFizzBuzz(self):
        fizzBuzz(1)

    def test_passingOne(self):
        self.checkFizzBuzz(1, "1")

    def test_passingTwo(self):
        self.checkFizzBuzz(2, "2")

    def test_fizzPassingThree(self):
        self.checkFizzBuzz(3, "Fizz")

    def test_buzzPassingFive(self):
        self.checkFizzBuzz(5, "Buzz")

    def test_fizzMultipleOfThree(self):
        self.checkFizzBuzz(6, "Fizz")

    def test_buzzMultipleOfFive(self):
        self.checkFizzBuzz(10, "Buzz")

    def test_fizzBuzzMultThreeAndFive(self):
        self.checkFizzBuzz(15, "FizzBuzz")