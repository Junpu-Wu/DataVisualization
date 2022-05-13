import jieba
import pandas
import pandas as pd
import numpy as np
import xlwt
import wordcloud
from collections import Counter
import matplotlib.pyplot as matplo

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 1500)
pd.set_option('display.width', 50)


class DataProcess:
    def __init__(self, xls, sheet):  # 初始化类型
        self.xls = xls
        self.data = pd.read_excel(xls, sheet_name=sheet)

    def drop_blank(self, coloum_name):  # 删除存在的空行
        self.data = self.data.dropna(subset=coloum_name)
        self.data.reset_index(drop=True, inplace=True)
        print("已完成" + coloum_name + "列的过滤！")
        return

    def save_to_excel(self):
        self.data.to_excel('aftClean.xls', sheet_name='0')
        print('数据已保存')
        return


def main():
    obj = DataProcess(r'D:\Library\Code\PyCharm_Project\douban_com\text.xls', sheet=0)
    obj.data = obj.data[['name', 'area', 'decorate', 'nearSubway', 'rentFee']]
    obj.drop_blank('name')  # '过滤空置行'
    obj.drop_blank('area')
    obj.data.fillna(value=0)
    obj.data['nearSubway'].fillna('非近地铁', inplace=True)
    obj.data['decorate'].fillna('非精装', inplace=True)
    # print(obj.data)
    obj.save_to_excel()
    data2 = pandas.DataFrame(columns=['area', 'decorate', 'nearSubway', 'rentFee'])
    print((type(obj.data)))
    index2 = 0
    for index, row in obj.data.iterrows():
        if row['name'] == '誉峰三期':
            data2.loc[index2] = [row['area'], row['decorate'], row['nearSubway'], row['rentFee']]
            index2 += 1
    data2.to_excel('yufeng.xls', sheet_name='2')
    print('已经整理出招商大魔方的数据！')
    for index, row in data2.iterrows():  # 为‘装修’‘近地铁’两列进行编码
        print(type(row['decorate']))
        if row['decorate'] == '精装':
            data2.at[index, 'decorate'] = 1
        else:
            data2.at[index, 'decorate'] = 0
        if row['nearSubway'] == '近地铁':
            data2.at[index, 'nearSubway'] = 1
        else:
            data2.at[index, 'nearSubway'] = 0
    data2['rentFee'] = data2['rentFee'] / 1000  # 将单位改为千元
    print(data2)
    data2.to_excel('yufeng2.xls', sheet_name='3')
    return


main()
