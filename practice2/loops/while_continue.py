# 1. Continue example
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# 2. Skip even numbers
n = 0
while n < 6:
    n += 1
    if n % 2 == 0:
        continue
    print(n)

# 3. Skip multiple
x = 0
while x < 5:
    x += 1
    if x == 2 or x == 4:
        continue
    print(x)

# 4. Skip zero
nums = [-1,0,1]
i = 0
while i < len(nums):
    if nums[i] == 0:
        i += 1
        continue
    print(nums[i])
    i += 1

# 5. Continue with break
i = 0
while i < 5:
    i += 1
    if i == 2:
        continue
    print(i)
    if i == 4:
        break
