# lab - 1

# 101
# s = input()
# print("Hello,", s + "!")

# 102
# a = input()
# b = input()
# print(a +  "***" + b)

# 103
# a = input()
# if a.isdigit():
#     print("int")
# else: 
#     print("str")

# 104
# a = input()
# b = input()
# print(int(a)+int(b))

# 105
# a = int(input())
# b = int(input())
# c = a // b
# d = a / b
# print(c)
# print(d)

# 106
# a = int(input())
# b = int(input())
# print(a**b)

# 107
# a = int(input())
# b = int(input())
# print(a%b)

# 108
# a = input()
# b = int(input())
# print(a*b)

# 109
# a = input()
# print(len(a))

# 110
# a = input()
# print(a.upper())
# print(a.lower())

# 111
# a = input()
# print(a[0], a[-1])

# 112
# a = input()
# print(a[2:5])

# 113
# a = input()
# print(a[::-1])

# 114
# a = input()
# b = int(input())
# print("Hello,", a + ". You are", b, "years old.")

# 115
# long = input()
# short = input()
# if short in long:
#     print(bool(-1))
# else:
#     print(bool(0))

# 116
# a = input()
# b = input()
# print(a+b)

# 117
# a = input()
# b = input()
# print(b, a)

# 118
# a = int(input())
# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")

# 119
# a = input()
# b = input()
# c = input()
# print(a.replace(b,c))

# 120
# a = int(input())
# b = int(input())
# if a > b:
#     print(a)
# elif a < b:
#     print(b)
# else:
#     print("equal")

# lab - 2

# 201
# a = int(input())
# if a % 4 == 0  and a % 100 != 0 or a % 400 == 0:
#     print("YES")
# else:
#     print("NO")

# 202
# a = int(input())
# sum = 0
# for i in range(a+1):
#     sum += i
# print(sum)

# 203
# a = int(input())
# n = input().split()
# sum = 0
# for i in range(a):
#     sum+=int(n[i])
# print(sum)

# 204
# a = int(input())
# n = input().split()
# cnt = 0
# for i in range(a):
#     if int(n[i]) > 0:
#         cnt += 1
# print(cnt)

# 205
# a = int(input())
# while a % 2 == 0:
#     a//=2
# if a == 1:
#     print("YES")
# else:
#     print("NO")



# 206
# a = int(input())
# n = input().split()
# max = int(n[0])
# for i in range(a):
#     if int(n[i]) > max:
#         max = int(n[i])
# print(max)

# 207
# a = int(input())
# n = input().split()
# pos = 1
# max = int(n[0])
# for i in range(1,a):
#     if int(n[i]) > max:
#         max = int(n[i])
#         pos = i + 1
# print(pos)

# 208
# a = int(input())
# n = 1
# while n <= a:
#     print(n, end=' ')
#     n*=2

# 209
# n = int(input())
# s = list(map(int , input().split()))
# mx = s[0]
# mn = s[0]
# for i in range(n):
#     if s[i] > mx:
#         mx = s[i]
#     if s[i] < mn:
#         mn = s[i]
# for i in range(n):
#     if s[i] == mx:
#         s[i] = mn
# for i in range(n):
#     print(s[i], end=' ')

# 210
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    swapped = False
    for j in range(0,n - i - 1 ):
        if n[i] > n[j + 1]:
            n[j], n[j + 1] = n[j + 1], n[j]
            swapped = True
    if not swapped:
        break
return n
                    
