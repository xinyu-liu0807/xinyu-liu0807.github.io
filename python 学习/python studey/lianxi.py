# 练习 求sin(x) 从 0 到 2 * pi 与 x 轴 围成的面积
'''
import math
n = 10
width = 2 * math.pi / n
x = []
y = []
for i in range(n):
    x.append(i * width)
for i in x:
    y.append(abs(math.sin(i)))

s = sum(y)*width

print(s)
    
x = [abs(math.sin(i*width)) * width for i in range(n)]
print(sum(x))
'''

# 冒泡排序
'''
x = [1,2,6,7,3]
n = len(x)
for i in range(n):
    for j in range(i):
        if x[j] > x[i]:
            x[i],x[j] = x[j],x[i]
print(x)
'''

# 单词词频统计
'''
string = 'My name'
res = string[0]# 字符串索引
res = string[0:2]# 字符串切片
res = string * 2
print(res)
'''
# 字典 i:i**2 key ： value
'''
a = {i:i**2 for i in range(10)}
print(a)
'''
# python 对文件处理
# open(文件名，访问模式)
# f = open('Walden.txt','r')#以读的方式打开
# txt = f.read(100)#读取内容 read()中件为读取字符数
# txt_lines = f.readline()
# f.close()#关闭文件
# print(txt)
# print(txt_lines)
'''
import re
import os
path = os.getcwd()
print(path)

f = open('Walden.txt', 'r')  # 以读的方式打开 读的是字符串
txt = f.read()
f.close()
txt = re.sub('[,.?:"\'!-]', '', txt)  # 对标点符号字符去除
txt = txt.lower()  # 转小写
words = txt.split()  # 单词分割
word_sq = {}  # dict
type(word_sq)

for i in words:
    if i not in word_sq.keys():
        word_sq[i] = 1
    else:
        word_sq[i] += 1

res = sorted(word_sq.items(), key=lambda x: x[1], reverse=True)  # 排序
print(res)

type(res)
word_sq.keys()
word_sq.values()

'''

# 列表再学
'''
list1 = ['hello', 'world', 666]
print(list1)
# for i in list1:
#     print(i)
print(list1[2])  # 列表的索引
print(list1[0:2])  # 左闭右开

# 练习用户输入 判读属于那个月份
month = int(input("请输入月份的数字："))
if 1 <= month <= 3:
    print("spring")
elif 3 < month <= 6:
    print("summer")
elif 6 < month <= 9:
    print("autumn")
else:
    print("winter")
# 使用列表的方法：
month = int(input("请输入月份的数字："))
spring = [1, 2, 3]
summer = [4, 5, 6]
autumn = [7, 8, 9]
winter = [10, 11, 12]

if month in spring:
    print('spring')
elif month in summer:
    print('summer')
elif month in autumn:
    print('autumn')
elif month in winter:
    print('winter')
else:
    print("请输入正确年份")


# 练习 模拟栈的操作
# 定义一个空列表,用来表示栈
stack = []

# 定义操作选项的变量 三个“”“ 代表按照格式打印
info = """
        栈操作
    1.入栈
    2.出栈
    3.栈顶元素
    4.栈的长度
    5.栈是否为空
    q.退出
"""
# 无限循环
while True:
    # 输出操作选项信息
    print(info)
    choice = input('请输入选择:')
    if choice == '1':
        print('入栈'.center(50,'*'))
        # 接收入栈元素
        item = input('入栈元素:')
        # append:添加元素到列表中
        stack.append(item)
        print('元素%s入栈成功' % item)
    elif choice == '2':
        if len(stack) == 0:
            print('栈为空,无法出栈')
        else:
            print('出栈'.center(50, '*'))
            # pop:删除列表中的最后一个元素
            item = stack.pop()
            print('%s元素出栈成功' % item)
    elif choice == '3':
        # len:列表长度
        if len(stack) == 0:
            print('栈为空,无栈顶元素')
        else:
            print('栈顶元素为%s' % stack[-1])
    elif choice == '4':
        print('栈的长度为%s' % len(stack))
    elif choice == '5':
        if len(stack) == 0:
            print('栈为空')
        else:
            print('栈不为空')
    elif choice == 'q':
        break
    else:
        print('请输入正确的选择')
'''










