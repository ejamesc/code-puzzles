
def find_valleys(arr):
    peaks = []
    for i in xrange(0, len(arr)):
        if i == 0 and arr[i] > arr[i + 1]:
            peaks.append((i, arr[i]))
        elif i == (len(arr) - 1) and arr[i] > arr[i - 1]:
            peaks.append((i, arr[i]))
        elif arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            peaks.append((i, arr[i]))

    # reduce peaks
    has_merged = False
    while has_merged:
        to_remove = []
        for i in xrange(0, len(peaks)):
            if i != 0 or i != len(peaks) - 1:
                curr, next, prev = peaks[i], peaks[i + 1], peaks[i - 1]
                if curr[1] < next[1] and curr[1] < prev[1]:
                    has_merged = True
                    to_remove.append(i)

        for i in to_remove:
            peaks.pop(i)

    res_sum = 0
    for i in xrange(0, len(peaks) - 1):
        # print res_sum
        res_sum += calculate_area(peaks[i], peaks[i + 1], arr)

    return res_sum

def calculate_area(start, end, arr):
    # print "starting from", start[0], "to", end[0]
    mm = min(start[1], end[1])
    s = 0
    for i in xrange(start[0] + 1, end[0]):
        curr_sum = mm - arr[i]
        s += curr_sum if curr_sum > 0 else 0

    return s

if __name__ == "__main__":
    input = [4, 3, 2, 1, 5, 6, 3, 2, 3, 4]

    res = find_valleys(input)
    print res
