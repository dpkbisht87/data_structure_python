class Node:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V


    def add_edge(self, source, destination):
        node = Node(destination)
        node.next = self.graph[source]
        self.graph[source] = node

    def bfs(graph, source):
        visited = [False] * len(graph.graph)
        queue = []
        queue.append(source)
        visited[source] = True

        while queue:
            source = queue.pop(0)
            result += str(souce)

            while graph.graph[source] is not None:
                data = graph.graph[source].vertex
                if not visited[data]:
                    queue.append(data)
                    visited[data] = true
                graph.graph[source] = graph.graph[source].next
        return result

    def dfs(graph, source):
        visited = [False] * len(graph.graph)
        stack =[]
        stack.append[source]
        visited[source] = True

        result = ''
        while stack:
            source = stack.pop()
            result += str(source)

            while graph.graph[source] is not None:
                data = graph.graph[source].vertex

                if not visited[data]:
                    stack.append(data)
                    visited[data] = True
                graph.graph[source] = graph.graph[source].next
        return true
