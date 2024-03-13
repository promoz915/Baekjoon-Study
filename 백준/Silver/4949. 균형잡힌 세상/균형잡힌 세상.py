while True:
    a = input()
    arr = []

    if a == ".":
        break

    for i in a:
        if i == '[' or i == '(':
            arr.append(i)
        elif i == ']':
            if len(arr) != 0 and arr[-1] == '[':
                arr.pop()
            else:
                arr.append(i)
                break
        elif i == ')':
            if len(arr) != 0 and arr[-1] == '(':
                arr.pop()
            else:
                arr.append(i)
                break
    print('yes' if len(arr) == 0 else 'no')