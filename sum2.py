
# Find two numbers in a sorted arr that sum to s
def sum(arr, s):
    print arr
    p1, p2 = 0, len(arr) - 1
    while p1 < p2:
        # print p1, p2
        curr = arr[p1] + arr[p2]
        if curr == s:
            return arr[p1], arr[p2]
        elif curr > s:
            p2 = p2 - 1
        elif curr < s:
            p1 = p1 + 1
    return (0, 0)

if __name__ == "__main__":
    input = [1, 2, 4, 7, 11, 15]
    pair = sum(input, 15)
    print str(pair[0]) + " " + str(pair[1])

    input2 = [1, 4, 45, 6, 10, -8]
    input2.sort()
    pair = sum(input2, 16)
    print str(pair[0]) + " " + str(pair[1])
