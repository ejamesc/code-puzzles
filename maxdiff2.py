def maxdiff(numbers):
    if len(numbers) < 2 or len(numbers) == 0:
        return 0

    curr_max = numbers[0]
    max_diff = 0
    for x in numbers:
        curr_max = max(x, curr_max)
        max_diff = max(curr_max - x, max_diff)

    return max_diff

if __name__ == '__main__':
    a = [4, 3, -10, 1]
    res = maxdiff(a)

    print res