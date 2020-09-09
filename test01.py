#!/usr/bin/env python3
# coding:utf-8
# File: demo.py

whole = 'This is a example of too long string' + \
        ' which should be splited into multi-lines'+\
        ' to show it'
print(whole)

# 这是注释
print('hi, word!')  # 这也是注释,print输出（）里的东西。

#下面这些不能用作变量的命名。
'''False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield'''

print(1 != 3)

#布尔类型回答的是是非问题，那么什么情况下是True，什么情况下是False呢？ 
#Python里面实现了一个类型对象叫做bool，bool是一个int的子类，内置的True和False就是bool仅有的两个实例对象。
#bool的括号里就是判断内容是不是布尔量。
print(bool(0))
bool(())

'''
列表(list)
元组(tuple)
字典(dict)
集合(set)
'''


'''列表'''
list_a = ['a', 'b', 3, 8.9, [1,2]]
print(list_a[0]) #第一个
print(list_a[-1]) #倒数第一个

#通过索引我们可以访问到某个元素，那么我们就可以修改这个元素。
#没错，列表里面的元素是可以被修改的，相当于你先替别人排了个队，他来了就把你替换了。👇
list_b = ['a', 'b', 'c']
list_b[1] = 2
print(list_b)
#上面输出的是 ['a', 2, 'c']

list_a = ['a', 'b', 3, 8.9, [1,2]]
'''list(列表)的切片'''
list_a[1:3]#输出第二个和第四个
list_a[:3] #输出第四个前的全部 a, b, 3
list_a[1:] #输出第二个后的全部，包含第二个
list_a[:]  #输出list_a里的全部。

# 用 “ * ” 列表重复 |    ['a'] * 3      | 输出是 ['a', 'a', 'a']
# in 是否为列表元素 | 'a' in ['a', 'b'] | 输出是 True

'''删除list(列表)'''
del list_a #del 加上你的表格名
del list_a[0] # 删除一个元素
del list_a[1:3] # 删除切片

'''运算符	名称	含义'''
# "**"      幂    2**8得256
#  "%"     求余数 10 % 3得到1
#  "//"  向下取整除  11 // 2得到5

'''list(列表)推导式'''
'''
In [50]: even = [2 * i for i in range(10)]

In [51]: even
Out[51]: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

In [52]: even2 = [i for i in range(20) if i % 2 == 0]
In [53]: even2
Out[53]: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]                    '''
#生成even的过程是把0~10之间的数字都乘以2变成偶数；
#生成even2的过程是从0~20之间挑选出偶数。

