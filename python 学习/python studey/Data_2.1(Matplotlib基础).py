# 数据可视化基础
import matplotlib.pyplot as plt
import numpy as np

'''
plt.figure(figsize=(4, 4))
x = np.arange(10)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.legend(['sin', 'cos'])
plt.show()

os.listdir('./')
data = np.loadtxt('./国民经济核算季度数据.npz')
plt.scatter(range(69), data['values'][:, 2])
'''

data = np.load('国民经济核算季度数据.npz', allow_pickle=True)
data.files
plt.scatter(range(69), data['values'][:, 2])
plt.show()

l = ['r', 'g', 'b']
m = ['o', '*', 'D']
for j,i in enumerate([3, 4, 5]):
    plt.plot(range(69), data['values'][:, i], c=l[j], marker=m[j], alpha=0.5 )
plt.legend(['1', '2', '3'])
plt.show()

x = np.arange(0,  3 * np.pi,  0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
# 建立 subplot 网格，高为 2，宽为 1
# 激活第一个 subplot
plt.subplot(2,  1,  1)
# 绘制第一个图像
plt.plot(x, y_sin)
plt.title('Sine')
# 将第二个 subplot 激活，并绘制第二个图像
plt.subplot(2,  1,  2)
plt.plot(x, y_cos)
plt.title('Cosine')
# 展示图像
plt.show()

# 三个常用图像
# 1.直方图：
num = data['values'][68, 3:6]
plt.bar(range(len(num)),num)
plt.xticks(range(len(num)),['1', '2', '3'])

x = [5, 7, 9]
y = [12, 16, 6]
x2 = [6, 8, 10]
y2 = [6, 15, 7]
plt.bar(x, y, align='center')
plt.bar(x2, y2, color='g', align='center')
plt.title('Bar graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()

# 2.饼图
plt.figure(figsize=(4,4))
plt.pie(num,autopct='%.2f %%', explode=[0.1, 0, 0], labels=['1', '2', '3'])
plt.show()

# 3.箱线图
num = (list(data['values'][:, 3]),list(data['values'][:, 4]),list(data['values'][:, 5]))

plt.boxplot(num)
plt.show()