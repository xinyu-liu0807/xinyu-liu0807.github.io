# numpy 数组对象 ndarray
import numpy as np
'''
a = np.array([[1, 2, 3], [1, 3, 4]], dtype=np.float32)
# a.size  # 返回长度
# a.shape  # 返回数组尺寸为元组 2行3列
# a.ndim  # 返回维度 2
# a.dtype
a.reshape(3, 2)  # 修改维度
list(range(10))
np.arange(10)
np.linspace(0, 10, 5)  # 等差数列
np.logspace(0, 10, 10)
#
data = np.array([0.2, 1.3, 3.4, 4.5], dtype=np.float32)
one = np.ones(2)  # [1, 1]
print(data + one, data * one, data - one, data / one, data * 1.6)
print(data[0:4])  # 数组切片

c = np.zeros((2.3, 3.3), dtype=np.float32)
type(c)   # 以元组创建
d = np.eye(3)
print(d * 9)
np.random.random(size=2)
np.random.randint(1, 10, size=(5, 3, 4))  # 5行 3列 4个维度

arr = np.arange(10)   # 从0-9 列出从0 开始的10个数
arr[-1]  # 从后面开始数第1个


# numpy矩阵
a = np.mat([[1, 2], [3, 4]])
b = np.mat([[1, 1], [1, 1]])
print(a * b)  # 注意矩阵乘法计算
print(a.T)  # 矩阵转置的概念 行 和 列 调换位置
print(a.H)  # 共轭矩阵 针对有复数的
print(a.I)  # 逆矩阵 AB = E 等于单位矩阵
print(a.A)  # 自身二维数组视图
'''
# numpy 进行文件读写

a = np.random.random((3, 3))
np.save('./tmp.npy', a)  # 当前文件夹下命名为tmp
b = np.random.randn(2, 2)
np.savez('./tmp2.npz', a, b)
np.load('./tmp.npy')
d = np.load('./tmp2.npz')
d['arr_0']
np.savetxt('./tmp3.txt', a)
np.loadtxt('tmp3.txt')
a.sort(axis=1)

e = np.array([92, 32, 3, 4, 3])
e.sort()
e.argsort()
e.repeat(e)
np.unique(e)

# 读取iris数据集中长度数据  并排序 去重 求和 等
data = np.loadtxt('./iris_sepal_length.csv')
data.sort()
m = np.unique(data)
np.sum(m)