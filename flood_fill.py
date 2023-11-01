def flood_fill(matrix_height, matrix_width, matrix, start, target_color, replace_color):
    height = len(matrix)
    width = len(matrix[0])

    if (matrix_height != height or matrix_width != width):
        print(height, width)
        print(matrix_height, matrix_width)
        print (f"Height && Width Error")
        return matrix

    stack = [start]

    while stack:
        x, y = stack.pop()
        if 0 <= x < height and 0 <= y < width and matrix[x][y] == target_color:
            matrix[x][y] = replace_color
            stack.append((x + 1, y))
            stack.append((x - 1, y))
            stack.append((x, y + 1))
            stack.append((x, y - 1))

def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        height, width = map(int, lines[0].strip().split(','))
        start = tuple(map(int, lines[1].strip().split(',')))
        target_color = lines[2].strip().strip('‘’')
        matrix = [list(row.strip().strip('[\'\'],').split('\', \'')) for row in lines[3:]]
        return (height, width, start, target_color, matrix)

def write_output(file_path, matrix):
    with open(file_path, 'w') as f:
        for row in matrix:
            f.write('[\'' + '\', \''.join(row) + '\']\n')

if __name__ == '__main__':
    input_file = 'input.txt'
    output_file = 'output.txt'

    data = read_input(input_file)
    height, width, start, target_color, matrix = data

    replace_color = 'C'  # Вказуємо колір для заміни

    # print(height, width)
    # print(start)
    # print(target_color, "=>", replace_color)
    # for i in matrix:
    #     print(i)

    flood_fill(height, width, matrix, start, target_color, replace_color)

    # print()
    # for i in matrix:
    #     print(i)

    write_output(output_file, matrix)
