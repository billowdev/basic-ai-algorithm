graph = [
         ['u','-->','x'],
         ['u','-->','y'],
         ['u','-->','z'],
         ['x','-->','y'],
         ['x','-->','r'],
         ['y','-->','r'],
         ['y','-->','t'],
         ['z','-->','y'],
         ['z','-->','t'],
         ['r','-->','w'],
         ['r','-->','s'],
         ['s','-->','w'],
         ['t','-->','s'],
         ['t','-->','w'],  
]

def get_moves(start_state, g_list):
	if(g_list == []): return []
	else:
		temp_graph = g_list.copy()
		path = temp_graph.pop(0)
		copy_path = path.copy()
		if(copy_path.pop(0) == start_state):
			return [copy_path.pop(1)] + get_moves(start_state, temp_graph)
		else:
			return get_moves(start_state, temp_graph)

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
		
		return pds_q(next_paths + temp_paths, goal, frontier, explored, temp_graph)

depth=0
pds = pds_q('u', 'w', graph)