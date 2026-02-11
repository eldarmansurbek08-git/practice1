# 1. Simple If Statement
age = 20

if age >= 18:
    print("You are an adult")  # True, because age is 20

if age < 18:
    print("You are a minor")   # False, won't print

# 2. Checking positive number
num = 5
if num > 0:
    print("Positive number")

# 3. Checking even number
number = 8
if number % 2 == 0:
    print("Even number")

# 4. Nested if
score = 85
if score >= 80:
    if score < 90:
        print("Good score")

# 5. Single line if
temperature = 30
if temperature > 25: print("It's hot today")
