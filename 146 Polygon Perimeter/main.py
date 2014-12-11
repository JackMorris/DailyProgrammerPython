# http://www.reddit.com/r/dailyprogrammer/comments/1tixzk/122313_challenge_146_easy_polygon_perimeter/

import math

side_count, circumradius = input().split()
side_count, circumradius = int(side_count), float(circumradius)

side_length = 2*circumradius*math.sin(math.pi/side_count)
print('%.3f' % (side_count*side_length))