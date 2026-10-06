# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem?isFullScreen=false


def getNext(head, tail):
    return [head[0] + 1, head[1] + 1], [tail[0] - 1, tail[1] - 1]


def matrixRotation(matrix, R):
    rotated_matrix = [row[:] for row in matrix]

    head = [0, 0]
    tail = [len(matrix) - 1, len(matrix[0]) - 1]
    while head[0] < tail[0] and head[1] < tail[1]:
        matrixRotationLayer(matrix, R, head, tail, rotated_matrix)
        head, tail = getNext(head, tail)

    return rotated_matrix


def matrixRotationLayer(matrix, R, head, tail, rotated_matrix):
    r1, c1, r2, c2 = head[0], head[1], tail[0], tail[1]

    original_index = []
    for c in range(c1, c2):
        original_index.append([r1, c])
    for r in range(r1, r2):
        original_index.append([r, c2])
    for c in range(c2, c1, -1):
        original_index.append([r2, c])
    for r in range(r2, r1, -1):
        original_index.append([r, c1])

    rotated_index = (
        original_index[R % len(original_index) :]
        + original_index[: R % len(original_index)]
    )

    index_map = dict(
        zip([tuple(x) for x in original_index], [tuple(x) for x in rotated_index])
    )

    # print("head:", head, " tail:", tail)
    # print("original_index:", original_index)
    # print("rotated_index:", rotated_index)
    # print()

    for (i, j), (ni, nj) in index_map.items():
        rotated_matrix[i][j] = matrix[ni][nj]


def printMatrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    first_multiple_input = input().rstrip().split()
    m = int(first_multiple_input[0])
    n = int(first_multiple_input[1])
    r = int(first_multiple_input[2])
    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    rotated_matrix = matrixRotation(matrix, r)
    printMatrix(rotated_matrix)
