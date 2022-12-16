
from get_vertexes_of_mesh import *
from move_mesh import move
from get_all_point_of_mesh import *
from interpolation import *

# Класс для мэша температуры
class TempT():
    def __init__(self, array_of_temp):
        temp = get_xyz_ijk(array_of_temp)
        self.x = temp.get('x')
        self.y = temp.get('y')
        self.z = temp.get('z')
        self.i = temp.get('i')
        self.j = temp.get('j')
        self.k = temp.get('k')
        self.intens = [define_shell_temperature_by_interpolation(x, y, z, array_of_temp) for x,y,z in zip(self.x, self.y, self.z)]
    def move_on(self, x, y, z):
        return move(self.x, self.y, self.z, [x, y, z])