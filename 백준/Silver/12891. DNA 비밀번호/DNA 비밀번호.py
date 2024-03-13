from collections import deque

s, p = map(int, input().split())
string = list(str(input()))
A, C, G, T = map(int, input().split())

dic = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
i = 0
j = p - 1
arr = deque(string[i:j])
for k in arr:
    dic[k] += 1
cnt = 0

while j < s:
    dic[string[j]] += 1

    if dic['A'] >= A and dic['C'] >= C and dic['G'] >= G and dic['T'] >= T:
        cnt += 1

    dic[string[i]] -= 1
    i += 1
    j += 1

print(cnt)