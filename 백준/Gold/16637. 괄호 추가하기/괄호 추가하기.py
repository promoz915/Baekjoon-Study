n = int(input())
s = list(input())
result = -1e9


def func(num1, order, num2):
    if order == '+':
        return num1 + num2
    elif order == '-':
        return num1 - num2
    else:
        return num1 * num2
    

def dfs(idx, value):
    global result
    
    if idx == n - 1:
        result = max(result, value)
        return
    
    if idx + 2 < n:
        dfs(idx+2, func(value, s[idx+1], int(s[idx+2])))
        
    if idx + 4 < n:
        dfs(idx+4, func(value, s[idx+1], func(int(s[idx+2]), s[idx+3], int(s[idx+4]))))
        

dfs(0, int(s[0]))
print(result)