for i in range(3, 0, -1):
    a = input()
    if a not in ["FizzBuzz", "Fizz", "Buzz"]:
        n = int(a) + i
if n % 5 == 0 and n % 3 == 0:
    print("FizzBuzz")
elif n % 5 == 0:
    print("Buzz")
elif n % 3 == 0:
    print("Fizz")
else:
    print(n)