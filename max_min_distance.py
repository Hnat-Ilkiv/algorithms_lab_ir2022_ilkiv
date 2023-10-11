def max_min_distance(N: int, C: int, free_sections: list[int]) -> int:
    free_sections = merge_sort(free_sections)
    
    low = 0
    
    high = free_sections[-1] - free_sections[0]
    
    result = 0
    
    while low <= high:
        mid = (low + high) // 2
        
        if can_place_cows(mid, N, C, free_sections):
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result

def can_place_cows(mid: int, N: int, C: int, free_sections: list[int]) -> bool:
    cows_placed = 1
    
    prev_stall = free_sections[0]
    
    for i in range(1, N):
        if free_sections[i] - prev_stall >= mid:
            cows_placed += 1
            prev_stall = free_sections[i]
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
    N = 5
    C = 3
    free_sections = [1, 2, 8, 4, 9]
    result = max_min_distance(N, C, free_sections)
    print(result)