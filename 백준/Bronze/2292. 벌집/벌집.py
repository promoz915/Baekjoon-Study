n = int(input())
hive = 1
count = 1
while n > hive:
    hive += 6 * count
    count += 1
print(count)