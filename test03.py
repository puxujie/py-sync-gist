'''
要确定元组中是否存在指定的项，请使用 in 关键字：
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

'''
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
# in 判断元组里是否有apple

'''Python 集合'''
#  set
#创建集合  变量 = { } 花括号编写
'''
thisset = {"apple", "banana", "cherry"}
print( thisset )
   集合是无序的
'''

'''
添加项目
要将一个项添加到集合，请使用 add() 方法。
要向集合中添加多个项目，请使用 update() 方法。
'''
thisset = {"apple", "banana", "cherry"}
thisset.add("orange") #add只能添加单个
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.update(["orange","mango","grapes"])#update 可以添加多个
print(thisset)

'''
删除项目
要删除集合中的项目，请使用 remove() 或 discard() 方法。
'''
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #remove 
#删除项目“banana”如果指定的项目不存在，则 remove() 方法将引发错误，而 discard() 方法不会。
print(thisset)
'''discard()  删除项目“banana”  如果指定的项目不存在，
则remove() 方法将引发错误，而 discard() 方法不会。'''
thisset = {"apple", "banana", "cherry"}
thisset.discard("banane")
'''clear() 方法清空集合'''
thisset.clear()
print(thisset)

'''del 删除集合'''
del thisset
print(thistuple)

'''合并两个集合'''
set1 ={"a","b","c"}
set2 ={1,2,3,4,4} #排除任何重复项
set3=set1.union(set2) #union 可以让集合合并。包含两个集合中的所有项目
print(set3)

#update() 方法将 set2 中的项目插入 set1 中：
set1.update(set2)
print(set1)
#注释：union() 和 update() 都将排除任何重复项。

'''set() 构造函数来创建集合'''
thisset = set(("apple", "banana", "cherry")) # 请留意这个双括号,双括号代替 { }花括号
print(thisset)

'''集合 difference() 方法'''
x={"a","b","c"}
y={"a","e","f"}
z=x.difference(y) #集合x和集合y 做对比 突出x里的集合不同的输出。
print(z)

'''symmetric_difference 包含两个集合中的所有项目，但两个集合中都存在的项目,输出两个集合里都没有的'''

'''集合 intersection() 方法'''
x={"a","b","c"}
y={"a","e","f"}
z=x.intersection(y) #输出两个集合里相同的项目，返回包含存在于集合 x 和集合 y 中的项目的集合
print(z)
'''intersection_update() 方法'''
x={"a","b","c"}
y={"a","e","f"}
z=x.intersection_update(y)  #删除集合 x 和集合 y 都不存在的项目
print(z)
#intersection_update() 方法与 intersection() 方法不同，因为 intersection() 方法返回一个新集合，
# 其中没有不需要的项目，而 intersection_update() 方法从原始集中删除了不需要的项目。

'''集合 isdisjoint() 方法'''
x={"a","b","c"}
y={"a","e","f"}
z=x.isdisjoint(y)  #所有集合 x 中没有项目存在于集合 y 中，则返回 True
print(z)
#   第三天