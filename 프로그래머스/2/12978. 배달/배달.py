import heapq

def solution(N, road, K):
    # 인접리스트 
    graph = [[] for _ in range(N+1)]
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
        
        # 초기화
        dist = [float('inf')] * (N+1)
        dist[1] = 0
        
        queue = [(0, 1)]
        
        while queue:
            curr_dist, curr_node = heapq.heappop(queue)
            
            # 더 짧은 경로가 있다면 무시
            if dist[curr_node] < curr_dist :
                continue
                
            for neighbor, weight in graph[curr_node]:
                new_dist = curr_dist + weight
                
                # 최단 거리 발견하면 갱신
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(queue, (new_dist, neighbor))

    return len([d for d in dist if d <= K])

    
    
