def solution(participant, completion):
    hash_dict = {}
    sum_hash = 0
    for i in participant:
        hash_dict[hash(i)] = i
        sum_hash += hash(i)
        
    for i in completion:
        sum_hash -= hash(i)
        
    return hash_dict[sum_hash]