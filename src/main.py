"""
Module Description: Gas Transport Algorithm

This module provides functions for analyzing gas transport connectivity
between gas storage locations and cities using active pipelines.

Author: Hnat Ilkiv
Date: 2023-11-16
"""


def bfs(
    first_gas_storage: str, gas_storage: list[str], pipelines: list[str]
) -> list[str]:
    """
    Perform Breadth-First Search (BFS) to find reachable locations from a given gas storage.

    Args:
        first_gas_storage (str): The starting gas storage.
        gas_storage (list): List of gas storage locations.
        pipelines (list): List of active pipelines.

    Returns:
        list: List of reachable locations.
    """
    queue = [first_gas_storage]
    visited = []

    while queue:
        current_note = queue.pop(0)
        if current_note not in visited:
            visited.append(current_note)

            for connection in pipelines:
                if (
                    connection[0] == current_note
                    and connection[1] not in gas_storage
                ):
                    queue.append(connection[1])

    visited.pop(0)
    return visited


def find_unreachable(
    city: list[str], gas_storage: list[str], pipelines: list[str]
) -> list[str, list[str]]:
    """
    Find gas storage locations and the corresponding unreachable cities.

    Args:
        city (list): List of cities.
        gas_storage (list): List of gas storage locations.
        pipelines (list): List of active pipelines.

    Returns:
        list: List of unreachable locations and their corresponding cities.
    """
    unreachable = []

    for storage in gas_storage:
        available = bfs(storage, gas_storage, pipelines)
        unavailable = [
            element for element in city if element not in available
        ]

        if unavailable:
            unreachable.append([storage, unavailable])

    return unreachable
