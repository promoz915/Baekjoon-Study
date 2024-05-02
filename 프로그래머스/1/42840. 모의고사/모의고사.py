def solution(answers):
    answer = []
    temp = [0 for i in range(3)]
    
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        if answers[i] == s1[i%5]:
            temp[0] += 1
        
        if answers[i] == s2[i%8]:
            temp[1] += 1
            
        if answers[i] == s3[i%10]:
            temp[2] += 1
            
    for idx, value in enumerate(temp):
        if value == max(temp):
            answer.append(idx+1)
    
    return answer