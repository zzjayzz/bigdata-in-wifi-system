import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
from sklearn.cluster import DBSCAN
from geopy.distance import great_circle
from shapely.geometry import MultiPoint
# plt.switch_backend('agg')

# matplotlib.use('Agg')

df_1= pd.read_csv(r'C:\Users\dell\Documents\GPS\traceset_2_code\function of building_with_gps.csv',encoding = 'unicode_escape')
df_2=df_1.iloc[:,2:4]
# df_2.drop_duplicates(['lat'],keep = 'first', inplace = True)
# df_2=df_2.loc[(df_2['lat']>=59.345) & (df_2['lat']<=59.352)]
# df_2=df_2.loc[(df_2['long']>=18.065) & (df_2['long']<=18.074)]
print(len(df_2))
coords=df_2.to_numpy()
#

kms_per_radian = 6371.0088
epsilon = 0.03/ kms_per_radian

db = DBSCAN(eps=epsilon, min_samples=1, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))
cluster_labels = db.labels_
num_clusters = len(set(cluster_labels))
clusters = pd.Series([coords[cluster_labels == n] for n in range(num_clusters)])
print('Number of clusters: {}'.format(num_clusters))








core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True

unique_labels = set(cluster_labels)
colors = [plt.cm.Spectral(each)
          for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]

    class_member_mask = (cluster_labels == k)
    xy = coords[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 1], xy[:, 0], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=12)

    xy = coords[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 1], xy[:, 0], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=8)
n_clusters_ = len(set(cluster_labels)) - (1 if -1 in cluster_labels else 0)
plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()
df_1['cluster']=cluster_labels
print(df_1)
# df_1.to_csv('cluster.csv', encoding='utf-8', index=False)
#
# plt.figure(figsize=(10, 7))
# dendrogram(Z,
#             orientation='top',
#             distance_sort='descending',
#             show_leaf_counts=True)
# # plt.show()

df_count= pd.read_csv(r'C:\Users\dell\Documents\GPS\traceset_2_code\venv\buildingcount.csv',encoding = 'unicode_escape')
df_combine= df_1.join(df_count, lsuffix='_caller', rsuffix='_other')
