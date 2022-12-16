# Функция интерполяции по 4 значениям
def interpolation(t1, x1, t2, x2, x):
    t = (x - x1) * (t2 - t1) / (x2 - x1) + t1
    return t
# Получение температуры по координатам
def define_shell_temperature_by_interpolation(x, y, z, arr):
    coords = (x, y, z)
    pre_arr_by_x = []
    for i in arr:
        if (coords[0] >= i[0][0] and coords[0] <= i[1][0]) or (coords[0] >= i[1][0] and coords[0] <= i[0][0]):
            pre_arr_by_x.append(i)
    pre_arr_by_y = []
    for i in pre_arr_by_x:
        if coords[1] >= i[0][1] and coords[1] <= i[1][1]:
            pre_arr_by_y.append(i)
    pre_arr_by_z = []
    for i in pre_arr_by_y:
        if coords[2] >= i[0][2] and coords[2] <= i[1][2]:
            pre_arr_by_z.append(i)
    if len(pre_arr_by_z) == 0:
        print(coords)
        for i in pre_arr_by_y:
            print(i)
        return 0
    else:
        t1 = pre_arr_by_z[0][2]
        t2 = pre_arr_by_z[0][3]
        y1 = pre_arr_by_z[0][0][1]
        y2 = pre_arr_by_z[0][1][1]
        y = coords[1]
        t = interpolation(t1, y1, t2, y2, y)
    return t