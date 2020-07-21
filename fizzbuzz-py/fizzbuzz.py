def is_divisible(number, divisor):
    remainder = number % divisor
    # print(number, divisor, remainder)
    if remainder == 0:
        return True
    else:
        return False


# assert is_divisible(2, 2)
# assert is_divisible(2, 1)
# assert not is_divisible(2, 5)
# assert not is_divisible(5, 2)
# assert is_divisible(9, 3)
# assert not is_divisible(3, 9)
# print("passed")


# def fizzbuzz(number):
#     fizz, buzz = False, False
#     if is_divisible(number, 3):
#         fizz = True
#     if is_divisible(number, 5):
#         buzz = True
#     if fizz and buzz:
#         return "FizzBuzz"
#     elif fizz:
#         return "Fizz"
#     elif buzz:
#         return "Buzz"
#     else:
#         return number

# for number in range(1, 100):
#     print(fizzbuzz(number))

def fizzbuzz_concat(number):
    reply = ""
    if is_divisible(number, 3):
        reply = reply + "Fizz"
    if is_divisible(number, 5):
        reply = reply + "Buzz"
    if reply:
        return reply
    else:
        return number

for number in range(1, 100):
    print(fizzbuzz_concat(number))
