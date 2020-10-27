def tt():
    table = []

    for i in range(1, 11):
        row = []
        for j in range(1, 11):
            row.append(i*j)
        table.append(row)
    return table


def print_table(table):
    for row in table:
        print(*row, sep=" ")
