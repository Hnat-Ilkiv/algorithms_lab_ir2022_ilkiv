def length_peak_sequence(array: list[int]) -> int:
    print(array)

    longest_peak_length = 0
    longest_left_index = 0
    longest_right_index = 0
    i = 1

    while i < len(array) - 1:
        is_peak = array[i - 1] < array[i] > array[i + 1]

        if not is_peak:
            i += 1
            continue

        left_index = i - 2
        while left_index >= 0 and array[left_index] < array[left_index + 1]:
            left_index -= 1

        right_index = i + 2
        while right_index < len(array) and array[right_index] < array[right_index - 1]:
            right_index += 1

        current_peak_length = right_index - left_index - 1
        longest_left_index = left_index + 1 if current_peak_length > longest_peak_length else longest_left_index
        longest_right_index = right_index if current_peak_length > longest_peak_length else longest_right_index
        longest_peak_length = max(longest_peak_length, current_peak_length)

        i = right_index

    print(f"{longest_peak_length} -> {array[longest_left_index:longest_right_index]}")

    return longest_peak_length

length_peak_sequence([4, 8, 9, 0, 1, 2, 3, 4, 0, 8, 9, 10, 0])

# length_peak_sequence([1, 2, 3, 4, 5])
# length_peak_sequence([5, 4, 3, 2, 1])
# length_peak_sequence([1, 2])
# length_peak_sequence([3, 2, 1, 2, 3])
# length_peak_sequence([1, 3, 5, 4, 2, 8, 3, 7, 2, 0])
# length_peak_sequence([1, 3, 5, 7, 4, 2, 9, 8])
# length_peak_sequence([8, 9, 2, 4, 7, 5, 3, 1])
