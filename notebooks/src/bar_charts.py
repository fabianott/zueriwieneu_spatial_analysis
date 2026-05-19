import matplotlib.pyplot as plt

def plot_bar(
    series,          # e.g. reports_gdf["year"].value_counts()
    title,
    xlabel,
    ylabel,
    output_path,
    figsize=(10, 5),
    color="skyblue",
    sort_index=False,  
):
    fig, ax = plt.subplots(figsize=figsize)
    
    if sort_index:
        series = series.sort_index()
    
    series.plot(kind="bar", ax=ax, color=color)
    
    ax.set_title(title, fontsize=15)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.show()