# 用户管理系统
"""
print('用户管理系统'.center(50, '*'))
users = ['admin', 'lxy']
passwd = ['admin', 'lxy']


def info():
    print('1:添加用户\t\t', '2:删除用户\t\t', '3:查看所有用户\t\t', '4；退出\t\t', '5:更新用户')


while True:
    print(info())
    option = input("请输入操作：")
    if option == '1':
        print('添加用户'.center(50, '*'))
        adduser = input("输入用户名：")
        addpasswd = input("输入密码：")
        if adduser  in users:
            print("添加失败！")
        else:
            users.append(adduser)
            passwd.append(addpasswd)
            print("添加成功！")
    elif option == '2':
        print('删除用户'.center(50, '*'))
        deluser = input("输入需要删除的用户名：")
        if deluser not in users:
            print("没有该用户信息")
        else:
            delindex = users.index(deluser)
            users.remove(deluser)
            passwd.pop(delindex)
            print('删除信息成功!')
    elif option == '3':
        print('查找用户'.center(50,'*'))
        length = len(users)
        for i in range(0,length):
            print(users[i] ,'\t\t', passwd[i])
    elif option == '4':
        print("即将退出！ say bye")
        exit()

    elif option == '5':
        print("更新用户".center(50, '*'))
        upduser = input("请输入需要更新的用户：")
        if upduser not in users:
            print("输入正确的用户")
        else:
            print("请输入需要更新的是账号或密码：(7:用户/ 8: 密码)")
            shu = input("7/8:")
            updindex = users.index(upduser)
            if shu == '7':
                upuser = input("新用户名：")
                users[updindex] = upuser
            elif shu == '8':
                uppass = input("新密码：")
                passwd[updindex] = uppass

            print("更新成功！")

"""

















