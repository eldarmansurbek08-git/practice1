
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
# n = int(input())
# a = list(map(int, input().split()))

# a.sort(reverse=True)

# print(*a)

# 211
# params = list(map(int, input().split()))[:3]
# n, start_ind, end_ind = params[0], params[1], params[2] 
# numbers = list(map(int, input().split()))[:n]
# reversed_list = list(reversed(numbers[start_ind - 1: end_ind]))
# numbers[start_ind - 1: end_ind] = reversed_list
# print(*numbers)

# 212
# n, numbers = int(input()), list(map(int, input().split()))
# for i in range(n): numbers[i] **= 2
# print(*numbers)

# 213
# n, trig = int(input()), 1

# if n < 2:
#    print("No")
# else:
#    for i in range(2, n):
#       if n%i == 0:
#          print("No")
#          break
#    else: print("Yes")

# 214
# n, numbers = int(input()), list(map(int, input().split()))

# freq = {}
# for num in numbers: freq[num] = freq.get(num, 0) + 1

# most_frequent = min(freq.keys(), key=lambda x: (-freq[x], x))
# print(most_frequent)

# 215
# n, surnames = int(input()), {''}
# for i in range(n): surnames.add(input())
# print(len(surnames) - 1)

# 216
# n, numbers = int(input()), list(map(int, input().split()))
# for i in range(len(numbers)):
#    if numbers[i] not in numbers[0: i]:
#       print("YES")
#    else: print("NO")

# 217
# n = int(input())
# freq = {}

# for i in range(n):
#     phone = input().strip()
#     freq[phone] = freq.get(phone, 0) + 1

# answer = 0
# for count in freq.values():
#     if count == 3:
#         answer += 1

# print(answer)

# 218
# n = int(input())
# first = {}

# for i in range(1, n+1):
#    s = input()
#    if s not in first:
#       first[s] = i

# for s in sorted(first):
#    print(s, first[s])

# 219
# n = int(input())
# watched = {}

# for i in range(n):
#    s, k = input().split()
#    k = int(k)
#    watched[s] = watched.get(s, 0) + k

# for name in sorted(watched):
#    print(name, watched[name])
