# -*- coding = utf-8 -*-
# @Time : 2022/2/10 0:00
# @Author : 保罗贝尔
# @File : 2-10.py
# @Software : PyCharm

import time

def sum02e(n):
    start = time.time()
    theSum = 0
    for i in range(1,n+1):
        theSum += i
    end = time.time()
    return theSum, end - start

def sum02e2(n):
    start = time.time()
    theSum2 = (n*(n+1))/2
    end = time.time()
    return theSum2, end - start


for i in range(5):
    print("Sum is %d required %10.7f second" % sum02e2(10000000))

