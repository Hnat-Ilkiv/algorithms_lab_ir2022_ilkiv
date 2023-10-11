def max_min_distance(N, C, free_sections):
    free_sections.sort()
    
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

def can_place_cows(mid, N, C, free_sections):
    cows_placed = 1
    
    prev_stall = free_sections[0]
    
    for i in range(1, N):
        if free_sections[i] - prev_stall >= mid:
            cows_placed += 1
            prev_stall = free_sections[i]
            if cows_placed == C:
                return True
    return False

if __name__ == "__main__":
    N = 5
    C = 2
    free_sections = [1, 2, 8, 4, 9]
    result = max_min_distance(N, C, free_sections)
    print(result)
