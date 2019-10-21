import numpy as np


graph1 = {6: [4],
          4: [3, 5, 6],
          3: [4, 2],
          5: [1, 2, 4],
          2: [3, 5, 1],
          1: [5, 2]}

graph2 = {'E': ['A', 'B'],
          'A': ['E', 'B', 'D'],
          'B': ['E', 'A', 'D'],
          'D': ['A', 'B', 'C'],
          'C': ['D']}


def degreeAndconnectivityOfUndirectedGraph(undirectedGraph):
    for keys, values in undirectedGraph.items():
        print("{0} is connected to {1} and has the degree of {2}".format(keys, values, len(values)))


# degreeAndconnectivityOfUndirectedGraph(graph1)
# degreeAndconnectivityOfUndirectedGraph(graph2)


graph3 = {7: {'in': [], 'out': [8, 11]},
          5: {'in': [], 'out': [11]},
          3: {'in': [], 'out': [8, 10]},
          11: {'in': [7, 5], 'out': [2, 9, 10]},
          8: {'in': [7, 3], 'out': [9]},
          2: {'in': [11], 'out': []},
          9: {'in': [11, 8], 'out': []},
          10: {'in': [11, 3], 'out': []},}


def degreeAndconnectivityOfDirectedGraph(directedGraph):
    for keys, values in directedGraph.items():
        data = values['in'] + values['out']
        print("{0} is connected to {1} And in degree is {2} And out degree is {3}".format(keys, data, len(values['in']), len(values['out']) ))

# degreeAndconnectivityOfDirectedGraph(graph3)


def findMyPath(_fromthis, _tothis, graph):
    path = [_fromthis]
    def find(fromthis, tothis, graph):
        if fromthis == tothis:
            return True
        else:
            for nowforthis in graph[fromthis]:
                if (nowforthis not in path):
                    path.append(nowforthis)
                    find(nowforthis, tothis, graph)
                    return path
    find(_fromthis, _tothis, graph)
    print(path)


findMyPath(6, 1, graph1)
findMyPath('E','C',graph2)

def findDirectedPath(_fromthis, _tothis, graph):
    path = [_fromthis]

    def find(fromthis, tothis, graph):
        if fromthis == tothis:
            return True
        else:
            for nowforthis in graph[fromthis]:
                if (nowforthis not in path):
                    path.append(nowforthis)
                    find(nowforthis, tothis, graph)
                    return path
    find(_fromthis, _tothis, graph)
    print(path)