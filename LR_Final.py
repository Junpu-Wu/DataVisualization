import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# pd.set_option('display.max_columns', 10)
# pd.set_option('display.max_rows', 1500)
# pd.set_option('display.width', 50)

df_X = pd.read_excel(r'D:\Library\Code\PyCharm_Project\douban_com\yufeng2.xls', sheet_name=0)
df_X=df_X[['area', 'decorate', 'nearSubway', 'rentFee']]
print(df_X.corr()['rentFee']) # 相关性分析

y =np.array(df_X['rentFee'])
df_X1 = df_X.drop(['rentFee', 'decorate', 'nearSubway'], axis=1)
df_X2 = df_X.drop(['rentFee'], axis=1)
X = np.array(df_X1)
X2 = np.array(df_X2)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

from sklearn import preprocessing
# 初始化标准化器
min_max_scaler = preprocessing.MinMaxScaler()
# 分别对训练和测试数据的特征以及目标值进行标准化处理
X_train = min_max_scaler.fit_transform(X_train)
y_train = min_max_scaler.fit_transform(y_train.reshape(-1, 1)) # reshape(-1,1)指将它转化为1列，行自动确定
X_test = min_max_scaler.fit_transform(X_test)
y_test = min_max_scaler.fit_transform(y_test.reshape(-1, 1))

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
# 使用训练数据进行参数估计
lr.fit(X_train, y_train)
# 使用测试数据进行回归预测
y_test_pred = lr.predict(X_test)
# 训练数据的预测值
y_train_pred = lr.predict(X_train)
# print(y_train_pred)
# 线性回归的系数
print('单变量线性回归的系数为:\n w = %s \n b = %s' % (lr.coef_, lr.intercept_))

plt.scatter(X_train, y_train, marker='x')
plt.plot(X_train, y_train_pred, c='r')

plt.xlabel("x")
plt.ylabel("y")
plt.show()

from sklearn.metrics import mean_squared_error
error_train = mean_squared_error(y_train, y_train_pred)
error_test = mean_squared_error(y_test,y_test_pred)
print('线性回归训练测试总误差为：{}'.format(error_test+error_train))



from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X2, y, test_size=0.2, random_state=0)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

from sklearn import preprocessing
# 初始化标准化器
min_max_scaler = preprocessing.MinMaxScaler()
# 分别对训练和测试数据的特征以及目标值进行标准化处理
X_train = min_max_scaler.fit_transform(X_train)
y_train = min_max_scaler.fit_transform(y_train.reshape(-1, 1)) # reshape(-1,1)指将它转化为1列，行自动确定
X_test = min_max_scaler.fit_transform(X_test)
y_test = min_max_scaler.fit_transform(y_test.reshape(-1, 1))

from sklearn.linear_model import LinearRegression
lr = LinearRegression()
# 使用训练数据进行参数估计
lr.fit(X_train, y_train)
# 使用测试数据进行回归预测
y_test_pred = lr.predict(X_test)
# print(y_test_pred)
y_train_pred = lr.predict(X_train)
# print(y_train_pred)
# 线性回归的系数
print('多变量线性回归的系数为:\n w = %s \n b = %s' % (lr.coef_, lr.intercept_))


from sklearn.metrics import mean_squared_error
error_train = mean_squared_error(y_train, y_train_pred)
error_test = mean_squared_error(y_test,y_test_pred)
print('线性回归训练测试总误差为：{}'.format(error_test+error_train))

