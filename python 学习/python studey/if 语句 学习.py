# if 语句 注意：缩进相同的为一个语句块
'''
if 表达式1：
    语句1
    语句2
else：
    语句3



多重if
if 表达式1：
    语句1
elif 表达式2：
    语句2
else：
    语句n

    
'''

# 注意： 逻辑与为 and  逻辑或 or

# eg1.闰年判断
'''
year = input("请输入一个年份：")
myyear = int(year)
if(myyear%4==0 and myyear%100 != 0  or myyear%400 == 0):
     print(year,"是闰年")
else:
    print(year,"不是闰年")
'''

#eg2. 剪刀石头布 游戏 random随机数产生
'''
import random
player = int(input("请输入1（布），2（剪刀），3（石头）："))
computer = random.randint(1,3)# 产生1—3 的随机数
if( (player == 1 and computer == 3) or(player == 2 and computer == 1) or (player == 3 and computer == 2) ):
    print(play,computer," player ==> win")
elif ( player == computer ):
    print(player,computer," player = computer")
else:
    print(player,computer," computer ==> win")
'''

# 嵌套if
# eg3. 判断是否是3或7的倍数
'''
num = int(input("请输入一个数："))
if num %3==0 :
    if num %7==0:
        print(num,"能被3和7整除")
    else:
        print(num,"能被3整除，不能被7整除")
else:
    print(num,"不能被3 和 7 整除")
'''













