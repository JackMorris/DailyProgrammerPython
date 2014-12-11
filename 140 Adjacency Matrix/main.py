# http://www.reddit.com/r/dailyprogrammer/comments/1t6dlf/121813_challenge_140_intermediate_adjacency_matrix/

n, edge_count = map(int, input().split())
matrix = [['0']*n for _ in range(n)]

for _ in range(0, edge_count):
    start_nodes, end_nodes = input().split(' -> ')
    for start_node in start_nodes.split():
        for end_node in end_nodes.split():
            matrix[int(start_node)][int(end_node)] = '1'

for row in matrix:
    print(''.join(row))