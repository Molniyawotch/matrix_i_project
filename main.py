# matrix
matrix = [
    [1, 3, 5, 7, 8, 2, 6, 2, 5, 3],
    [4, 6, 2, 5, 3, 6, 3, 5, 3, 8],
    [1, 3, 5, 7, 8, 2, 6, 2, 5, 3],
    [4, 6, 2, 5, 3, 6, 3, 5, 3, 8],
    [1, 3, 5, 7, 8, 2, 6, 2, 5, 3],
    [4, 6, 2, 5, 3, 6, 3, 5, 3, 8],
    [1, 3, 5, 7, 8, 2, 6, 2, 5, 3],
    [4, 6, 2, 5, 3, 6, 3, 5, 3, 8],
    [1, 3, 5, 7, 8, 2, 6, 2, 5, 3],
    [4, 6, 2, 5, 3, 6, 3, 5, 3, 8]
]


# functions


def sum_of_numbers(matrix: list[list[int]]):
    _sum = 0
    _max = _min = matrix[0][0]
    mode = [0, 0]
    frequencies = {}
    for i in matrix:
        for j in i:
            _sum += j
            if _max < j:
                _max = j
            if _min > j:
                _min = j
            if j in frequencies:
                frequencies[j] += 1
            else:
                frequencies[j] = 1
            if mode[1] < frequencies[j]:
                mode[0] = j
                mode[1] = frequencies[j]
    else:
        return {"sum": _sum, "max": _max, "min": _min, "mode": mode}


if __name__ == '__main__':
    a = sum_of_numbers(matrix)
    print(a)
