n = int(input('Enter number - '))
st = 2
sum1 = 0
for i in range(0,n):
    sum1 += st
    st = st* 10 + 2
print(sum1)
