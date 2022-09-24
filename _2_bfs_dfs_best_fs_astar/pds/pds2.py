graph = [
    ['S', '-->', 'p'],
    ['S', '-->', 'd'],
    ['S', '-->', 'e'],
    ['p', '-->', 'q'],
    ['d', '-->', 'b'],
    ['d', '-->', 'c'],
    ['e', '-->', 'h'],
    ['e', '-->', 'r'],
    ['q', '-->', 'r'],
    ['b', '-->', 'a'],
    ['c', '-->', 'a'],
    ['h', '-->', 'q'],
    ['h', '-->', 'p'],
    ['r', '-->', 'f'],
    ['f', '-->', 'G'],
    ['f', '-->', 'c'],
]


def get_moves(start_state, g_list):
	if(g_list == []): return []
	else:
		temp_graph = g_list.copy()
		path = temp_graph.pop(0)
		
		copy_path = path.copy()
		if(copy_path.pop(0) == start_state):
			n=copy_path.pop(1)
			#rint('move',n)
			return [n] + get_moves(start_state, temp_graph)
		else:
			return get_moves(start_state, temp_graph)

def progressive_deeping_search(start, goal, graph):
	res = pds_q([[start]], goal, [], [], graph)
	return res

def extend_path(path, next_frontier, explored):
	if(len(next_frontier)<1): 
		return []
	elif next_frontier[0] in path:
		next_frontier.pop(0)
		return extend_path(path, next_frontier, explored)
	elif next_frontier[0] in explored:
		next_frontier.pop(0)
		return extend_path(path, next_frontier, explored)
	else:
		el = next_frontier.pop(0)
		explored.append(el)
		return [[el]+path] + extend_path(path, next_frontier, explored)

def pds_q(paths, goal, frontier, explored, graph):
	global depth
	print("\n progressive deeping search \n path--> {} \n depth = {}\n".format(paths, depth))
	current_node = paths[0][0]
	if(len(paths) < 1):
		return paths
	elif current_node == goal:
		return paths[0]
	else:
		temp_graph, temp_paths = graph.copy(), paths.copy()
		current_path, present_node = temp_paths[0], temp_paths[0][0]

		for node in frontier:
			if(node not in explored):
				explored.append(node)
			frontier.pop(frontier.index(node))

		if frontier == []: depth+=1

		next_frontier = get_moves(present_node, temp_graph)
		next_paths = extend_path(current_path, next_frontier, explored)
		
		return pds_q(next_paths + temp_paths, goal, frontier, explored, temp_graph)

depth=0
pds = progressive_deeping_search('S', 'G', graph)

print("\n=== result === \n path: {} \n depth = {}".format(pds, depth))
