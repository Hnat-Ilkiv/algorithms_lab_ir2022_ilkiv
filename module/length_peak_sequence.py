def length_peak_sequence(array: list[int]) -> int:
    longest_peak_length = 0
    i = 1

    while i < len(array) - 1:
        is_peak = array[i - 1] < array[i] > array[i + 1]

        if not is_peak:
            i += 1
            continue

    return longest_peak_length