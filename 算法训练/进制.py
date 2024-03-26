# int_to_char = "0123456789ABCDEF"
# char_to_int ={}
#
# for idx,char in enumerate(int_to_char):
#     char_to_int[char] = idx
#
# def K_To_Ten(k,x):
#     ans = 0
#     for char in x:
#         ans = ans * k + char_to_int[char]
#     return ans

int_to_char = "0123456789ABCDEF"
char_to_int ={}

for idx,char in enumerate(int_to_char):
    char_to_int[char] = idx

def k_to_ten(k,x):
  ans = 0
  x = str(x)
  x = x[::-1]
  for i in range(len(x)):
    ans += char_to_int[x[i]] * k ** i
  return ans

print(k_to_ten(9,2022))