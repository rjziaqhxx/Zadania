num = int(input('Enter number - '))
result = 0
while num != 0:
    num = num // 10
    result += 1
print(result)