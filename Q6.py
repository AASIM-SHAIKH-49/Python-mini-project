import random
import math

try:
    numbers = set()

    while len(numbers) < 10:
        num = int(input("Enter a number: "))
        numbers.add(num)

    print("Unique Numbers:", numbers)

    t = tuple(numbers)

    print("Tuple:", t)

    print("Random Numbers:", random.sample(t, 3))

    total = sum(t)

    print("Square Root of Sum:", math.sqrt(total))

except ValueError:
    print("Please enter numbers only.")

except Exception as e:
    print("Error:", e)