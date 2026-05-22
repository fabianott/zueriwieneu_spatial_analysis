import matplotlib.pyplot as plt

def plot_bar(
    series,          # e.g. reports_gdf["year"].value_counts()
    title,
    xlabel,
    ylabel,
    output_path,
    figsize = (10, 5),
    color = "skyblue",
    sort_index = False,  
):
    """
    Plots a 2x5 grid of yearly choropleth maps with a shared colorbar.

    Parameters
    ----------
    reports_district_gdf : geopandas.GeoDataFrame
        Spatially joined reports with district name and year columns.
    district_gdf : geopandas.GeoDataFrame
        District polygons with name and area_km2 columns.
    lakes_gdf : geopandas.GeoDataFrame
        Lake polygons overlaid on each map.
    output_path : str
        File path to save the plot.
    years : range, optional
        Years to include. Default is range(2016, 2026).
    """

    fig, ax = plt.subplots(figsize=figsize)
    
    if sort_index:
        series = series.sort_index()
    
    series.plot(kind = "bar", ax = ax, color = color)
    
    ax.set_title(title, fontsize = 15)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi = 300, bbox_inches = "tight")
    plt.show()