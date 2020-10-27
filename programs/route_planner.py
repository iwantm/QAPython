def convert(string):
    li = list(string.split(" "))
    return li


def router(set):
    points = convert(set)
    path = []

    for point in range(len(points)-1):
        if points[point] < points[point+1]:

            path.append(points[point+1])
    print(path)


router('0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15')
