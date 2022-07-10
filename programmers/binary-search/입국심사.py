def solution(n, times):

    answer = 0
    
    times.sort() # sorted() 도 있지만 원래 순서가 중요하지 않기 때문에 sort() 사용
    
    left = min(times) # 최소값
    right = max(times) * n # 최대값
    
    while left <= right:
        
        mid = (left + right) // 2 # 중간값
        
        passed = 0 # 통과 인원수
        for time in times:
            passed += mid // time # 시간별 통과 인원수 합계
            if passed >= n: # 모두 심사에 통과되면 break
                break

        if passed < n: # 모든 사람이 심사를 통과하지 못한 경우
            left = mid + 1
            continue

        right = mid - 1
        answer = mid

    return answer
