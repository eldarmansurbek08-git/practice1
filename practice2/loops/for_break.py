# 1. Break when i == 3
for i in range(10):
    if i == 3:
        break
    print(i)

# 2. Break in list
nums = [1,2,3,4]
for n in nums:
    if n == 3:
        break
    print(n)

# 3. Nested break
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i,j)

# 4. Break in string
for c in "Python":
    if c == "h":
        break
    print(c)

# 5. Stop on condition
for i in range(5):
    print(i)
    if i == 2:
        break
