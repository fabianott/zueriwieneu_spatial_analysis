import geopandas as gpd
import matplotlib.pyplot as plt

def plot_choropleth(
    points_gdf,        # point layer
    district_gdf,      # districts as polygones
    lakes_gdf,         # lake
    title,             
    legend_label,      
    output_path,       # e.g. "../outputs/waste_choropleth.png"
    cmap="Reds",
    figsize=(7, 6),
    filter_column=None,   
    filter_value=None
):
    """Aggregates points to district density and plots a choropleth map. Returns the aggregated GeoDataFrame."""

    # Optinal Filter
    gdf = points_gdf.copy()
    if filter_column and filter_value:
        gdf = gdf[gdf[filter_column] == filter_value]
   
    # Spatial Join and Aggregation per district
    joined = gpd.sjoin(gdf, district_gdf, how="inner", predicate="within") # points not being in a polygone are discarded
    counts = joined.groupby("name").size().reset_index(name="count") # reset.index makes normal df and names column

    # 3. Merge and Normalization
    result = district_gdf.merge(counts, on="name", how="left") # points with no value are assigned with NaN
    result["count"] = result["count"].fillna(0)
    result["density"] = result["count"] / result["area_km2"]

    # 4. Plot
    fig, ax = plt.subplots(figsize=figsize)

    result.plot(
        column="density",
        cmap=cmap,
        legend=True,
        legend_kwds={"label": legend_label},
        edgecolor="black",
        linewidth=0.5,
        vmin=vmin,
        vmax=vmax,
        ax=ax,
    )

    lakes_gdf.plot(ax=ax, color="skyblue", zorder=2)
    ax.set_title(title, fontsize=15)
    ax.axis("off")

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.show()

    return result  # later used for further analysis