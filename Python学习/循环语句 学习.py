# while 格式
'''
while 判断条件：
    语句
'''
#eg1. 统计字符个数
'''
mystr = input("请输入一行字符串：")
myletters = 0 # 字母数
myspaces = 0  # 空格数
mynums = 0 # 数字数
others = 0 
i = 0
while i < len(mystr):
    mychar = mystr[i] # 循环提取每个字符
    i = i + 1
    if mychar.isalpha():# 调用方法
        myletters = myletters + 1
    elif mychar.isspace():
        myspaces = myspaces + 1
    elif mychar.isdigit():
        mynums = mynums + 1
    else:
        others = + 1
print("字母数",myletters,"空格数",myspaces,"数字数",mynums,"其他数",others )

        
    

'''
#while else 语句  例如阶乘
'''
while 判断条件：
    语句1
else
    语句2
    
'''
# eg2. 求1—15 的 阶乘和
'''
n = 0
t = 1
s = 0
while n<15:
    n = n + 1
    t = t * n
    s = s + t
else:
    print(s)
'''

# for 循环
'''
格式
for <variable> in <sequence>:
    <statements>
'''
#eg3 . 遍历输入字符数
'''
mychar = input("请输入要遍历的字符串：")
for char in mychar:
    print(char)
'''

# for 循环中使用range()函数
'''
range()是用来创建数级数序列的通用函数 返回一个 [start , start+step , start+2*step , ]
range(stop)
range(start,stop[,step])

range()是一个左闭右开 序列数

'''
#eg4 . 求最大公约数
'''
num1 = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数"))
if num2 > num1 :
    temp = num2
    num2 = num1
    num1 = temp
for i in range(1,num2+1):
    if num1 % i == 0 and num2 % i == 0:
        mymax = i
print("\n\n 两个数的最大公约数为：",mymax)


# 拓展 海归画图
import turtle
turtle.screensize(800,600,"white")
stuname = turtle.textinput("请输入要输入的字：","输入文字对话框")
mycolors = ["green","red","blue","black"]
for x in range(80) :
    turtle.pencolor(mycolors[x%4])
    turtle.penup
    turtle.forward(x*4)
    turtle.down()
    turtle.write(stuname,font=("Arial",int((x+4)/4),"bold"))
    turtle.left(93)

'''
# 循环嵌套

#eg5 . 9 × 9 乘法表
'''
for i in range(1,10):
    print()
    for j in range(1,i+1):
        print("%d*%d=%d"%(i,j,i*j),end=' ')
'''
#eg 6. 杨辉三角
'''
coef = 1
rows = int(input("请输入显示的行数："))
for i in range(0,rows):
    for space in range(1,rows+1-i):
        print("  ",end = "")
    for j in range(0,i+1):
        if j==0 or i==0:
            coef = 1
        else:
            coef = int(coef * (i-j+1)/j)
        print(" ",coef,end="")
    print()
'''

# break 和 continue  语句
# pass 语句 ==> 空语句 ==> 不执行

















