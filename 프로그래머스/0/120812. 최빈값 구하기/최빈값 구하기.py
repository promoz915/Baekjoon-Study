def solution(array):
    temp = set(array)
    max_cnt = 0
    for i in temp:
        cnt = array.count(i)
        if max_cnt < cnt:
            max_cnt = cnt
            ans = i
        elif max_cnt == cnt:
            ans = -1
    return ans