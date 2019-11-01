# Define a function for computing the cross products of two arrays of vectors
# version in pure python using loops
# version using numpy without loops
from compas.geometry import Vector
import numpy as np

def cross_vectors(u, v):
    # compute the cross product of two given vectors and return it in a list
    c = [u[1] * v[2] - u[2] * v[1],
         u[2] * v[0] - u[0] * v[2],
         u[0] * v[1] - u[1] * v[0]]

    return c

def cross_two_arrays_vectors(u, v):
    # compute the cross product of two arrays of vectors
    return [cross_vectors(u[i], v[i]) for i in range(len(u))]

def cross_two_arrays_vectors_np(u, v):
    # compute the cross product of two arrays of vectors using numpy
    u_np = np.array(u)
    v_np = np.array(v)

    return np.cross(u_np, v_np)

u = [
    [2.0, 0.0, 0.5],
    [0.0, 0.0, 8.0],
    [0.0, 5.0, 0.0],
    [4.0, 1.0, 0.0]
    ]

v = [
    [0.0, 0.0, 5.5],
    [0.0, 8.7, 0.0],
    [1.5, 0.0, 0.0],
    [3.0, 2.0, 0.0]
    ]

print(cross_two_arrays_vectors(u, v))
print(cross_two_arrays_vectors_np(u, v))