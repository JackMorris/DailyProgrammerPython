# http://www.reddit.com/r/dailyprogrammer/comments/20cydp/14042014_challenge_152_hard_minimum_spanning_tree/


class DisjointSet:
    def __init__(self):
        self.parent = {}    # Parent of each item. If x is root, parent[x]=x
        self.rank = {}      # Rank of tree in set, indexed by root.

    def make_set(self, x):
        """ Add a single element set, containing x, to the DisjointSet. """
        self.parent[x] = x
        self.rank[x] = 0

    def union(self, x, y):
        """
        Union the two sets identified by `x` and `y`. Here, `x` and `y` are the
        roots of the respective trees for each set, and can be retrieved using
        `find_set()`.
        """
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def find_set(self, x):
        """
        Returns the set identifier for the set containing `x`. Therefore
        returns the root of the tree containing `x`. As an optimisation, also
        performs path compression as this operation is performed (flattens the
        tree).
        """
        if x != self.parent[x]:
            self.parent[x] = self.find_set(self.parent[x])
        return self.parent[x]


class Edge:
    def __init__(self, v1, v2, weight):
        self.v1, self.v2, self.weight = v1, v2, weight
        self.v1_char = chr(self.v1+65)
        self.v2_char = chr(self.v2+65)


if __name__ == '__main__':
    vertex_count = int(input())
    edges = []
    for v1 in range(vertex_count):
        str_weights = input().split(',')
        for v2 in range(v1+1, vertex_count):
            weight = int(str_weights[v2])
            if weight >= 0:
                edges.append(Edge(v1, v2, weight))

    # Implementation of Kruskal's algorithm
    mst = []
    d = DisjointSet()
    edges.sort(key=lambda e: e.weight)
    for v in range(vertex_count):
        d.make_set(v)

    for edge in edges:
        v1_set = d.find_set(edge.v1)
        v2_set = d.find_set(edge.v2)
        if v1_set is not v2_set:
            # v1 and v2 not currently connected, add edge to MST.
            mst.append(edge)
            d.union(v1_set, v2_set)

    mst_sum = sum(map(lambda e: e.weight, mst))
    print('MST sum: %s' % mst_sum)
    print(','.join(edge.v1_char + edge.v2_char for edge in mst))