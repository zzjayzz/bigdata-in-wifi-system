import numpy as np
import pandas as pd
# from matplotlib.mlab import griddata
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from scipy.interpolate import griddata as gd

# 设置基本图片画板
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, frame_on=False)

# 提取数据
data = pd.read_csv('data.txt', delim_whitespace=True)
norm = Normalize()

#设置地图边界值
lllon = 18.058
lllat = 59.343
urlon = 18.08
urlat = 59.354



#初始化地图
m = Basemap(
    projection = 'merc',
    llcrnrlon = lllon, llcrnrlat = lllat, urcrnrlon = urlon, urcrnrlat = urlat,
    resolution='h')

m.readshapefile(r'C:\Users\dell\Documents\GPS\traceset_2_code\venv\shap\roads', 'roads')
data['projected_lon'], data['projected_lat'] = m(*(data.Lon.values, data.Lat.values))

# 生成经纬度的栅格数据
numcols, numrows = 1000, 1000
xi = np.linspace(data['projected_lon'].min(), data['projected_lon'].max(), numcols)
yi = np.linspace(data['projected_lat'].min(), data['projected_lat'].max(), numrows)
xi, yi = np.meshgrid(xi, yi)

# 插值
x, y, z = data['projected_lon'].values, data['projected_lat'].values, data.Z.values
zi = gd(
    (data[['projected_lon', 'projected_lat']]),
    data.Z.values,
    (xi, yi),
    method='cubic')

# 设置地图细节
m.drawmapboundary(fill_color = 'white')
m.fillcontinents(color='#C0C0C0', lake_color='#7093DB')
m.drawcountries(
    linewidth=.75, linestyle='solid', color='#000073',
    antialiased=True,
    ax=ax, zorder=3)

m.drawparallels(
    np.arange(lllat, urlat, 2.),
    color = 'black', linewidth = 0.5,
    labels=[True, False, False, False])
m.drawmeridians(
    np.arange(lllon, urlon, 2.),
    color = '0.25', linewidth = 0.5,
    labels=[False, False, False, True])

# 等值面图绘制
con = m.contourf(xi, yi, zi, zorder=4, alpha=0.6, cmap='jet')
# 插入测绘点
list1=list(data['Z'])
m.scatter(
    data['projected_lon'],
    data['projected_lat'],
    color='#545454',
    edgecolor='#ffffff',
    alpha=.75,
    s=50 * norm(list1),
    cmap='jet',
    ax=ax,
    vmin=zi.min(), vmax=zi.max(), zorder=4)

# 插入色标、名称和范围
cbar = plt.colorbar(con,orientation='horizontal', fraction=.057, pad=0.05)
cbar.set_label("Mean Rainfall - mm")



plt.title("Mean Rainfall")
plt.savefig("rainfall.png", format="png", dpi=300, transparent=True)
plt.show()