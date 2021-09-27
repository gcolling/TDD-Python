def fizzBuzz(value):
    res = ""
    if value % 3 == 0: res = "Fizz"
    if value % 5 == 0: res = res + "Buzz"
    if res == "": res = str(value)
    return res