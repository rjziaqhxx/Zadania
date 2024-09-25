num1 = 0
num2 = 1
print(num1, end=' ')
for i in range(8):
    result = num1 + num2
    num1 = num2
    num2 = result
    print(result, end=' ')
