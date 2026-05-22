import matplotlib.pyplot as plt

def plot_point_distribution(
    points_gdf,
    district_gdf,
    lakes_gdf,
    title,
    output_path,
    color = "red",
    markersize = 1,
    alpha = 0.4,
    figsize = (6, 6),
):
    """
    Plots the raw point distribution of a GeoDataFrame overlaid on district boundaries.

    Parameters
    ----------
    points_gdf : geopandas.GeoDataFrame
        Point layer to plot.
    district_gdf : geopandas.GeoDataFrame
        District polygons used as background.
    lakes_gdf : geopandas.GeoDataFrame
        Lake polygons overlaid on the map.
    title : str
        Plot title.
    output_path : str
        File path to save the plot.
    color : str, optional
        Marker color. Default is "red".
    markersize : float, optional
        Marker size. Default is 1.
    alpha : float, optional
        Marker transparency. Default is 0.4.
    figsize : tuple, optional
        Figure size. Default is (6, 6).
    """
    
    fig, ax = plt.subplots(figsize = figsize)

    # District polygons as background
    district_gdf.plot(ax = ax, color = "whitesmoke", linewidth = 0.5, zorder = 1)
    # Plot points on top
    points_gdf.plot(ax = ax, color = color, markersize = markersize, alpha = alpha, zorder = 2)
    # District boundaries on top of points for visual clarity
    district_gdf.boundary.plot(ax = ax, color = "black", linewidth = 0.5, zorder = 3)
    # Lake on top to mask water areas
    lakes_gdf.plot(ax = ax, color = "skyblue", zorder = 4)

    ax.axis("off")
    ax.set_title(title, fontsize = 15)

    plt.tight_layout()
    plt.savefig(output_path, dpi = 300, bbox_inches = "tight")
    plt.show()