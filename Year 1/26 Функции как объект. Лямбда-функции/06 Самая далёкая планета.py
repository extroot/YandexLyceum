def find_farthest_orbit(orbits):
    return max(map(lambda x: (x[0], x[1], x[0] * x[1] * 3.141596 if x[0] != x[1] else 0), orbits),
               key=lambda x: x[2])[:2]
