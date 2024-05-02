def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
    else:
        arr[0] = -1
    return arr