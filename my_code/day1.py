from math import sqrt
from random import randint
# 华氏度转摄氏度
# f = input("化氏度：")
# print(type(f))
# f = float(f)
# print(type(f))
# C = (f - 32)/1.8
# print("摄氏度：%.1f" %C)

# # 输入圆的半径计算周长和面积
# r = float(input("请输入半径:"))
# PI = 3.141592653589793
# s = PI * r ** 2
# l = PI * r * 2 
# print("面积为： %.2f\n 周长为：%.2f" %(s, l))

# 英制单位英寸与公制单位厘米互换


# # 输入一个正整数判断是不是素数。
# from math import sqrt
# value = int(input("输入一个正整数："))
# end = int(sqrt(value))
# print(end)
# is_prime = True
# for i in range(2, end + 1):
#     if value % i == 0:
#         is_prime = False
#         break
# if is_prime:
#     print("%d是素数" %value)
# else:
#     print("%d不是素数" %value)


# # 输入两个正整数，计算它们的最大公约数和最小公倍数。
# a = int(input("a = "))
# b = int(input("b = "))

# for i in range(max(a, b), 0, -1):
#     if a % i == 0 and b % i == 0:
#         print("%d和%d的最大公约数为%d" %(a, b, i))
#         print('%d和%d的最小公倍数是%d' % (a, b, a * b // i))
#         break

# # 打印如下所示的三角形图案
# row = 5
# # *
# # **
# # ***
# # ****
# # *****
# for i in range(row):
#     for j in range(i + 1):
#         print("*", end ="") # 加end = "" 不自动换行
#     print()
# #     *
# #    **
# #   ***
# #  ****
# # *****
# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(" ", end = "")
#         else:
#             print("*", end ="") # 加end = "" 不自动换行
#     print()
# #     *
# #    ***
# #   *****
# #  *******
# # *********
# for i in range(row):
#     for _ in range(row - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     print()


# # 寻找水仙花数
# for i in range(100, 1000):
#     high = i // 100
#     mid  = i %  100 // 10
#     low  = i %  10
#     #print(high, mid, low, low ** 3 + mid ** 3 + high ** 3)
#     if low ** 3 + mid ** 3 + high ** 3 == i:
#         print(i)

# # 百钱百鸡问题
# for i in range(20):
#     for j in range(33):
#         k = 100 - i - j
#         if i * 5 + j * 3 + k / 3 == 100:
#             print("公鸡%d只，母鸡%d只，鸡仔%d只 " %(i, j, k))

# # CRAPS赌博游戏
# from random import randint

# go_on = False
# count = 2 
# count_win = 0

# for i in range(100):
#     first = randint(1, 6) + randint(1, 6)
#     print("第1次色子：%d" %first)
#     if first == 7 or first == 11 :
#         print("win")
#         count_win += 1
#     elif first == 2 or first == 3 or first == 12 :
#         print("loss")
#     else:
#         go_on = True
#     while go_on:
#         second = randint(1, 6) + randint(1, 6)    
#         print("第%d次色子：%d" %(count,second))
#         count += 1
#         if second == first:
#             print("win")
#             count_win += 1
#             go_on = False
#             count = 2
#         elif second == 7 :
#             print("loss")
#             go_on = False
#             count = 2
#         else:
#             go_on = True
# print("玩家赢次数:%d" %count_win)

# # 斐波那契数列
# a = 1
# b = 1
# print("1 1", end ="")
# for i in range(18):
#     c = a + b
#     a = b
#     b = c
#     print(" %d" %c, end ="")

# 找出10000以内的完美数。
is_prime = True
for i in range(2, 100):
    sd = int(sqrt(i))
    for j in range(2, sd + 1):
        if i % j == 0:
            is_prime = False 
            break
        else:
            is_prime = True
    if is_prime:
        print(i)




