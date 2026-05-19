import matplotlib.pyplot as plt

def plot_point_distribution(
    points_gdf,
    district_gdf,
    lakes_gdf,
    title,
    output_path,
    color="red",
    markersize=1,
    alpha=0.4,
    figsize=(6, 6),
):
    fig, ax = plt.subplots(figsize=figsize)

    district_gdf.plot(ax=ax, color="whitesmoke", linewidth=0.5, zorder=1)
    points_gdf.plot(ax=ax, color=color, markersize=markersize, alpha=alpha, zorder=2)
    district_gdf.boundary.plot(ax=ax, color="black", linewidth=0.5, zorder=3)
    lakes_gdf.plot(ax=ax, color="skyblue", zorder=4)

    ax.axis("off")
    ax.set_title(title, fontsize=15)

    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.show()