import time

count = 0
while count < 5:
    print(time.time())
    count = count + 1

# 输入1--100所以数的和
num = 0
count1 = 0
while num < 100:
    num = num + 1
    count1 = count1 + num
print(count1)
print('----------------------------------------')

# 输出1--10内的所有偶数
num1 = 0
while num1 < 10:
    num1 = num1+1
    if num1 % 2 == 0:
        print(num1)

print('----------------------------------------')

# 输出1--10内的所有奇数
num1 = 0
while num1 < 10:
    num1 = num1+1
    if num1 % 2 == 1:
        print(num1)
print('----------------------------------------')

# 输出1 2 4 5
a = 1
while a < 6:
    if a == 3:
        pass
    else:
        print(a)
    a = a + 1
print('----------------------------------------')

# 输出1-2+3-4+......100的和
b = 1
sumB = 0
while b < 100:
    if b % 2 == 0:
        b = -b
    else:
        b = b
    sumB = sumB + b
    b = abs(b) + 1
print(sumB)
print('----------------------------------------')
# 另一种方法
b = 1
sumB = 0
while b < 100:
    if b % 2 == 0:
        sumB = sumB - b
    else:
        b = b
        sumB = sumB + b
    b = abs(b) + 1
print(sumB)
