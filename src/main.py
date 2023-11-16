def bfs(city, first_gas_storage, gas_storage, pipelines):
    queue = [first_gas_storage]
    visited = []

    while queue:
        current_note = queue.pop(0)
        if current_note not in visited:
            visited.append(current_note)

            for connection in pipelines:
                if connection[0] == current_note and connection[1] not in gas_storage:
                    queue.append(connection[1])

    visited.pop(0)
    return visited




def find_unreachable(city, gas_storage, pipelines):
    unreachable = []

    for storage in gas_storage:
        available = bfs(city, storage, gas_storage, pipelines)
        unavailable = [element for element in city if element not in available]

        if unavailable:
            unreachable.append([storage, unavailable])

    return unreachable
