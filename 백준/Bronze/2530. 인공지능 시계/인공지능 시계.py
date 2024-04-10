hour, minute, second = map(int, input().split())
data = int(input())

second += data % 60
data = data // 60
if second >= 60:
    second -= 60
    minute += 1

minute += data % 60
data = data // 60
if minute >= 60:
    minute -= 60
    hour += 1

hour += data % 24
if hour >= 24:
    hour -= 24

print(hour, minute, second)