from queue import PriorityQueue  # essentially a binary heap


def dijkstra(G, start, goal):
    """ Uniform-cost search / dijkstra """
    visited = set()
    cost = {start: 0}
    parent = {start: None}
    todo = PriorityQueue()

    todo.put((0, start))
    while todo:
        while not todo.empty():
            _, vertex = todo.get()  # finds lowest cost vertex
            # loop until we get a fresh vertex
            if vertex not in visited: break
        else:   
            break  # quit main loop
        visited.add(vertex)
        if vertex == goal:
            break
        for neighbor, distance in G[vertex]:
            if neighbor in visited: continue  # skip these to save time
            old_cost = cost.get(neighbor, float('inf'))  # default to infinity
            new_cost = cost[vertex] + distance
            if new_cost < old_cost:
                todo.put((new_cost, neighbor))
                cost[neighbor] = new_cost
                parent[neighbor] = vertex

    return parent


def make_path(parent, goal):
    if goal not in parent:
        return None
    v = goal
    path = []
    while v is not None:  # root has null parent
        path.append(v)
        v = parent[v]
    return path[::-1]


## Example

G = {  # random example graph
    'A': {('C', 76)},
    'B': {('C', 20), ('J', 78)},
    'C': {('C', 62), ('F', 99), ('G', 72), ('H', 40)},
    'D': {('A', 8), ('G', 71), ('I', 61)},
    'E': {('C', 16), ('E', 54), ('I', 3)},
    'F': {('J', 66)},
    'G': {('B', 92), ('E', 48), ('G', 31)},
    'H': {('G', 36)},
    'I': {('J', 88), ('K', 16)},
    'J': {('H', 4), ('K', 46)},
    'K': {('I', 40)}
}

parent = dijkstra(G, 'A', 'K')
print(make_path(parent, 'K'))
