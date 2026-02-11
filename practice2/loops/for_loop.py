# 1. Basic for loop
for i in range(5):
    print(i)

# 2. Loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 3. Sum numbers
total = 0
for i in range(1,6):
    total += i
print("Sum:", total)

# 4. Loop with step
for i in range(0,10,2):
    print(i)

# 5. Nested for loop
for i in range(1,4):
    for j in range(1,3):
        print(i, j)
