def find_2023(num):
    one = str(num).find('2')
    if  one == -1:
        return False
    two = str(num).find('0',one+1)
    if  two == -1:
        return False
    three = str(num).find('2',two+1)
    if  three == -1:
        return False
    four = str(num).find('3',three+1)
    if  four == -1:
        return False
    
    return True

count = 0
for i in range(12345678,98765433):
    if find_2023(i) is False:
        count += 1
print(count)
    
