Number = 11
num = Number
count = 0
while num > 0:
    num //= 10
    count += 1
for i in range(count):
    first = Number // 10**(count-i-1)
    sec = Number % 10 
    Number -= first * 10 ** (count-i-1)
    Number //= 10
    count -= 1
    if first != sec: 
        print('Не полиндром')
        break
else:
    print('Палиндром')

print('END')
