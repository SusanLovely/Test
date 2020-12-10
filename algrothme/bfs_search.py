def bsf(graph, start):
    quene = []
    visited = set()
    quene.append(start)
    visited.add(start)
    while len(quene) > 0:
        pop = quene.pop(0)
        nodes = graph[pop]
        for node in nodes:
            if node not in visited:
                quene.append(node)
                visited.add(node)
        print(pop)


def dsf(graph, start):
    stack = []
    visited = set()
    stack.append(start)
    visited.add(start)
    parents = {start: None}
    while len(stack) > 0:
        pop = stack.pop()
        nodes = graph[pop]
        for node in nodes:
            if node not in visited:
                stack.append(node)
                visited.add(node)
                parents[node] = pop
        print(pop)
    return parents


import heapq


def dikasij(graph, start):
    """
    定义各队列，把初始节点加入到优先队列中
    定义个集合，记录已经被访问过的节点
    定义个距离字典，记录离初始节点最近的距离
    定义父亲字典，记录到当前节点的上一个最近的节点
    """
    dqueue = []
    heapq.heappush(dqueue, (0, start))
    seen = set()
    distance = {}
    parent = {start: None}

    # 当列表中有还有值时
    while len(dqueue) > 0:
        pair = heapq.heappop(dqueue)  # 出队
        distant = pair[0]  # 离初始节点的距离
        node = pair[1]  # 出队的节点
        if node not in seen:
            seen.add(node)  # 将每次出队的节点加入到已经访问过的集合中
            distance[node] = distant  # 将离初始节点的最短距离加入到距离字典

            """
            访问邻居节点，如果邻居节点已经被访问过，则丢弃
            否则，将邻居节点入队，入队的距离需要加上初始节点到上一个节点的距离
            并将邻居节点的最近的父节点设置为上一个节点
            """
            for item in graph[node].keys():
                if item not in seen:
                    heapq.heappush(dqueue, (distant + graph[node][item], item))
                    parent[item] = node
    return distance, parent


if __name__ == '__main__':
    # graph = {
    #     "A": ["B", "C"],
    #     "B": ["A", "C", "D"],
    #     "C": ["A", "B", "D", "E"],
    #     "D": ["B", "C", "E", "F"],
    #     "E": ["C", "D"],
    #     "F": []
    # }
    # bsf(graph, "A")
    # print('-------------------')
    # parents = dsf(graph, "A")
    # for i in parents.keys():
    #     print(i, parents[i])
    #
    # key = 'E'
    # while key != None:
    #     print(key)
    #     key = parents[key]
    graph = {
        "A": {"B": 1, "C": 3},
        "B": {"A": 1, "C": 5, "D": 2, "E": 7},
        "C": {"A": 3, "B": 5, "E": 6},
        "D": {"B": 2, "E": 4, "F": 2},
        "E": {"C": 6, "B": 7, "D": 4},
        "F": {"D": 2}
    }
    distance, parent = dikasij(graph, "A")
    print(distance,parent)
    # 求任意两个节点的最短路径
    key = 'E'
    while key != 'B':
        print(key)
        key = parent[key]
    print('B')
