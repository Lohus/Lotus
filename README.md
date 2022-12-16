# Отображение 3-х мерного графика температуры совместно с моделью STL

Температура задаётся в виде списка блока данных, каждый из которых содержит:
- [$x_1$, $y_1$, $z_1$] - координаты начальной точки;
- [$x_2$, $y_2$, $z_2$] - координаты конечной точки; 
- $t_1$ - значение температуры в первой точке;
- $t_2$ - значение температуры во второй точке.

По данным из блока данных рассчитываются координаты всех точек ($x$, $y$, $z$), индексы ($i$, $j$, $k$), необходимые для кооректного отображения блока данных в пространстве, и температура $t$ в каждой точке блока. Такие расчёты осуществляются для каждого блока данных.

После всех расчётов в классе TempT имеется несколько массивов по которым строится конечный объект на графике:
- $x$, $y$, $z$ - массивы хронящие значенния всех точек по соответствующей координате;
- $i$, $j$, $k$ - массивы индексов, каждый массив содержит пордяковый номер точек, так три индекса $i$, $j$, $k$ образуют треугольник;
- $intens$ - значения температуры для каждой точки.

Конечный объект температуры имеет вид:
![Mesh of temp](https://raw.githubusercontent.com/Lohus/Lotus/main/img/temp.png)

Наложение объектов:
![All meshes](https://raw.githubusercontent.com/Lohus/Lotus/main/img/allmesh.png)

