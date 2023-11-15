"""
=======================================================================
=                     Flood fill application                          =
=======================================================================
"""

def bfs(graph, start, replace_color):
    visited = set()
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            graph[vertex][0] = replace_color
            for neighbor in graph[vertex][1]:
                if neighbor not in visited:
                    queue.append(neighbor)

def flood_fill(graph, start , replace_color):
    if graph[start][0] != replace_color:
        bfs(graph, start, replace_color)


def read_input(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        height, width = map(int, lines[0].strip().split(","))
        start = tuple(map(int, lines[1].strip().split(",")))
        replace_color = lines[2].strip().strip("‘’")
        matrix = [list(row.strip("\n[]', ").split("', '")) for row in lines[3:]]
        # Transformation into a graph
        graph = {}
        rows = height
        cols = width

        for i in range(rows):
            for j in range(cols):
                node = (i, j)
                value = matrix[i][j]
                neighbors = []
                current_node = matrix[i][j]

                if i > 0 and matrix[i - 1][j] == current_node:
                    neighbors.append((i - 1, j))
                if i < rows - 1 and matrix[i + 1][j] == current_node:
                    neighbors.append((i + 1, j))
                if j > 0 and matrix[i][j - 1] == current_node:
                    neighbors.append((i, j - 1))
                if j < cols - 1 and matrix[i][j + 1] == current_node:
                    neighbors.append((i, j + 1))

                graph[node] = [value, neighbors]

        return (height, width, start, replace_color, graph)

def write_output(file_path, graph, height, width):
    with open(file_path, "w") as f:
        matrix = []
        for i in range(height):
            line = []
            for j in range(width):
                line.append(graph[(i, j)][0])
            matrix.append(line)

        for row in matrix:
            f.write("['" + "', '".join(row) + "']\n")

if __name__ == "__main__":
    import time

    input_file = "big_input.txt"
    output_file = "output.txt"

    print(f"Start reading ...")
    start_time = time.time()
    data = read_input(input_file)
    end_time = time.time()
    print(f"Time: {end_time - start_time}\nFinish reading ...\n")

    print(f"Start saveing graph and other data ...")
    start_time = time.time()
    height, width, start, replace_color, graph = data
    end_time = time.time()
    print(f"Time: {end_time - start_time}\nFinish saveing graph and other data ...\n")

    print(f"Start working ...")
    start_time = time.time()
    flood_fill(graph, start, replace_color)
    end_time = time.time()
    print(f"Time: {end_time - start_time}\nFinish working ... \n")

    print(f"Start writeing ...")
    start_time = time.time()
    write_output(output_file, graph, height, width)
    end_time = time.time()
    print(f"Time: {end_time - start_time}\nFinish writeing ...\n")
