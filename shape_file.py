import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns
# plt.switch_backend('agg')
sns.set(style='whitegrid', palette='pastel', color_codes=True)
sns.mpl.rc('figure', figsize=(10,6))
shp_path =r'C:\Users\dell\Documents\GPS\traceset_2_code\venv\shap\buildings.shp'
sf = shp.Reader(shp_path)

def read_shapefile(sf):
    """
    Read a shapefile into a Pandas dataframe with a 'coords'
    column holding the geometry information. This uses the pyshp
    package
    """
    fields = [x[0] for x in sf.fields][1:]
    records = sf.records()
    shps = [s.points for s in sf.shapes()]
    df = pd.DataFrame(columns=fields, data=records)
    df = df.assign(coords=shps)
    return df
df = read_shapefile(sf)

# def plot_shape(id, s=None):
#     """ PLOTS A SINGLE SHAPE """
#     plt.figure()
#     ax = plt.axes()
#     ax.set_aspect('equal')
#     shape_ex = sf.shape(id)
#     x_lon = np.zeros((len(shape_ex.points),1))
#     y_lat = np.zeros((len(shape_ex.points),1))
#     for ip in range(len(shape_ex.points)):
#         x_lon[ip] = shape_ex.points[ip][0]
#         y_lat[ip] = shape_ex.points[ip][1]
#     plt.plot(x_lon,y_lat)
#     x0 = np.mean(x_lon)
#     y0 = np.mean(y_lat)
#     plt.text(x0, y0, s, fontsize=10)
#     # use bbox (bounding box) to set plot limits
#     plt.xlim(shape_ex.bbox[0],shape_ex.bbox[2])
#     return x0, y0
# building = 'Nymble'
# building_id = df[df.name == building].index.to_numpy()[0]
# plot_shape(building_id, building)
# plt.show()

def plot_map(sf, x_lim=None, y_lim=None, figsize=(11, 9)):
    '''
    Plot map with lim coordinates
    '''
    plt.figure(figsize=figsize)
    id = 0
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        plt.plot(x, y, 'k')

        if (x_lim == None) & (y_lim == None):
            x0 = np.mean(x)
            y0 = np.mean(y)
            plt.text(x0, y0,id, fontsize=10)
        id = id + 1

    if (x_lim != None) & (y_lim != None):
        plt.xlim(x_lim)
        plt.ylim(y_lim)

#
#
#
#
y_lim = (59.344,59.353) # latitude
x_lim = (18.06,18.08) # longitude
plot_map(sf)
# plot_map(sf, x_lim, y_lim)
plt.show()
#
# def plot_map2(id, sf, x_lim=None, y_lim=None, figsize=(11, 9)):
#     '''
#     Plot map with lim coordinates
#     '''
#
#     plt.figure(figsize=figsize)
#     for shape in sf.shapeRecords():
#         x = [i[0] for i in shape.shape.points[:]]
#         y = [i[1] for i in shape.shape.points[:]]
#         plt.plot(x, y, 'k')
#
#     shape_ex = sf.shape(id)
#     x_lon = np.zeros((len(shape_ex.points), 1))
#     y_lat = np.zeros((len(shape_ex.points), 1))
#     for ip in range(len(shape_ex.points)):
#         x_lon[ip] = shape_ex.points[ip][0]
#         y_lat[ip] = shape_ex.points[ip][1]
#     plt.plot(x_lon, y_lat, 'r', linewidth=3)
#
#     if (x_lim != None) & (y_lim != None):
#         plt.xlim(x_lim)
#         plt.ylim(y_lim)
#
# plot_map2(7, sf, x_lim, y_lim)






















#
# y_lim = (59.345862,59.352709) # latitude
# x_lim = (18.061,18.076116) # longitude
# def plot_map_fill_multiples_ids(title, comuna, sf,
#                                 x_lim=None,
#                                 y_lim=None,
#                                 figsize=(11, 9),
#                                 color='r'):
#     '''
#     Plot map with lim coordinates
#     '''
#
#     plt.figure(figsize=figsize)
#     fig, ax = plt.subplots(figsize=figsize)
#     fig.suptitle(title, fontsize=16)
#     for shape in sf.shapeRecords():
#         x = [i[0] for i in shape.shape.points[:]]
#         y = [i[1] for i in shape.shape.points[:]]
#         ax.plot(x, y, 'k')
#
#     for id in comuna:
#         shape_ex = sf.shape(id)
#         x_lon = np.zeros((len(shape_ex.points), 1))
#         y_lat = np.zeros((len(shape_ex.points), 1))
#         for ip in range(len(shape_ex.points)):
#             x_lon[ip] = shape_ex.points[ip][0]
#             y_lat[ip] = shape_ex.points[ip][1]
#         ax.fill(x_lon, y_lat, color)
#
#         x0 = np.mean(x_lon)
#         y0 = np.mean(y_lat)
#         plt.text(x0, y0, id, fontsize=10)
#
#     if (x_lim != None) & (y_lim != None):
#         plt.xlim(x_lim)
#         plt.ylim(y_lim)
#
# building_id = [7, 72, 3, 4, 5, 66]
# plot_map_fill_multiples_ids("Multiple Shapes",
#                             building_id, sf, color = 'r')
#
#
# def plot_comunas_2(sf, title, comunas, color):
#     '''
#     Plot map with selected comunes, using specific color
#     '''
#
#     df = read_shapefile(sf)
#     comuna_id = []
#     for i in comunas:
#         comuna_id.append(df[df.NOM_COMUNA == i.upper()]
#                          .index.get_values()[0])
#     plot_map_fill_multiples_ids(title, comuna_id, sf,
#                                 x_lim=None,
#                                 y_lim=None,
#                                 figsize=(11, 9),
#                                 color=color);
#
#
#
#
#
#
#
#
#
# south = ['alhué', 'calera de tango', 'buin', 'isla de maipo', 'el bosque', 'paine', 'la granja', 'pedro aguirre cerda', 'lo espejo', 'puente alto',
#          'san joaquín', 'san miguel', 'pirque', 'san bernardo', 'san ramón', 'la cisterna', 'talagante', 'la pintana']
# plot_comunas_2(sf, 'South', south, 'c')




























