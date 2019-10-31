# Given two vectors, use the cross product to create a set of three orthonormal vectors
from compas.geometry import Vector

def orthonormal_vectors_from_two_vectors(u, v):
    # create 3 orthonormal vectors from 2 given vectors
    x = u.cross(v)
    return u.unitized(), x.unitized(), u.cross(x).unitized()

u = Vector(5.0, 0.0, 12.0)
v = Vector(0.0, 10.0, 0.0)

print(orthonormal_vectors_from_two_vectors(u, v))