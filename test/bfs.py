graph = [
    ['u', '-->', 'x'],
    ['u', '-->', 'y'],
    ['u', '-->', 'z'],
    ['x', '-->', 'y'],
    ['x', '-->', 'r'],
    ['y', '-->', 'r'],
    ['y', '-->', 't'],
    ['z', '-->', 'y'],
    ['z', '-->', 't'],
    ['r', '-->', 'w'],
    ['r', '-->', 's'],
    ['s', '-->', 'w'],
    ['t', '-->', 's'],
    ['t', '-->', 'w'],
]


def breadth_first_search_noncycles(startState, goalState):
    return bfs_q([[startState]], goalState, graph, explored=[startState])


def get_moves(start_state, graph):
    if graph == []:
        return []
    else:
        temp_graph = graph.copy()
        current_path = temp_graph.pop(0)
        current_path = current_path.copy()
        if current_path.pop(0) == start_state:
            return [current_path.pop(1)] + get_moves(start_state, temp_graph)
        else:
            return get_moves(start_state, temp_graph)


def extend_path(path, next_state, explored):
    if(len(next_state) < 1):
        return []
    elif next_state[0] in path:
        next_state.pop(0)
        return extend_path(path, next_state, explored)
    elif next_state[0] in explored:
        next_state.pop(0)
        return extend_path(path, next_state, explored)
    else:
        el = next_state.pop(0)
        explored.append(el)
        return [[el]+path] + extend_path(path, next_state, explored)

def bfs_q(paths, goal_state, graph, explored):
    global count
    count += 1
    print("\n {} breadth first search \n path--> {}\n".format(count, paths))
    if len(paths) < 1:
        return paths
    elif paths[0][0] == goal_state:
        return paths[0]
    else:
        copy_graph = graph.copy()
        temp_paths = paths.copy()
        current_path = temp_paths[0]
        present_node = temp_paths[0][0]
        temp_paths.pop(0)
        next_state = get_moves(present_node, copy_graph)
        next_paths = extend_path(current_path, next_state, explored)
        return bfs_q(temp_paths + next_paths, goal_state, copy_graph, explored)


count = 0
bfs = breadth_first_search_noncycles('u', 'w')
print("\n=== bfs result === \n path: {}".format(bfs))

