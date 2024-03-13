word = input().upper()
count = [0] * 26

for char in word:
    if 'A' <= char <= 'Z':
        count[ord(char) - ord('A')] += 1
        
max_count = max(count)

if count.count(max_count) > 1:
    print('?')
else:
    max_index = count.index(max_count)
    result_char = chr(max_index + ord('A'))
    print(result_char)