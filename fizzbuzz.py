for fizzbuzz in range(1,101):
    if fizzbuzz % 15 == 0:
        print("FizzBuzz")
        continue
    if fizzbuzz % 5 == 0:
        print("Buzz")
        continue
    if fizzbuzz % 3 == 0:
        print("Fizz")
        continue
    print(fizzbuzz)