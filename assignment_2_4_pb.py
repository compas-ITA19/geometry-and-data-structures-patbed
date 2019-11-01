# Using faces.obj
# Define a function for traversing the mesh from boundary to boundary in a "straight" line
# Visualise the result
import os, random
from compas.datastructures import Mesh
from compas_plotters import MeshPlotter

def get_straight_path(mesh, start_vertex):
    path = [start_vertex]

    if (len(mesh.vertex_neighbors(path[0])) > 2):
        while(True):
            # find neighbors of last vertex in path
            nbrs = mesh.vertex_neighbors(path[-1], ordered=True)

            # pick the opposite neighbor and continue
            next_i = 1
            if (len(path) > 1):
                next_i = nbrs.index(path[-2]) - 2
            
            path.append(nbrs[next_i])

            # stop if last neighbor is on edge
            if (mesh.is_vertex_on_boundary(path[-1])):
                break

    return path


HERE = os.path.dirname(__file__)
DATA = os.path.join(HERE, 'data')
FILE = os.path.join(DATA, 'faces.obj')
mesh = Mesh.from_obj(FILE)

# set random boundary vertex as start
deg3_vertices = []
for key in mesh.vertices():
    if mesh.vertex_degree(key) == 3:
        deg3_vertices.append(key)

start_vertex = random.choice(deg3_vertices)

# compute straight path
path = get_straight_path(mesh, start_vertex)

# visualize mesh, vertices and path
plotter = MeshPlotter(mesh, figsize=(16, 10))
plotter.draw_faces()
plotter.draw_edges()
plotter.draw_vertices(text = 'key', radius = 0.15)
plotter.draw_vertices(facecolor = (0, 255, 255), text = 'key', keys = path[:1], radius = 0.2)
plotter.draw_vertices(facecolor = (255, 0, 255), text = 'key', keys = path[1:], radius = 0.2)
plotter.show()
