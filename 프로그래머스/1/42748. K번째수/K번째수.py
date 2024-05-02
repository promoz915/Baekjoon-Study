def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        data = array[commands[i][0]-1:commands[i][1]]
        data.sort()
        answer.append(data[commands[i][2]-1])
    return answer