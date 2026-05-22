import geopandas as gpd
import matplotlib.pyplot as plt

def plot_choropleth(
    points_gdf,        # point layer
    district_gdf,      # districts as polygones
    lakes_gdf,         # lake
    title,             
    legend_label,      
    output_path,       # e.g. "../outputs/waste_choropleth.png"
    cmap = "Reds",
    figsize=(7, 6),
    filter_column = None,   
    filter_value = None
):
    """
    Aggregates point data to district level and plots a choropleth map.

    Parameters
    ----------
    points_gdf : geopandas.GeoDataFrame
        Point layer to aggregate.
    district_gdf : geopandas.GeoDataFrame
        District polygons with name and area_km2 columns.
    lakes_gdf : geopandas.GeoDataFrame
        Lake polygons overlaid on the map.
    title : str
        Plot title.
    legend_label : str
        Label for the colorbar.
    output_path : str
        File path to save the plot.
    cmap : str, optional
        Matplotlib colormap. Default is "Reds".
    figsize : tuple, optional
        Figure size. Default is (7, 6).
    filter_column : str, optional
        Column name to filter points_gdf before aggregation.
    filter_value : str, optional
        Value to filter on in filter_column.

    Returns
    -------
    geopandas.GeoDataFrame
        District polygons with count and density columns.
    """

   # Optional: filter points before aggregation (e.g. only waste reports)
    gdf = points_gdf.copy()
    if filter_column and filter_value:
        gdf = gdf[gdf[filter_column] == filter_value]
   
    # Spatial Join and Aggregation per district
    joined = gpd.sjoin(gdf, district_gdf, how = "inner", predicate = "within") # points not being in a polygone are discarded
    counts = joined.groupby("name").size().reset_index(name="count") # reset.index makes normal df and names column

    # Merge counts back to district polygons
    # how="left" keeps districts with zero points (filled with NaN → 0)
    result = district_gdf.merge(counts, on = "name", how = "left") 
    result["count"] = result["count"].fillna(0)

    # Normalize by area to get density (reports per km²)
    result["density"] = result["count"] / result["area_km2"]

    # Plot choropleth map
    fig, ax = plt.subplots(figsize=figsize)

    result.plot(
        column = "density",
        cmap = cmap,
        legend = True,
        legend_kwds = {"label": legend_label},
        edgecolor = "black",
        linewidth = 0.5,
        ax = ax,
    )

    # Overlay lake on top to mask water areas
    lakes_gdf.plot(ax = ax, color = "skyblue", zorder = 2)
    ax.set_title(title, fontsize = 15)
    ax.axis("off")

    plt.tight_layout()
    plt.savefig(output_path, dpi = 300, bbox_inches = "tight")
    plt.show()

    return result  # later used for further analysis