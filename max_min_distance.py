def max_min_distance(N: int, C: int, free_sections: list[int]) -> int:
    free_sections = merge_sort(free_sections)
    
    low = 0
    
    high = free_sections[-1] - free_sections[0]
    
    result = 0
    result_section = []
    
    while low <= high:
        mid = (low + high) // 2
        busy_section = []
        
        if can_place_cows(mid, N, C, free_sections, busy_section):
            result = mid
            result_section = busy_section
            low = mid + 1
        else:
            high = mid - 1

    print(f"{result} -> {result_section}")
    return result

def can_place_cows(mid: int, N: int, C: int, free_sections: list[int], busy_section: list[int]) -> bool:
    cows_placed = 1
    
    prev_stall = free_sections[0]
    busy_section.append(free_sections[0])
    
    for i in range(1, N):
        if free_sections[i] - prev_stall >= mid:
            cows_placed += 1
            prev_stall = free_sections[i]
            busy_section.append(prev_stall)
            if cows_placed == C:
                return True
    return False

def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)

def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == "__main__":
    # N = 5
    # C = 3
    # free_sections = [1, 2, 8, 4, 9]
    # result = max_min_distance(N, C, free_sections)
    # print(result)

    N = 10
    C = 5
    free_sections = [90, 60, 40, 30, 10, 5, 4, 3, 2, 1]
    result = max_min_distance(N, C, free_sections)
