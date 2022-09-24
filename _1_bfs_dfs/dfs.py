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

def depth_first_search_noncycles(start_state, goal_state):
    return dfs_q([[start_state]], goal_state, graph, explored=[start_state])

def get_moves(start_state, g_list):
    if(g_list == []):
        return []
    else:
        temp_graph = g_list.copy()
        path = temp_graph.pop(0)
        copy_path = path.copy()
        if(copy_path.pop(0) == start_state):
            return [copy_path.pop(1)] + get_moves(start_state, temp_graph)
        else:
            return get_moves(start_state, temp_graph)

def extend_path(path, next_state, explored):
	if(len(next_state)<1): 
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

def dfs_q(paths, goal_state, graph, explored):
    global count
    count += 1
    print("\n {} depth first search \n path --> {} \n".format(count, paths))

    if len(paths) < 1:
        return paths
    elif paths[0][0] == goal_state:
        return paths[0]
    else:
        temp_graph = graph.copy()
        temp_paths = paths.copy()
        current_path = temp_paths[0]
        present_node = temp_paths[0][0]

        next_state = get_moves(present_node, temp_graph)
        next_paths = extend_path(current_path, next_state, explored)
        return dfs_q(next_paths + temp_paths, goal_state, temp_graph, explored)

count = 0
dfs = depth_first_search_noncycles('u', 'w')
print("\n=== result === \n path: {} \n ".format(dfs))
