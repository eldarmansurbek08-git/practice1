# 1. Skip i == 3
for i in range(5):
    if i == 3:
        continue
    print(i)

# 2. Skip even numbers
for n in range(6):
    if n % 2 == 0:
        continue
    print(n)

# 3. Skip multiple
for x in range(1,6):
    if x == 2 or x == 4:
        continue
    print(x)

# 4. Skip letter 'a'
for c in "banana":
    if c == "a":
        continue
    print(c)

# 5. Continue with break
for i in range(5):
    if i == 1:
        continue
    print(i)
    if i == 3:
        break
