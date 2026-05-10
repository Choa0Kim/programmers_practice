def solution(answers):
    # 수포자 3명 패턴 정의
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    # 각 수포자의 점수 담는 리스트
    scores = [0, 0, 0]
    
    #정답 비교
    for i in range (len(answers)):
        # i % len(p1): i가 0~5를 반복
        # p2의 경우에는 0~7을 반복
        if answers[i] == p1[i % len(p1)]:
            scores[0] +=1
        if answers[i] == p2[i % len(p2)]:
            scores[1] +=1
        if answers[i] == p3[i % len(p3)]:
            scores[2] +=1
            
    max_score = max(scores)
    
    # 결과 리스트출력 
    result = []
    for i in range(3):
        if scores[i] == max_score:
            result.append(i+1)
            
    return result
    
    
    
    