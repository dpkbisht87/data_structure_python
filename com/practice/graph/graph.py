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

    def print_graph(self):
        for i in range(self.V):
            temp = self.graph[i]
            while temp:
                print(temp.vertex, end = " ")
                # print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
        print("\n")

    def bfs(graph, source):
        """
        Function to print a BFS of graph
        :param graph: The graph
        :param source: starting vertex
        :return:
        """
        visited = [False] * len(graph.graph)
        print(visited)

        result = ""
        queue = []

        queue.append(source)
        visited[source] = True

        while queue:
            source = queue.pop(0)
            result += str(source)

            while graph.graph[source] is not None:
                data = graph.graph[source].vertex
                if not visited[data]:
                    queue.append(data)
                    visited[data] = True
                graph.graph[source] = graph.graph[source].next
        return result

    def dfs(graph, source):
    """
    Function to print a DFS of graph
    :param graph: The graph
    :param source: starting vertex
    :return:
    """
    visited = [False] * len(graph.graph)
    stack = []
    result  = ''

    stack.append(source)
    visited[source] = True

    while stack:
        source = stack.pop()
        result += str(source)

        while graph.graph[source] is not None:
            data = graph.graph[source].vertex
            if not visited[data]:
                stack.append(data)
                visited[data] = True
            graph.graph[source] = graph.graph[source].next
    return result

# Main program
if __name__ == "__main__":

    V = 5  # Total vertices
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    g.print_graph()