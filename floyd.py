from copy import deepcopy


class Graph:
    def __init__(self, size):
        self.size = size

        # initialize a adjacency matrix
        # if an edge does not exist, then it is marked as float('inf')
        self.adj_matrix = [[float('inf')] * size for i in range(size)]

    def add_edge(self, i, j, weight):
        # add an edge (i -> v) with its weight in the adjacency matrix
        self.adj_matrix[i][j] = weight

    def floyd(self):
        # calculate and print (1) distance and (2) path of all shortest paths

        # Step 1: initialize distance and path array

        distance = deepcopy(self.adj_matrix)# initialize array of minimum distance

        path = [[0] * self.size for i in range(self.size)] # initialize array of vertex indices
        for i in range(self.size):
            for j in range(self.size):
                if i != j:
                    path[i][j] = j
        # if an edge does not exist, then we mark it as 0
        for i in range(self.size):
            for j in range(self.size):
                if i != j:
                    for k in range(self.size):
                        if (k!=i) and (k!=j):
                            if distance[j][k]>distance[j][i]+distance[i][k]:
                                distance[j][k]=distance[j][i]+distance[i][k]
                                path[j][k]=path[j][i]

        print(path)

        # Step 2: calculate the shortest path of all vertices by using flody algorithm
        # write your code

        # Step 3: print result
        print("pair\tdistance\tpath")
        for i in range(self.size):
            for j in range(self.size):
                if i != j:
                    path_i = [i]  # path_i will be save the shortest path for vetex i
                    while path_i[-1] != j:
                        path_i.append(path[path_i[-1]][j])
                    print("{i} -> {j}\t{dist}\t  \t \t{path_list}".format(
                        i=i, j=j, dist=distance[i][j], path_list=' -> '.join([str(j) for j in path_i])
                    ))

        return distance, path


def main():
    size = 4

    g = Graph(size)  # directed_graph
    g.add_edge(1, 0, weight=4)
    g.add_edge(0, 2, weight=-2)
    g.add_edge(1, 2, weight=3)
    g.add_edge(2, 3, weight=2)
    g.add_edge(3, 1, weight=-1)

    shortest_path, path = g.floyd()

    print(path)

    """
    pair	distance	path
    0 -> 1	-1	0 -> 2 -> 3 -> 1
    0 -> 2	-2	0 -> 2
    0 -> 3	0	0 -> 2 -> 3
    1 -> 0	4	1 -> 0
    1 -> 2	2	1 -> 0 -> 2
    1 -> 3	4	1 -> 0 -> 2 -> 3
    2 -> 0	5	2 -> 3 -> 1 -> 0
    2 -> 1	1	2 -> 3 -> 1
    2 -> 3	2	2 -> 3
    3 -> 0	3	3 -> 1 -> 0
    3 -> 1	-1	3 -> 1
    3 -> 2	1	3 -> 1 -> 0 -> 2
    """


main()