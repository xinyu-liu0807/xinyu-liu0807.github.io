# python程序设计常用数据结构 list tuple(元组)、 dict(字典)\ set(集合)


# 5.1 list(左开右闭)
'''
list = ["我","喜欢","计算机","要","努力学习"]
for i in list:
    print(i)
print("数据：",list)
# 修改list中的信息
list[4] = "奋斗"
# 添加信息
list.append("nice")

print("数据：",list)

#删除数据
del list[3:4]
print("数据：",list)
'''

'''
输出
数据： ['我', '喜欢', '计算机', '要', '努力学习']
数据： ['我', '喜欢', '计算机', '要', '奋斗', 'nice']
数据： ['我', '喜欢', '计算机', '奋斗', 'nice']


'''
# 随机数
'''
import random
list1 = []
for i in range(1):
    mynum = random.randint(0,120)
    list1.append(mynum)
print("产生的随机数：",list1)
list1.sort()
print(list1)
'''


# 5.2 元组




















