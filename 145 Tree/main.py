# http://www.reddit.com/r/dailyprogrammer/comments/1t0r09/121613_challenge_145_easy_tree_generation/

base_size, tree_c, trunk_c = input().split()
base_size = int(base_size)

number_of_levels = int((base_size+1)/2)
for level in range(number_of_levels-1, 0, -1):
    leaves_to_print = base_size - 2*level
    print(' '*level + tree_c*leaves_to_print)

trunk_offset = int((base_size-3)/2)
print(' '*trunk_offset + trunk_c*3)