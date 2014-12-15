import math

volume = float(input())
cube_root = math.pow(volume, 1.0/3.0)

cube_w, cube_h, cube_d = cube_root, cube_root, cube_root
sphere_r = math.pow(volume * 0.75 / math.pi, 1.0/3.0)
cylinder_h = cube_root
cylinder_r = math.sqrt((volume/cube_root)/math.pi)
cone_h = cube_root
cone_r = math.sqrt((3 * volume) / (math.pi * cone_h))

print('Cube: %.2fm wide, %.2fm high, %.2fm deep' % (cube_w, cube_h, cube_d))
print('Sphere: %.2fm radius' % sphere_r)
print('Cylinder: %.2fm high, %.2fm radius' % (cylinder_h, cylinder_r))
print('Cone: %.2fm high, %.2fm base radius' % (cone_h, cone_r))