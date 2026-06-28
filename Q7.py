numbers = list(range(1, 11))

# Square using lambda
squares = list(map(lambda x: x ** 2, numbers))

print("Squares:", squares)

# Even squares using list comprehension
even_squares = [x for x in squares if x % 2 == 0]

print("Even Squares:", even_squares)