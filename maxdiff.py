def maxdiff(numbers):
    if len(numbers) < 2 or len(numbers) == 0:
        return 0

    max, min, max_diff = maxdiff_core(numbers, 0, len(numbers) - 1)
    return max_diff

def maxdiff_core(numbers, start, end):
    if end == start:
        return numbers[start], numbers[start], 0

    middle = start + (end - start) / 2

    max_left, min_left, left_diff = maxdiff_core(numbers, start, middle)
    max_right, min_right, right_diff = maxdiff_core(numbers, middle + 1, end)

    cross_diff = max_left - min_right

    curr_max = max(max_left, max_right)
    curr_min = min(min_left, min_right)

    max_diff = max(left_diff, right_diff)
    max_diff = max(max_diff, cross_diff)

    # print max, min, max_diff
    return curr_max, curr_min, max_diff

if __name__ == '__main__':
    a = [4, 3, -10, 1]
    res = maxdiff(a)

    print res
