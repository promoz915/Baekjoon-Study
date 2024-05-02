from itertools import combinations

def check(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    val_sum = []
    for value in combinations(nums, 3):
        val_sum.append(sum(value))
    for v in val_sum:
        if check(v):
            answer += 1
        else:
            continue
    return answer