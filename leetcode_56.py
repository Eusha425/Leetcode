# 56. Merge Intervals
# not working proprely something is wrong with the approach, need to reevaluate

arr = [[1,3],[2,6],[8,10],[15,18]]

def merge(intervals):

    bs = []
    bs2 = [[]]
    bs2.pop(0)

    i = 0
    while i < len(intervals) - 1:
        if intervals[i][1] >= intervals[i+1][0]:
            bs.append(intervals[i][0])
            if intervals[i][1] > intervals[i+1][1]:

                bs.append(intervals[i][1])
            else:
                bs.append(intervals[i+1][1])
            i += 1
            bs2.append(bs)
        

        else:
            bs = []
            print(intervals[i][0])
            print(intervals[i][1])
            bs.append(intervals[i][0])
            bs.append(intervals[i][1])
            bs2.append(bs)
        i += 1

    if i == len(intervals) - 1:
        bs = []
        bs.append(intervals[i][0])
        bs.append(intervals[i][1])
        bs2.append(bs)
    return bs2



