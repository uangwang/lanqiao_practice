key = ['a','b','c']
value = [123,456,789]
zipped = zip(key,value)
print(list(zipped))

a = dict(list(zip(key,value)))
print(a)

# 判断是否在字典中
print('a' in a.keys())
print(123 in a.values())
print(('a',123) in a.items())

d = {}
d['2'] = b
a['3'] = c
print(d)
print(d['2'])
