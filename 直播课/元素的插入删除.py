a = ['apple', 'banana', 'cherry']
a.insert(1, 'orange')
print(a) # ['apple', 'orange', 'banana', 'cherry']
b=a.pop(3) # pop()方法删除指定位置的元素，如果没有指定，默认删除最后一个元素,并返回删除的元素
print(b) # cherry
print(a) # ['apple', 'orange', 'banana']
del a[0] # del删除指定位置的元素，无返回值
print(a) # ['orange', 'banana']
a.remove('banana') # remove()方法删除指定值的元素，无返回值
print(a) # ['orange']