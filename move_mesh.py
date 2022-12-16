# Среднее значение массива
def mid_point(x):
 return min(x) + (max(x) - min(x))/2

# Сдвинуть центр массива точек на final_point
def move(x, y, z, final_point = [0,0,0]):
    base_point = [mid_point(x), mid_point(y), mid_point(z)]
    delta = [final - base for final, base in zip(final_point, base_point)]
    x_moved = [i + delta[0] for i in x]
    y_moved = [i + delta[1] for i in y]
    z_moved = [i + delta[2] for i in z]
    return [x_moved, y_moved, z_moved]