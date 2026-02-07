
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
                    
