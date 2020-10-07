#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:10 tips for python
@Date       :2020/10/07 11:40:09
@Author     :JohnserfSeed
@version    :1.0
@Mail       :johnserfseed@gmail.com
@License    :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
'''

#import this
#python之父提供的编程建议


#tips1  变量交换

a = 1;b = 2

#old
#tmp = a;a = b;b = tmp

#new
a, b = b, a

print(a,b)


#tips2  字符串格式化

name = "JohnserfSeed";country = "China";age = 19

#old
#print("Hi, I'm " + name + ". I'm from " + country + ". And I'm " + str(age) + ".")

#new
print("Hi, I'm %s. I'm from %s. And I'm %d." % (name,country,age))

print("Hi, I'm {}. I'm from {}. And I'm {}.".format(name,country,age))

print("Hi, I'm {0}. Yes, I'm {0}!".format(name))

#pytv > 3.6
print(f"Hi, I'm {name}. I'm from {country}. And I'm {age}.")    #f-string   花括号中可以写表达式，例：{age + 1} 输出20 或调用函数{age()}


#tips3  yield

def fibonacci(n):
    """
    param :n = 斐波那契数列前n个数
    return:斐波那契数列
    """
    a = 0;b = 1
    #old
    #nums = []
    for _ in range(n):
        #new
        yield a
        #old
        #nums.append(a)
        a, b = b ,a + b    
    #old
    #return nums

for i in fibonacci(10):
    print(i)

#tips4  列表解析式

fruit = ["apple","pear","pineapple","orange","banana"]


#挑选a开头的水果

#old
#filtered_fruit = []
#for f in fruit:
#    if f.startswith("a"):
#        filtered_fruit.append(f)

#new
filtered_fruit = [x for x in fruit if x.startswith("a")]

print(filtered_fruit)


#全部水果改大写

#old
#for i in range(len(fruit)):
#    fruit[i] = fruit[i].upper()

#new
fruit = [x.upper() for x in fruit]  #构造一个新列表，枚举所有fruit元素并大写

print(fruit)


#tips5  enumerate函数

#输出列表所有元素

#old
#for x in fruit:
#    print(x)

#new
for i,x in enumerate(fruit):
    print(i,x)


#tips6.1  反向遍历

#将fruit元素从后往前依次输出
for i,x in enumerate(reversed(fruit)):
    print(i,x)


#tips6.2  顺序遍历

#a~z开头依次输出
for i,x in enumerate(sorted(fruit)):
    print(i,x)


#tips7  字典合并

a = {"rose": "123456", "xiaoming": "abc123"}
b = {"lilei": "111111", "zhangsan": "12345678"}

#old
#c = {}
#for k in a:
#    c[k] = a[k]
#for k in b:
#    c[k] = b[k]

#new
c = {**a, **b}  #**代表解包

print(c)


#tips8  三元运算符

score = 80

#old
#if score > 60:
#    s = "pass"
#else:
#    s = "fail"

#new
s = "pass" if score > 60 else "fail"    #条件满足输出 s = "pass" 不满足输出 s ="fail"

print(s)


#tips9  序列解包

#提取姓和名

name = "Johnserf Seed"

#old
#str_list = name.split()
#first_name = str_list[0]
#last_name = str_list[1]

#new
first_name, last_name = name.split()    #序列，列表，元祖，数组

print(first_name,last_name)


#tips10 with语句

#打开文件并读取内容

#old
#f = open("somefile.txt", "r")
#s = f.read()
#f.close()   #关闭文件否则一直占用资源

#new
with open("somefile.txt", "r") as f:
    s = f.read()

print(s)