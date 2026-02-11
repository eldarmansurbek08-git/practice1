# 1. Basic while loop
i = 1
while i <= 5:
    print(i)
    i += 1

# 2. While loop with condition
n = 10
while n > 0:
    print(n)
    n -= 2

# 3. Sum of numbers using while
total = 0
num = 1
while num <= 5:
    total += num
    num += 1
print("Sum:", total)

# 4. Print even numbers
x = 2
while x <= 10:
    print(x)
    x += 2

# 5. Break example
count = 1
while True:
    print(count)
    if count == 3:
        break
    count += 1
