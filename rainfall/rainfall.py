from sys import stdin, maxint

class WaterCell:
    def __init__(self, id_tuple, value):
        self.isPartitioned = False
        self.id = id_tuple
        self.value = value
        self.next = None
        self.group = -1

    def __repr__(self):
        return str(vars(self))

def get_lowest(grid, x, y, debug=False):
    max = len(grid)
    if max < 2 or max == 0:
        return x, y

    # Up Down Left Right
    vals = []
    up = (x - 1, y)
    down = (x + 1, y)
    left = (x, y - 1)
    right = (x, y + 1)
    directions = [up, down, left, right]
    for d in directions:
        if is_valid(d, max):
            vals.append(grid[d[0]][d[1]].value)
        else:
            vals.append(maxint)

    if debug:
        print vals
    vals.append(grid[x][y].value)
    directions.append((x, y))

    minval = min(vals)
    ind = vals.index(minval)
    if debug:
        print "minval", minval
        print "ind", ind
        print directions

    return directions[ind]

def is_valid(input_tuple, max):
    return input_tuple[0] >= 0 and input_tuple[1] >= 0 and input_tuple[0] < max and input_tuple[1] < max

if __name__ == '__main__':
    grid = []
    n = int(stdin.readline())
    for x in xrange(0, n):
        line = stdin.readline()
        str_nums = line.split(' ')
        nums = [int(a) for a in str_nums]
        curr_list = []
        for y in xrange(0, n):
            curr_water_cell = WaterCell((x, y), nums[y])
            curr_list.append(curr_water_cell)
        grid.append(curr_list)

    # Fill in the links
    for x in xrange(0, n):
        for y in xrange(0, n):
            curr = grid[x][y]
            next_id = get_lowest(grid, x, y)
            if next_id != curr.id:
                curr.next = next_id

    # Partition step
    partitions = []
    for x in xrange(0, n):
        for y in xrange(0, n):
            curr_list = []
            curr = grid[x][y]

            # Already partitioned, ignore
            if curr.isPartitioned:
                continue

            # This is a basin of one
            if curr.next is None:
                curr.isPartitioned = True
                curr.group = len(partitions)
                partitions.append([curr])

            # Otherwise, we trace the water flow till we reach the bottom
            while curr.next is not None:
                curr.isPartitioned = True

                nc = curr.next
                next = grid[nc[0]][nc[1]]
                if next.isPartitioned:
                    curr.group = next.group
                    partitions[next.group].append(curr)

                    if len(curr_list) > 0:
                        for a in curr_list:
                            a.group = next.group
                        partitions[next.group] = partitions[next.group] + curr_list
                        curr_list = []
                    break
                else:
                    curr_list.append(curr)
                    curr.group = len(partitions)
                    next.isPartitioned = True
                    next.group = curr.group
                    curr_list.append(next)

                # Do the swap
                curr = next

            if len(curr_list) > 0:
                partitions.append(curr_list)

    lengths = []
    for p in partitions:
        # I seem to have duplicates in my partitions
        t = set(p) # oh well, nothing a good set op can't fix
        lengths.append(len(t))

    lengths.sort()
    lengths.reverse()
    res = " ".join(str(a) for a in lengths)
    print res
