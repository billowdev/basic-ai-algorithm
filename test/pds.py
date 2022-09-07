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

f = []
e = []
d = 0
s = 'u'
g = 'w'
count = 0

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

def progressive_deeping_search(start, goal, graph):
	return pds_q(0, [[start]], goal, [], [], graph)

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

def pds_q(depth, start, goal, frontier, explored, graph):
	print(f"\n{depth}-- PDS path--\n", start)
	if(len(start) < 1):
		return start
	elif start[0][0] == goal:
		return start[0]
	else:
		temp_graph = graph.copy()
		temp_paths = start.copy()
		p = temp_paths[0]
		x = temp_paths[0][0]
		temp_paths.pop(0)

		for node in frontier:
			if(node not in explored):
				explored.append(node)
			frontier.pop(frontier.index(node))

		if frontier == []: depth+=1
		next_frontier = get_moves(x, temp_graph)
		next_paths = extend_path(p, next_frontier, explored)
		return pds_q(depth, next_paths + temp_paths, goal, frontier, explored, temp_graph)

res = progressive_deeping_search(s, g, graph)
print(res)
