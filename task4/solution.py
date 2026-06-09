def solution():
    data = open(0).read().split()
    if not data:
        return
    n, m = int(data[0]), int(data[1])
    matrix = data[2:2 + n]

    double = [row + row for row in matrix]

    min_row = '1' * m
    for row in matrix:
        d_row = row + row
        for i in range(m):
            sub = d_row[i:i+m]
            if sub < min_row:
                min_row = sub

    best_top = None
    best_matrix = None  

    for top in range(n):
        first_row_double = double[top]
        for left in range(m):
            if first_row_double[left:left+m] != min_row:
                continue
            cur_matrix = tuple(double[(top + i) % n][left:left+m] for i in range(n))
            
            if best_matrix is None:
                best_matrix = cur_matrix
                continue

            if cur_matrix < best_matrix:
                best_matrix = cur_matrix


    for row in best_matrix:
        print(row)

if __name__ == "__main__":
    solution()
