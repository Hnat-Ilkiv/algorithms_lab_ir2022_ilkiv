import random

def generate_random_matrix(height, width):
    possible_values = ['Y', 'G', 'W', 'R', 'B', 'X']
    possible_values = ['X']
    matrix = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(random.choice(possible_values))
        matrix.append(row)
    return matrix

def write_output(file_path, height, width, value, matrix):
    with open(file_path, "w") as f:
        f.write(f"{height},{width}\n")
        f.write(f"{int(height/2)},{int(width/2)}\n")
        f.write(f"‘{value}’\n")
        for row in matrix[:-1]:
            f.write("['" + "', '".join(row) + "'],\n")
        f.write("['" + "', '".join(matrix[-1]) + "']\n")

if __name__ == "__main__":
    import time

    output_file = "big_input.txt"
    height = 4_000
    width = 4_000
    value = "C"

    print(f"Start generateing matrix {height}x{width} ...")
    start_time = time.time()
    result_matrix = generate_random_matrix(height, width)
    end_time = time.time()
    print(f"Time: {end_time - start_time}\nFinish generateing matrix {height}x{width} ...\n")

    print(f"Start writeing matrix {height}x{width} ...")
    start_time = time.time()
    write_output(output_file, height, width, value, result_matrix)
    end_time = time.time()
    print(f"Time: {end_time - start_time}\nFinish writeing matrix {height}x{width} ...\n")
