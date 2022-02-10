# -*- coding = utf-8 -*-
# @Time : 2022/2/8 20:19
# @Author : 保罗贝尔
# @File : demo1.py
# @Software : PyCharm

# 单行注释只需一个井号
print("hello world")

'''
多行注释用单引号
'''

print("python")

a = "abc"
print(a)
print("我今年")
b = 10
print("%d"%b) # %d代整数

age = 18
print("我的名字是%s, 我的国籍是%s"%("校长","中国")) # %s代字符串
print("我的年纪是:%d岁"%age)

print("aaa","bbb","ccc")
print("www","baidu","com",sep=".") #用.隔开每个字符串
print("hello",end="") #与下一句不隔开
print("world",end="\t") #与下一句隔开但在同一行
print("python",end="\n") #下一句另起一行
print("end")
