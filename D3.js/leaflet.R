# Load necessary libraries
library(leaflet)
library(sf)

# Define the GeoJSON URL
provincies_url <- "https://cartomap.github.io/nl/wgs84/provincie_2024.geojson"
gemeenten_url <- "https://cartomap.github.io/nl/wgs84/gemeente_2024.geojson"
wijken_url <- "https://cartomap.github.io/nl/wgs84/wijk_2024.geojson"
buurten_url <- "https://cartomap.github.io/nl/wgs84/buurt_2024.geojson"

# Create a Leaflet map
provincies_url %>%
  st_read() %>%
  leaflet() %>%
  addTiles() %>% # Add base map tiles
  addPolygons(
    fillColor = ~colorFactor(topo.colors(12), statcode)(statcode),
    fillOpacity = 0.7,
    color = "black",
    weight = 1,
    popup = ~paste("Provincie: ", statnaam)
  ) %>%
  setView(lng = 5.5, lat = 52.2, zoom = 7) # Center on the Netherlands

# Create a Leaflet map
gemeenten_url %>%
  st_read() %>%
  leaflet() %>%
  addTiles() %>% # Add base map tiles
  addPolygons(
    fillColor = ~colorFactor(topo.colors(12), statcode)(statcode),
    fillOpacity = 0.7,
    color = "black",
    weight = 1,
    popup = ~paste("Gemeente: ", statnaam)
  ) %>%
  setView(lng = 5.5, lat = 52.2, zoom = 7) # Center on the Netherlands

# Create a Leaflet map
wijken_url %>%
  st_read() %>%
  leaflet() %>%
  addTiles() %>% # Add base map tiles
  addPolygons(
    fillColor = ~colorFactor(topo.colors(12), statcode)(statcode),
    fillOpacity = 0.7,
    color = "black",
    weight = 1,
    popup = ~paste("Wijk: ", statnaam)
  ) %>%
  setView(lng = 5.5, lat = 52.2, zoom = 7) # Center on the Netherlands

# info
# https://service.pdok.nl/cbs/gebiedsindelingen/2024/wfs/v1_0?request=GetCapabilities&service=WFS