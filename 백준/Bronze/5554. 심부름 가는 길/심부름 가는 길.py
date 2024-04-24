hour, minute = 0, 0
a = int(input())
b = int(input())
c = int(input())
d = int(input())
minute = a + b + c + d
if minute >= 60:
    hour = minute // 60
    minute %= 60
print(hour)
print(minute)