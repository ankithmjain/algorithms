graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }

def breadth_search(graph, a, b):
    path = [a]
    queue = [path]
    while queue:
        current_path = queue.pop(0)
        node = current_path[-1]