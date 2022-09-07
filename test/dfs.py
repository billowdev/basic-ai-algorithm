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


def DFS_noncycles(startState, goalState):
    return DFS_Q([[startState]], goalState, graph, V=[startState])


def GetMoves(sState, lst):
    if lst == []:
        return []
    else:
        templst = lst.copy()
        x = templst.pop(0)
        tempx = x.copy()
        if tempx.pop(0) == sState:
            return [tempx.pop(1)] + GetMoves(sState, templst)
        else:
            return GetMoves(sState, templst)


def extend_all_DFS(path, nextStates, V):
    if len(nextStates) < 1:
        return []
    elif nextStates[0] in path:
        nextStates.pop(0)
        return extend_all_DFS(path, nextStates, V)
    elif nextStates[0] in V:
        nextStates.pop(0)
        return extend_all_DFS(path, nextStates, V)
    else:
        x = nextStates.pop(0)
        V.append(x)
        return [[x]+path] + extend_all_DFS(path, nextStates, V)


count = 0


def DFS_Q(paths, goalState, lst, V):
    global count
    count += 1
    print(f"\n{count}--DFS path--\n", paths)

    if len(paths) < 1:
        return paths
    elif paths[0][0] == goalState:
        return paths[0]
    else:
        lstTemp = lst.copy()
        tempPaths = paths.copy()
        p = tempPaths[0]
        x = tempPaths[0][0]
        tempPaths.pop(0)
        moves = GetMoves(x, lstTemp)
        #print("-p-", p)
        #print("-moves-", moves)
        print("-V-", V)
        nextPaths = extend_all_DFS(p, moves, V)
        return DFS_Q(nextPaths + tempPaths, goalState, lstTemp, V)


res = DFS_noncycles('u', 'w')
print(f"\n{count+1}--DFS result--\n", res)
