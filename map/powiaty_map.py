
# A02_Granice_powiatow

import geopandas as gpd
import matplotlib.pyplot as plt

url = "https://mapy.geoportal.gov.pl/wss/service/PZGIK/PRG/WFS/AdministrativeBoundaries?SERVICE=WFS&\
REQUEST=GetFeature&VERSION=2.0.0&\
TYPENAMES=A02_Granice_powiatow&\
TYPENAME=A02_Granice_powiatow&\
STARTINDEX=0&\
COUNT=1000&\
SRSNAME=urn:ogc:def:crs:EPSG::2180&\
BBOX=171000,130000,870000,790000,urn:ogc:def:crs:EPSG::2180"

df = gpd.read_file(url)

print(df.head())

# Narysuj mapę powiatów
fig, ax = plt.subplots(figsize=(10, 10))
df.plot(ax=ax, color='lightblue', edgecolor='black')
# Dodaj etykiety na mapie
for idx, row in df.iterrows():
    # Współrzędne środka geometrycznego (centroid) powiatu
    centroid = row['geometry'].centroid
    # Dodanie tekstu z nazwą powiatu
    ax.annotate(text=row['JPT_NAZWA_'],
      xy=(centroid.x, centroid.y), 
      horizontalalignment='center', fontsize=8, color='darkblue')

plt.title('Mapa powiatów w Polsce')
plt.show()
