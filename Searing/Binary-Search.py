def binary_search(element, some_list):
    left = 0
    right = len(some_list) - 1
    
    while left <= right:
        mid = (left + right) // 2 # 2로 나눈 정수
        if element == some_list[mid]:
            return mid
        elif element > some_list[mid]:
            left = mid + 1
        else:
            right = mid - 1