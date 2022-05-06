""" Earthquakes Magnitude Counts Module"""

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

def magCounts(eventMagnitude):
    # *** counts earthquake numbers in every mag range ***
    # ---transfer object format to int format---
    mag_list = [int(float(i)) for i in eventMagnitude]  # 将所有震级取整
    counts_num = get_counts(mag_list)
    if not (1 in counts_num.keys()):
        counts_num[1] = 0
    if not (2 in counts_num.keys()):
        counts_num[2] = 0
    if not (3 in counts_num.keys()):
        counts_num[3] = 0
    if not (4 in counts_num.keys()):
        counts_num[4] = 0
    if not (5 in counts_num.keys()):
        counts_num[5] = 0
    if not (6 in counts_num.keys()):
        counts_num[6] = 0
    if not (7 in counts_num.keys()):
        counts_num[7] = 0
    if not (8 in counts_num.keys()):
        counts_num[8] = 0
    return counts_num