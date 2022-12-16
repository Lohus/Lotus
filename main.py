import plotly
import numpy as np
from stl import mesh
import plotly.graph_objects as go
import urllib
from stl2mesh3dlib import stl2mesh3d
from move_mesh import move
from DataPrep import *
from datatemp import *

# Подготовка 3D мэша из STL
my_mesh = mesh.Mesh.from_file('stl\sthe_stl_model_22606154.stl')
vertices, I, J, K = stl2mesh3d(my_mesh)
x, y, z = move(*vertices.T) # Сдвигаем центр меша на координаты (0,0,0)
colorscale= [[0, '#555555'], [1, '#e5dee5']]                           
STLMesh = go.Mesh3d(
            x=x,
            y=y,
            z=z, 
            i=I, 
            j=J, 
            k=K,
            flatshading=True,
            colorscale=colorscale, 
            intensity=z, 
            name='LOTUS STHE',
            showscale=False)

# Подготовка 3D-меша и данных температуры
DataOfTemperature = TempT(arr)
x_t, y_t, z_t = DataOfTemperature.move_on(-100, 5, 20) 
print(min(DataOfTemperature.intens))
print(max(DataOfTemperature.intens))                        
TempMesh = go.Mesh3d(
            x=x_t,
            y=y_t,
            z=z_t,
            i=DataOfTemperature.i,
            j=DataOfTemperature.j,
            k=DataOfTemperature.k,
            colorscale='Inferno',
            cmin = min(DataOfTemperature.intens),
            cmax = max(DataOfTemperature.intens),
            intensity=DataOfTemperature.intens,
            name='Data_Of_Temperature',
            opacity= 0.2,
            showscale=True)
title = "Mesh of Temp and STL"
layout = go.Layout(
    paper_bgcolor='rgb(1,1,1)',
    title_text=title,
    title_x=0.5,
    font_color='white',
    width=1600,
    height=800,
    scene_camera=dict(
        eye=dict(x=1.25, y=1.25, z=1)),
    scene_xaxis_visible=True,
    scene_yaxis_visible=True,
    scene_zaxis_visible=True,
    scene = dict(aspectratio = dict(
        x = 4,
        y = 1,
        z = 1
    )),
)
fig = go.Figure(data=[STLMesh], layout=layout)
fig.add_trace(TempMesh)
fig.show()