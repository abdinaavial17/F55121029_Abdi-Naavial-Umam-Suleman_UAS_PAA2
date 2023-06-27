import sys
import time

# Definisikan graf
graph = {
    'A': {'B': 12, 'C': 10, 'G': 12},
    'B': {'A': 12, 'C': 8, 'D': 12},
    'C': {'A': 10, 'B': 8, 'D': 11, 'E': 3, 'G': 9},
    'D': {'B': 12, 'C': 11, 'E': 11, 'F': 10},
    'E': {'C': 3, 'D': 11, 'F': 6, 'G': 7},
    'F': {'D': 10, 'E': 6, 'G': 9},
    'G': {'A': 12, 'C': 9, 'E': 7, 'F': 9}
}


def tsp(graph, start):
    n = len(graph)
    visited = [False] * n
    path = []
    min_dist = sys.maxsize
    start_time = time.time()

    def backtrack(curr_vertex, curr_path, curr_dist):
        nonlocal min_dist

        if len(curr_path) == n:
            if graph[curr_vertex].get(start):
                curr_dist += graph[curr_vertex][start]
                if curr_dist < min_dist:
                    min_dist = curr_dist
                    path.extend(curr_path + [curr_vertex, start])
            return

        for neighbor, distance in graph[curr_vertex].items():
            if not visited[ord(neighbor) - ord('A')]:
                visited[ord(neighbor) - ord('A')] = True
                backtrack(neighbor, curr_path + [curr_vertex], curr_dist + distance)
                visited[ord(neighbor) - ord('A')] = False

    visited[ord(start) - ord('A')] = True
    backtrack(start, [], 0)

    end_time = time.time()
    execution_time = end_time - start_time

    return path, min_dist, execution_time


def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    shortest_path = {start: []}
    unvisited = graph.copy()
    start_time = time.time()

    while unvisited:
        min_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        for neighbor, distance in graph[min_vertex].items():
            if neighbor in unvisited:
                new_distance = distances[min_vertex] + distance
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    shortest_path[neighbor] = shortest_path[min_vertex] + [min_vertex]

        unvisited.pop(min_vertex)

    end_time = time.time()
    execution_time = end_time - start_time

    return shortest_path, distances, execution_time


def print_iteration_results(iterations):
    print("Path iterations: ", iterations)


def print_execution_time(execution_time):
    print("Execution Time: %.6f seconds" % execution_time)


def print_shortest_path(path, distance):
    print("Shortest Path: ", ' -> '.join(path))
    print("Shortest Distance: ", distance)


def analyze_algorithm():
    print("Analysis Algorithm:")
    print("1. Worst Case:")
    print("   - TSP: O(n!)")
    print("   - Dijkstra: O((V + E)logV)")
    print("2. Best Case:")
    print("   - TSP: O(n!)")
    print("   - Dijkstra: O((V + E)logV)")
    print("3. Average Case:")
    print("   - TSP: O(n!)")
    print("   - Dijkstra: O((V + E)logV)")


def main():
    print("Welcome to Shortest Path Program!")
    print("1. TSP (Traveling Salesman Problem)")
    print("2. Dijkstra")
    print("3. Analysis Algorithm")
    choice = input("Enter your choice (1-3): ")
    print()

    if choice == '1':
        start_vertex = input("Enter the start vertex: ")
        path, distance, execution_time = tsp(graph, start_vertex)
        print_iteration_results(path)
        print_execution_time(execution_time)
        print_shortest_path(path, distance)
    elif choice == '2':
        start_vertex = input("Enter the start vertex: ")
        shortest_path, distances, execution_time = dijkstra(graph, start_vertex)
        print_iteration_results(shortest_path)
        print_execution_time(execution_time)
        for vertex in shortest_path:
            if vertex != start_vertex:
                path = shortest_path[vertex] + [vertex]
                distance = distances[vertex]
                print_shortest_path(path, distance)
    elif choice == '3':
        analyze_algorithm()
    else:
        print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()