from graph import Graph
from queue import MyQueue
from stack import MyStack

def bfs_traversal(g, source):
        result = ""
        num_of_vertices = g.vertices
        visited = [False] * num_of_vertices
        q = MyQueue()
        q.enqueue(source)
        visited[source] = True

        while not q.is_empty():
            cur = q.dequeue()
            result += str(cur)
            temp = g.array[cur].head_node
            while temp is not None:
                if not visited[temp.data]:
                    q.enqueue(temp.data)
                    visited[temp.data] = True
                temp = temp.next_element
        return result

def dfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    if num_of_vertices is 0:
        return result
    visited = [False] * num_of_vertices
    s = MyStack()
    s.push(source)
    visited[source] = True

    while not s.is_empty():
        cur = s.pop()
        result += str(cur)
        temp = g.array[cur].head_node
        while temp is not None:
            if not visited[temp.data]:
                s.push(temp.data)
                visited[temp.data] = True
            temp = temp.next_element
    return result

def perform_DFS(g, source):
    vertex_visited = 0
    s = MyStack()
    visited = [False] * g.vertices
    s.push(source)
    visited[source] = True
    while not s.is_empty():
        cur = s.pop()
        temp = g.array[cur].head_node
        while temp:
            if not visited[temp.data]:
                visited[temp.data] = True
                vertex_visited += 1
                s.push(temp.data)
            temp = temp.next_element
    return vertex_visited + 1


def find_mother_vertex(g):
    num_of_vertices_reached = 0
    num_of_vertices = g.vertices

    for i in range(g.vertices):
        num_of_vertices_reached = perform_DFS(g, i)
        if num_of_vertices_reached is g.vertices:
            return i
    return -1



def get_adjacent_nodes(g, source):
    temp = g.array[source].head_node
    edges = 0
    while temp:
        edges += 1
        temp = temp.next_element
    print(source, edges)
    return edges

def num_edges(g):
    vertices_count = g.vertices
    edges = 0

    for i in range(vertices_count):
        edges += get_adjacent_nodes(g, i)
    return edges  // 2


def check_path(g, source, destination):
    vertices_count = g.vertices
    visited = [False] * vertices_count
    s = MyStack()
    s.push(source)
    visited[source] = True
    while not s.is_empty():
        cur = s.pop()
        temp = g.array[cur].head_node
        while temp:
            if not visited[temp.data]:
                if temp.data == destination:
                    return True
                visited[temp.data] = True
                s.push(temp.data)
            temp = temp.next_element
    return False

def check_cycle(g, node, visited, parent):
    visited[node] = True

    temp = g.array[node].head_node
    while temp:
        if not visited[temp.data]:
            if check_cycle(g, temp.data, visited, node):
                return True
        elif temp.data != parent:
            return True
        temp = temp.next_element
    return False

def is_tree(g):
    visited = [False] * g.vertices
    if check_cycle(g, 0, visited, -1):
        return False
    for i in visited:
        if not i:
            return False
    return True
