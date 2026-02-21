# 1
# def square_gen(n):
#     for i in range(1,1+n):
#         yield i * i
# n = int(input())
# for num in square_gen(n):
#     print(num)

# 2
# def even_gen(n):
#     for i in range(0,n+1):
#         if i % 2 == 0:
#             yield str(i)
# n = int(input())
# print(','.join(even_gen(n)))

# def even_gen(limit):
#     for i in range(0, limit+1, 2):
#         yield i

# n = int(input())

# first = True
# for x in even_gen(n):
#     if not first:
#         print(',', end='')
#     print(x, end='')
#     first = False
# print()

# n = int(input())
# for i in range(0,n+1,2):
#     if i != 0:
#         print(",",end ="")
#     print(i,end="")

# 3
# def wws(n):
#     for i in range(0,n+1):
#         if i % 3 == 0 and i % 4 == 0:
#             yield i
# n = int(input())
# for x in wws(n):
#     print(x,end = ' ')

# 4
# def square_generetor(n , m):
#     for i in range(n , m+1):
#         yield i*i
# n , m = list(map(int , input().split()))
# for x in square_generetor( n , m):
#     print(x)

# 5
# def wws(n):
#     for i in range(n,-1,-1):
#         yield i
# n = int(input())
# for i in wws(n):
#     print(i)

# 6
# def wws(n):
#     a,b = 0,1
#     for _ in range(n):
#         yield str(a)
#         a,b = b,a+b
# n = int(input())
# print(','.join(wws(n)))

# 7
# n = input()
# print(n[::-1])

class Reverse:
    def __init__(self, string):
        self.data = string
        self.index = len(string) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        value = self.data[self.index]
        self.index -= 1
        return value
n = input()
for ch in Reverse(n):
    print(ch, end='')

