# matrix
matrix = [
    1, 3, 5, 7, 8, 2, 6, 2, 5, 3,
    4, 6, 2, 5, 3, 6, 3, 5, 3, 8,
    1, 3, 5, 7, 8, 2, 6, 2, 5, 3,
    4, 6, 2, 5, 3, 6, 3, 5, 3, 8,
    1, 3, 5, 7, 8, 2, 6, 2, 5, 3,
    4, 6, 2, 5, 3, 6, 3, 5, 3, 8,
    1, 3, 5, 7, 8, 2, 6, 2, 5, 3,
    4, 6, 2, 5, 3, 6, 3, 5, 3, 8,
    1, 3, 5, 7, 8, 2, 6, 2, 5, 3,
    4, 6, 2, 5, 3, 6, 3, 5, 3, 8
]


# functions


def sum_of_numbers():
    a = 0
    i = 0
    while i < 100:
        a += matrix[i]
        i += 1
    else:
        print(a)


def biggest_number():
    a = 0
    i = 0
    while i < 100:
        if a < matrix[i]:
            a = matrix[i]
        i += 1
    else:
        print(a)


def smallest_number():
    a = 100
    i = 0
    while i < 100:
        if a > matrix[i]:
            a = matrix[i]
        i += 1
    else:
        print(a)


sum_of_numbers()
biggest_number()
smallest_number()
