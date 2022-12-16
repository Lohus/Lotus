from get_vertexes_of_mesh import *

# Получение i, j, k индексов и x, y, z всех точек
def get_xyz_ijk(arrtemp):
    ib=[0,2,6,4,1,3,7,5,1,7,0,6]
    jb=[1,3,7,5,3,7,5,1,5,3,2,4]
    kb=[2,6,4,0,2,6,4,0,3,5,4,2]
    x = []
    y = []
    z = []
    i = []
    k = []
    j = []
    for values in arrtemp:
        arrxyz = get_vertexes(values[0], values[1])
        temp = len(x)
        x.extend([vertex[0] for vertex in arrxyz])
        y.extend([vertex[1] for vertex in arrxyz])
        z.extend([vertex[2] for vertex in arrxyz])
        i.extend([temp + value for value in ib])
        j.extend([temp + value for value in jb])
        k.extend([temp + value for value in kb])
    return {'x': x, 'y': y, 'z': z, 'i': i, 'j': j, 'k': k}
