def hIndex(citations) -> int:
    stored_h_index = 0
    max_count = 0
    for i in range(len(citations), 0, -1):
        h_index = i
        count = len(citations)
        for j in range(len(citations)):
            if citations[j] < h_index:
                count -= 1

        if count >= h_index and h_index > stored_h_index:
            stored_h_index = h_index
            max_count = count

    return min(max_count, stored_h_index)


def hIndex_alternate(citations) -> int:
    citations.sort(reverse=True)
    h = 0

    while h < len(citations) and citations[h] > h:
        h += 1

    return h


citations = [3, 0, 2, 1, 4]

print(hIndex_alternate(citations))
