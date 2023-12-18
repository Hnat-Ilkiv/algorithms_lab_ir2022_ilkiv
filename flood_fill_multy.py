import multiprocessing

def bfs(matrix, start, replace_color, rows, cols, visited):
    queue = [start]
    replace_node = matrix[start[0]][start[1]]

    while queue:
        x, y = queue.pop(0)
        if not visited[x][y]:
            visited[x][y] = True
            matrix[x][y] = replace_color

            if x > 0 and matrix[x - 1][y] == replace_node and not visited[x - 1][y]:
                queue.append((x - 1, y))
            if x < rows - 1 and matrix[x + 1][y] == replace_node and not visited[x + 1][y]:
                queue.append((x + 1, y))
            if y > 0 and matrix[x][y - 1] == replace_node and not visited[x][y - 1]:
                queue.append((x, y - 1))
            if y < cols - 1 and matrix[x][y + 1] == replace_node and not visited[x][y + 1]:
                queue.append((x, y + 1))

def flood_fill(matrix, start, replace_color, rows, cols):
    x, y = start
    if matrix[x][y] != replace_color:
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        bfs(matrix, start, replace_color, rows, cols, visited)

def read_input(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        height, width = map(int, lines[0].strip().split(","))
        start = tuple(map(int, lines[1].strip().split(",")))
        replace_color = lines[2].strip().strip("‘’")
        matrix = [list(row.strip("\n[]', ").split("', '")) for row in lines[3:]]

        return height, width, start, replace_color, matrix

def write_output(file_path, matrix):
    with open(file_path, "w") as f:
        for row in matrix:
            f.write("['" + "', '".join(row) + "']\n")

if __name__ == '__main__':
    import time

    input_file = "big_input.txt"
    output_file = "output.txt"

    print(f"Start reading & saveing matrix and other data ...")
    start_time = time.time()
    height, width, start, replace_color, matrix = read_input(input_file)
    end_time = time.time()
    print(f"Time: {end_time - start_time}\nFinish reading & saveing matrix and other data ...\n")

    print(f"Start working ...")
    start_time = time.time()
    processes = []
    for i in range(multiprocessing.cpu_count()):
        p = multiprocessing.Process(target=flood_fill, args=(matrix, start, replace_color, height, width))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()
    end_time = time.time()
    print(f"Time: {end_time - start_time}\nFinish working ... \n")

    print(f"Start writeing ...")
    start_time = time.time()
    write_output(output_file, matrix)
    end_time = time.time()
    print(f"Time: {end_time - start_time}\nFinish writeing ...\n")
