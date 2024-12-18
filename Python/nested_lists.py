if __name__ == '__main__':
    result = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        result.append([name, score])
    
#converting list to set to avoid duplicated records
second_highest = sorted(set([score for name, score in result]))[1]
print('\n'.join(sorted([name for name, score in result if score == second_highest])))
        