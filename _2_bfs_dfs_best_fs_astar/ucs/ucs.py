import graphlib


graph = [
        ['S','-->','p', 1],
         ['S','-->','d', 3],
         ['S','-->','e', 9],
         ['p','-->','q', 15],
         ['d','-->','b', 1],
         ['d','-->','c', 8],
         ['e','-->','h', 1],
         ['e','-->','r', 9],
         ['q','-->','r', 3],
         ['b','-->','a', 2],
         ['c','-->','a', 2],
         ['h','-->','q', 4],
         ['h','-->','p', 4],
         ['r','-->','f', 5],
         ['f','-->','G', 5],
         ['f','-->','c', 2],
         ]


def get_moves(state, lst):
    lstTemp = lst.copy()
    if len(lstTemp) < 1:
        return []
    elif lstTemp[0][0] == state:
        x = lstTemp[0].copy()
        r = [x[2], x[3]]
        lstTemp.pop(0)
        return [r] + get_moves(state, lstTemp)
    else:
        lstTemp.pop(0)
        return get_moves(state, lstTemp)


def extend_all(path, nextStates, V):
    if len(nextStates) < 1:
        return []
    elif nextStates[0][0] in path:
        nextStates.pop(0)
        return extend_all(path, nextStates, V)
    elif nextStates[0][0] in V:
        nextStates.pop(0)
        return extend_all(path, nextStates, V)
    else:
        X = nextStates.pop(0)
        state = X[0]
        cost = X[1]
        pathX = path.copy()
        pathX[0] = pathX[0] + cost
        pathX.insert(1, state)
        return [pathX] + extend_all(path, nextStates, V)


def UniformCost_Expanded(paths, goalState, moveList, V):
    print(f'{paths} | {V}')
    if len(paths) < 1:
        return []
    elif paths[0][1] == goalState:
        return paths[0]
    else:
        path = paths[0].copy()
    if path[1] not in V:
        V.append(path[1])
        move = get_moves(path[1], moveList)
        tempPaths = paths.copy()
        tempPaths.pop(0)
        tempPaths = tempPaths + extend_all(path, move, V)
        tempPaths.sort()
        return UniformCost_Expanded(tempPaths, goalState, moveList, V)


def UniformCost(paths, goalState, moveList):
	print(paths)
	if len(paths) < 1:
		return []
	elif paths[0][1] == goalState:
		return paths[0]
	else:
		path = paths[0].copy()
		move = get_moves(path[1], moveList)
		tempPaths = paths.copy()
		tempPaths.pop(0)
		tempPaths = tempPaths + extend_all(path, move)
		tempPaths.sort()
		return UniformCost(tempPaths, goalState, moveList)

UniformCost(['S'], 'G', graph)