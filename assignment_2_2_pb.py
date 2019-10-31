# Use the cross product to compute the area of a convex, 2D polygon
from compas.geometry import Polygon

def area_polygon(polygon):
    # compute the area of a convex polygon

    c = polygon.centroid
    area = 0
    vertices = polygon.points

    # area of polygon is the sum of all triangles formed by two consecutive vertices and the centroid
    for i in range(len(vertices)):
        u = vertices[i-1]
        v = vertices[i]
        area += (c - u).cross(c - v).length / 2
    return area


polygon = Polygon([
    [0.0, 0.0, 0.0],
    [1.0, 0.0, 0.0],
    [1.0, 1.0, 0.0],
    [0.0, 1.0, 0.0]
    ])

print(area_polygon(polygon))