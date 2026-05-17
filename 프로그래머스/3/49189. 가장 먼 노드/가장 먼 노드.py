from collections import deque

def solution(n, edge):
    #인접 리스트 
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        # 양방향 설정
        graph[a].append(b)
        graph[b].append(a)
    # 거리 기록 리스트
    # -1이 방문X
    distance= [-1] * (n+1)
    
    # 시작점 설정
    queue = deque([1])
    distance[1]=0 #1번 노드 자기 자신까지의 거리는 0
    #bfs 탐색
    while queue:
        current = queue.popleft()
        
        #현재 노드와 연결된 이웃노드들 하나씩 확인
        for neighbor in graph[current]:
            #방문확인
            if distance[neighbor] == -1:
                #이웃 노드의 거리: 현재 노드까지의 거리 +1
                distance[neighbor] = distance[current] +1
                queue.append(neighbor) #다음 탐색을 위해 큐에 추가
    # 가장 먼 거리 찾기
    max_distance = max(distance)
    
    # 가장 먼 거리에 있는 노드가 몇 개인지 반환
    return distance.count(max_distance)
                


    
