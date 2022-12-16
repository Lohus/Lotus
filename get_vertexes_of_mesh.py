# Координаты вершин по начальной и конечной точке
def get_vertexes(first_point, last_point):
    vertexlist = []
    delta = [last - first for last, first in zip(last_point, first_point)]
    for i in range(8):
        vertexlist.append([first_point[a] + delta[a] * ((i&(2**(2 - a)))>>(2 - a)) for a in range(3)] )
    return vertexlist
