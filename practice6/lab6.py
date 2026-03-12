#( 1
# n = int(input())
# numbers = list(map(int,input().split()))
# squares = map(lambda x: x**2, numbers)
# print(sum(squares))

# 2
# n = int(input())
# numbers = list(map(int,input().split()))
# even = list(filter(lambda x: x % 2 == 0,numbers))
# print(len(even)))

# 3
# n = int(input())
# names = input().split()
# for index,name in enumerate(names):
#     print(f"{index}:{name}", end=" ")
    
# 4
# n = int(input())
# A = list(map(int,input().split()))
# B = list(map(int,input().split()))
# sum = 0
# for i in range(n):
#     sum += A[i] * B[i]
# print(sum)

# 5
# s = input()
# v = "aeiouAEIOU"
# for i in s:
#     if i in v:
#         print("Yes")
#         break
# else:
#     print("No")

# 6
# n = int(input())
# s = list(map(int,input().split()))
# if all(x >= 0 for x in s):
#     print("Yes")
# else:
#     print("No")

# 7
# n = int(input())
# words = input().split()
# longest = max(words,key=len)
# print(longest)

# 8
# n = int(input())
# t = list(map(int,input().split()))
# d = sorted(set(t))
# for i in d:
#     print(i,end=' ')

# 9
# n = int(input())
# keys = input().split()
# values = input().split()
# d = dict(zip(keys,values))
# t = input()
# print(d.get(t,"Not found"))

# 10
# n = int(input())
# nums = list(map(int,input().split()))
# count = 0
# for i in nums:
#     if i != 0:
#         count +=1
# print(count)

