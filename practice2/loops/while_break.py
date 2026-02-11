# 1. Break in while loop
i = 1
while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1

# 2. Break when a condition is met
n = 0
while n < 10:
    if n == 7:
        break
    print(n)
    n += 1

# 3. User input example (simulated)
i = 0
while i < 5:
    print(i)
    if i == 2:
        break
    i += 1

# 4. Search in list
numbers = [1,3,5,7,9]
index = 0
while index < len(numbers):
    if numbers[index] == 5:
        print("Found 5!")
        break
    index += 1

# 5. Infinite loop with break
x = 0
while True:
    print(x)
    x += 1
    if x > 2:
        break
