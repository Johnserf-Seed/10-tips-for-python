# Python编程中的10个小技巧

![Python version](https://img.shields.io/badge/python-v3.7.3-blue)

### Tips1、	交换变量

普遍的写法是利用一个中间变量tmp进行交换，例：

```python
a = 1;b = 2

tmp = a;a = b;b = tmp

print(a,b)
```
但是我们可以这样子写

```python
a = 1;b = 2

a, b = b, a

print(a,b)
```

**输出结果：**  *2,1*

### Tips2、	字符串格式化

```python
name = "JohnserfSeed";country = "China";age = 19
```

打印字符串我们习惯使用  +  连接，例：

```python
print("Hi, I'm " + name + ". I'm from " + country + ". And I'm " + str(age) + ".")
```

**输出结果：**  *Hi, I'm JohnserfSeed. I'm from China. And I'm 19.*

但是我们还可以使用f-string、format等方法实现，例：

```python
print("Hi, I'm %s. I'm from %s. And I'm %d." % (name,country,age))

print("Hi, I'm {}. I'm from {}. And I'm {}.".format(name,country,age))

print("Hi, I'm {0}. Yes, I'm {0}!".format(name))

#pytv > 3.6
print(f"Hi, I'm {name}. I'm from {country}. And I'm {age}.")    #f-string   花括号中可以写表达式，例：{age + 1} 输出20 或调用函数{age()}

```

#### **其中f-string方法需要pyt版本大于3.6**

**输出结果：**	

*Hi, I'm JohnserfSeed. I'm from China. And I'm 19.*
*Hi, I'm JohnserfSeed. I'm from China. And I'm 19.*
*Hi, I'm JohnserfSeed. Yes, I'm JohnserfSeed!*
*Hi, I'm JohnserfSeed. I'm from China. And I'm 19.*

### Tips3、	yield

创建一个斐波那契数列，并输出。我们习惯用函数封装，用数组存放，例：

```python
def fibonacci(n):
    """
    param :n = 斐波那契数列前n个数
    return:斐波那契数列
    """
    a = 0;b = 1
    nums = []
    for _ in range(n):
        nums.append(a)
        a, b = b ,a + b    
    return nums

for i in fibonacci(10):
    print(i)
```

但是我们可以写的更简洁一些，例：

```python
def fibonacci(n):
    """
    param :n = 斐波那契数列前n个数
    return:斐波那契数列
    """
    a = 0;b = 1
    for _ in range(n):
        yield a	#使用yield生成器，每次生成及时输出
        a, b = b ,a + b    

for i in fibonacci(10):
    print(i)
```

简单地讲，yield 的作用就是把一个函数变成一个 生成器(generator),执行到 yield a 时，fibonacci 函数就返回一个迭代值，下次迭代时，代码从 yield a 的下一条语句继续执行。

**输出结果：**

*0*
*1*
*1*
*2*
*3*
*5*
*8*
*13*
*21*
*34*

### Tips4、	列表解析式

创建一个水果列表，例：

```python
fruit = ["apple","pear","pineapple","orange","banana"]
```

挑选首字母a开头的水果我们可以用循环遍历，例：

```python
filtered_fruit = []
for f in fruit:
    if f.startswith("a"):
        filtered_fruit.append(f)
        
print(filtered_fruit)
```

但是我们可以用列表解析式写成一句话，例：

```python
filtered_fruit = [x for x in fruit if x.startswith("a")]

print(filtered_fruit)
```

构造了一个新列表，枚举所有fruit元素去判断首字母是否为大写

**输出结果：** *['apple']*

全部元素改成大写呢？ 按之前的写法，例：

```python
for i in range(len(fruit)):
    fruit[i] = fruit[i].upper()
    
print(fruit)
```

当然学会了解析式我们也可以这样做，例：

```python
fruit = [x.upper() for x in fruit]

print(fruit)
```

**输出结果：** *['APPLE', 'PEAR', 'PINEAPPLE', 'ORANGE', 'BANANA']*

### Tips5、	enumerate函数

还是那个fruit列表，我们想要输出所有元素必须要用到for循环，但是如果要输出元素下标及元素可没这么容易了，还好pyt提供了一个函数：enumerate()，例：

```python
for i,x in enumerate(fruit):
    print(i,x)
```

**输出结果：** 

*0 APPLE*
*1 PEAR*
*2 PINEAPPLE*
*3 ORANGE*
*4 BANANA*

### Tips6、	反向，顺序遍历

将fruit列表元素从后往前依次输出，我们只需使用reversed(),如果按照a~z的顺序输出呢，pyt还是提供了一个函数：sorted()，例：

```python
#将fruit元素从后往前依次输出
for i,x in enumerate(reversed(fruit)):
    print(i,x)

#a~z开头依次输出
for i,x in enumerate(sorted(fruit)):
    print(i,x)
```

**输出结果：** 

*0 BANANA*
*1 ORANGE*
*2 PINEAPPLE*
*3 PEAR*
*4 APPLE*

*0 APPLE*
*1 BANANA*
*2 ORANGE*
*3 PEAR*
*4 PINEAPPLE*

### Tips7、	字典合并

```python
a = {"rose": "123456", "xiaoming": "abc123"}
b = {"lilei": "111111", "zhangsan": "12345678"}
```



假设a，b两字典均为账号密码，如果想要合并，我们的思路一开始也是利用c[]的空白字典存入，例：

```python
c = {}
for k in a:
    c[k] = a[k]
for k in b:
    c[k] = b[k]

print(c)
```

我们还可以用另一种解包(unpacking)的思维,例：

```python
c = {**a, **b}  #**代表解包

print(c)
```

pyt里的**代表着解包，是不是比写两个循环来的快捷呢

**输出结果：** *{'rose': '123456', 'xiaoming': 'abc123', 'lilei': '111111', 'zhangsan': '12345678'}*

### Tips8、	三元运算符

很多情况下我们需要判断一个变量并输出不同的字符，我们会使用if...else...的这张格式，例：

```python
if score > 60:
    s = "pass"
else:
    s = "fail"
    
print(s)
```

但是三元运算符可以很好地解决这个问题，例;

```python
s = "pass" if score > 60 else "fail"    #条件满足输出 s = "pass" 不满足输出 s ="fail"

print(s)

```

### Tips9、	序列解包

提取一些字符串中由空格分隔的字符时我们往往会用split()函数，但是字符串一多，代码就会变得冗长，例：

```python
#提取姓和名

name = "Johnserf Seed"

str_list = name.split()
first_name = str_list[0]
last_name = str_list[1]

print(first_name,last_name)
```

我们这时候要用到解包思维，和上面的字典合并方向一样，例：

```python
first_name, last_name = name.split()    #可以是序列，列表，元祖，数组

print(first_name,last_name)
```

**输出结果：** *Johnserf Seed* 

### Tips10、	with文件读取操作

pyt脚本很多情况下都需要读取、写入操作，我们都会用open()函数去打开这个对象，例：

```python
#打开文件并读取内容

f = open("somefile.txt", "r")
s = f.read()
f.close()   #切记关闭文件否则会一直占用资源

print(s)
```

这个写法如果应用到一些服务器项目上，随着读取资源的增加势必会造成服务器负担，这时候我们就可以用with open()的方法，例：

```python
with open("somefile.txt", "r") as f:
    s = f.read()

print(s)
```

这样子在我们读取完之后就会自己释放占用的资源，somefile文件就可以被读取并打印了。

**输出结果：** 

*..\1.txt*
*..\2.img*
*..\3.mp4*



**项目地址[10-tips-for-python](https://github.com/Johnserf-Seed/10-tips-for-python)**



#### 以上就是一些在日常编程中提高代码效率，可读性，简洁性的10个技巧

![嘻嘻](https://tva4.sinaimg.cn/large/006908GAly1gjgsqp2yk7g306o06ows4.gif)