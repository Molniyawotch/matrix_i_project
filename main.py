# task 1
# matrix
matrix = [
    [15, 2, 7, 8, 9, 10, 3, 5, 14, 11],
    [6, 12, 18, 4, 3, 9, 17, 11, 6, 2],
    [13, 5, 8, 9, 1, 20, 6, 17, 3, 14],
    [7, 11, 4, 16, 10, 9, 2, 14, 8, 6],
    [5, 3, 1, 6, 12, 7, 19, 8, 14, 15],
    [9, 13, 11, 15, 5, 7, 2, 6, 3, 10],
    [2, 7, 13, 10, 9, 8, 5, 4, 12, 1],
    [6, 17, 9, 4, 3, 12, 14, 5, 8, 20],
    [16, 5, 11, 13, 3, 9, 6, 8, 10, 1],
    [4, 18, 7, 9, 13, 11, 2, 3, 6, 8]
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


# task 2
serials_db = [{"title": "Chronicles of the Galaxy", "genre": "adventure", "seasons": 5, "rating": 8},
              {"title": "Mystery Island", "genre": "fantasy", "seasons": 3, "rating": 9},
              {"title": "Epic Quest", "genre": "fantasy", "seasons": 4, "rating": 7},
              {"title": "Crime Files", "genre": "crime drama", "seasons": 6, "rating": 5},
              {"title": "Medical Miracles", "genre": "medical drama", "seasons": 2, "rating": 8},
              {"title": "Time Travelers", "genre": "adventure", "seasons": 4, "rating": 8},
              {"title": "Comedy Central", "genre": "comedy", "seasons": 7, "rating": 9}]


def find_by_genre(genre: str):
    search = []
    for serial in serials_db:
        if serial["genre"] == genre:
            search.append(serial)
    return search


def find_by_rating(rating: int):
    search = []
    for serial in serials_db:
        if serial["rating"] == rating:
            search.append(serial)
    return search


def display_info(shows):
    for show in shows:
        print(show["title"])
        print(f'Genre - {show["genre"]}')
        print(f'Seasons - {show["seasons"]}')
        print(f'Rating - {show["rating"]}')
        print("=======================")


if __name__ == '__main__':
    # a = sum_of_numbers(matrix)
    # print(a)
    variant = int(input("1 - поиск по жанру, 2 - поиск по рейтингу\n"))
    if variant == 1:
        chose = input("Жанр: ").lower()
        b = find_by_genre(chose)
    if variant == 2:
        chose = int(input("Рейтинг: ").lower())
        b = find_by_rating(chose)

    display_info(b)
