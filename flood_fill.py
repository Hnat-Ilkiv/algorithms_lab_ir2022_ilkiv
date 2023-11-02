"""
=======================================================================
=                     Flood fill application                          =
=======================================================================
"""

import time

def flood_fill(matrix_height, matrix_width, matrix, start, target_color, replace_color):
    height = len(matrix)
    width = len(matrix[0])

    if matrix_height != height or matrix_width != width:
        raise ValueError("The height or width is incorrect")

    if start[0] < 0 or start[0] > height or start[1] < 0 or start[1] > width:
        raise IndexError("The coordinates of the initial node are outside the array")

    if matrix[start[0]][start[1]] != target_color:
        raise ValueError("The original color is not correct")

    if target_color == replace_color:
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
    with open(file_path, "r") as f:
        lines = f.readlines()
        height, width = map(int, lines[0].strip().split(","))
        start = tuple(map(int, lines[1].strip().split(",")))
        target_color = lines[2].strip().strip("‘’")
        matrix = [list(row.strip("\n[]', ").split("', '")) for row in lines[3:]]
        return (height, width, start, target_color, matrix)

def write_output(file_path, matrix):
    with open(file_path, "w") as f:
        for row in matrix:
            f.write("['" + "', '".join(row) + "']\n")

if __name__ == "__main__":
    print(__doc__)

    question = input("Show you an example [Y/n]: ")
    do_example = True if question == "Y" or question == "y" or question == "YES" or question == "yes" or question == "" else False

    if do_example:
        input_file = "input.txt"
        output_file = "output.txt"
    else:
        input_file = input("Specify the name of the input file: ") # "input.txt"
        output_file = input("Specify the name of the output file: ") # "output.txt"

        if input_file == "":
            input_file = "input.txt"

        if output_file == "":
            output_file = "output.txt"

    data = read_input(input_file)
    height, width, start, target_color, matrix = data

    read_file = (f"Height: {height}\tWidth: {width}\nStart coordinates: {start}\nTarget color: {target_color}\n")
    print("\nReading a file:")
    for i in read_file:
        time.sleep(0.01)
        print(i, end="")
    time.sleep(0.2)
    print("Initial matrix:")
    for i in matrix:
        time.sleep(0.2)
        print(" ".join(i))

    print()
    replace_color = input(f"What color do you want to replace {target_color} with:")  # Вказуємо колір для заміни
    if replace_color == "":
        replace_color = "C"

    print(f"The colors are being changed from {target_color} to {replace_color}...")

    flood_fill(height, width, matrix, start, target_color, replace_color)

    print("Processing . . . ")

    time.sleep(2)

    print("\nThe resulting matrix:")
    for i in matrix:
        time.sleep(0.2)
        print(" ".join(i))

    write_output(output_file, matrix)
