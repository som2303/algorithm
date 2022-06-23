class GraphNode:

    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None


class Graph:

    def __init__(self, size):
        self.adj_list = [None] * size
        self.size = size

    def insert_edge(self, u, v):
        ## Completed Function - Do not remove
        # Insert an edge(u, v) into graph
        if u >= self.size or v >= self.size:
            print("vertex index error")
            return

        new_node = GraphNode(v)
        new_node.next = self.adj_list[u]
        self.adj_list[u] = new_node

        new_node = GraphNode(u)
        new_node.next = self.adj_list[v]
        self.adj_list[v] = new_node

    def depth_first_search(self, v, visited=None):
        # DFS - traverses a graph in a depthward
        """
        Input:  value
        Output: print(v, end = ' ')
        """
        if visited == None:
            visited = [False] * (self.size)
        print(v,end=' ')

        visited[v]=True
        temp=self.adj_list[v]
        while temp:
            if visited[temp.vertex] == False:
                self.depth_first_search(temp.vertex, visited)

            temp=temp.next



    # -----------Fill in the blank

    def breadth_first_search(self, v):
        # BFS - traverses a graph in a breadthward
        """
        Input:  v
        Output: print(v, end = ' ')
        """
        visited = [False] * (self.size)
        queue = []


        visited[v] = True
        queue.append(v)

        while len(queue)!=0:
            a=queue.pop(0)
            print(a, end=' ')
            temp = self.adj_list[a]
            while temp:
                if visited[temp.vertex] == False:
                    queue.append(temp.vertex)
                    visited[temp.vertex]=True
                temp = temp.next



    # -----------Fill in the blank

    def display(self):
        ## Completed Function - Do not remove
        # Display graph adjacency list
        for i in range(self.size):
            if self.adj_list[i] != None:
                print(i, end='')

                values = []
                start_node = self.adj_list[i]
                while start_node:
                    values.append(start_node.vertex)
                    start_node = start_node.next

                print(" ", ' -> '.join(map(str, values)))
            else:
                print(i)


def main():
    graph = Graph(5)

    graph.insert_edge(0, 4)
    graph.insert_edge(0, 2)
    graph.insert_edge(0, 1)
    graph.insert_edge(2, 4)
    graph.insert_edge(2, 3)
    graph.insert_edge(3, 4)

    graph.display()
    print("DFS", end='\t')
    graph.depth_first_search(0)  # 1 0 2 3 4
    print("\nBFS", end='\t')
    graph.breadth_first_search(0)  # 0 1 2 4 3


main()