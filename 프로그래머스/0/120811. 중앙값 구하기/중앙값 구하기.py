def solution(array):
    array.sort(reverse=True)
    return array[len(array)//2]