#
# def calc_color(data, color=None):
#     if color == 1: color_sq =['#dadaebFF', '#bcbddcF0', '#9e9ac8F0','#807dbaF0', '#6a51a3F0', '#54278fF0']; colors = 'Purples';
#
#     elif color == 2: color_sq = ['#c7e9b4', '#7fcdbb', '#41b6c4','#1d91c0', '#225ea8', '#253494'];colors = 'YlGnBu';
#     elif color == 3: color_sq =['#f7f7f7', '#d9d9d9', '#bdbdbd','#969696', '#636363', '#252525'];colors = 'Greys';
#     elif color == 9: color_sq =['#ff0000', '#ff0000', '#ff0000','#ff0000', '#ff0000', '#ff0000']
#     else:            color_sq =['#ffffd4', '#fee391', '#fec44f','#fe9929', '#d95f0e', '#993404'];colors = 'YlOrBr';
#     new_data, bins = pd.qcut(data, 6, retbins=True,
#                          labels=list(range(6)))
#     color_ton = []
#     for val in new_data:
#         color_ton.append(color_sq[val])
#     if color != 9:
#         colors = sns.color_palette(colors, n_colors=6)
#         sns.palplot(colors, 0.6);
#         for i in range(6):
#             print("\n" + str(i + 1) + ': ' + str(int(bins[i])) +
#               " => " + str(int(bins[i + 1]) - 1), end=" ")
#         print("\n\n   1   2   3   4   5   6")
#     return color_ton, bins;
#
#
#
#
#
#
# def plot_comunas_data(sf, title, comunas, data=None,
#                       color=None, print_id=False):
#     '''
#     Plot map with selected comunes, using specific color
#     '''
#
#     color_ton, bins = calc_color(data, color)
#     df = read_shapefile(sf)
#     comuna_id = []
#     for i in comunas:
#         i = conv_comuna(i).upper()
#         comuna_id.append(df[df.NOM_COMUNA ==
#                             i.upper()].index.get_values()[0])
#     plot_map_fill_multiples_ids_tone(sf, title, comuna_id,
#                                      print_id,
#                                      color_ton,
#                                      bins,
#                                      x_lim=None,
#                                      y_lim=None,
#                                      figsize=(11, 9));
#
#
#
#
#
#
#
#
#
#
#
#
# def plot_map_fill_multiples_ids_tone(sf, title, comuna,
#                                      print_id, color_ton,
#                                      bins,
#                                      x_lim=None,
#                                      y_lim=None,
#                                      figsize=(11, 9)):
#     '''
#     Plot map with lim coordinates
#     '''
#
#     plt.figure(figsize=figsize)
#     fig, ax = plt.subplots(figsize=figsize)
#     fig.suptitle(title, fontsize=16)
#
#
# for shape in sf.shapeRecords():
#     x = [i[0] for i in shape.shape.points[:]]
#     y = [i[1] for i in shape.shape.points[:]]
#     ax.plot(x, y, 'k')
#
# for id in comuna:
#     shape_ex = sf.shape(id)
#     x_lon = np.zeros((len(shape_ex.points), 1))
#     y_lat = np.zeros((len(shape_ex.points), 1))
#     for ip in range(len(shape_ex.points)):
#         x_lon[ip] = shape_ex.points[ip][0]
#         y_lat[ip] = shape_ex.points[ip][1]
#     ax.fill(x_lon, y_lat, color_ton[comuna.index(id)])
#     if print_id != False:
#         x0 = np.mean(x_lon)
#         y0 = np.mean(y_lat)
#         plt.text(x0, y0, id, fontsize=10)
# if (x_lim != None) & (y_lim != None):
#     plt.xlim(x_lim)
#     plt.ylim(y_lim)




