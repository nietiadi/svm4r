import matplotlib.pyplot as plt
import numpy as np
#import math

"""
#抛物线
x = np.arange(-10, 10, 0.01)
y = x ** 2
plt.plot(x,y)
plt.show()

#log
x = np.arange(-10, 10, 0.01)
y = np.log(x)
plt.plot(x,y)
plt.show()

#幂函数
x = np.arange(-1, 1, 0.01)
y = 2 ** x
plt.plot(x,y)
plt.show()

x = np.arange(-10, 10, 0.01)
y = 2 ** x
plt.plot(x,y)
plt.show()
#plt.savefig()
plt.close()




labels=['Male','Female']
X=[30,20]
#fig = plt.figure(num="1-1")
#plt.pie(X,labels=labels,autopct='%1.2f%%') #画饼图（数据，数据对应的标签，百分数保留两位小数点）
plt.pie(X,labels=labels, autopct='%1.1f%%') #画饼图（数据，数据对应的标签，百分数保留两位小数点）
plt.title("Pie chart")
plt.legend()
plt.show()
#plt.savefig("piechart.png")
plt.close()
"""


# 柱子总数
N = 3
# 包含每个柱子对应值的序列
values = (30, 50, 20)
# 包含每个柱子下标的序列
index = np.arange(N)
width = 0.45
p2 = plt.bar(index, values, width, label="num")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Title')
# 添加纵横轴的刻度
plt.xticks(index, ('Beijing', 'Shanghai', 'Guangzhou'))
plt.yticks(np.arange(0, 70, 10))
plt.show()
