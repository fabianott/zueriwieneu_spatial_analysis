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
    Plots a bar chart from a pandas Series and saves it to the specified output path.

    Parameters
    ----------
    series : pandas.Series
        Data to plot.
    title : str
        Plot title.
    xlabel : str
        Label for the x-axis.
    ylabel : str
        Label for the y-axis.
    output_path : str or pathlib.Path
        File path to save the plot.
    figsize : tuple, optional
        Figure size. Default is (10, 5).
    color : str, optional
        Bar color. Default is "skyblue".
    sort_index : bool, optional
        Whether to sort the Series by index before plotting. Default is False.
    """

    fig, ax = plt.subplots(figsize=figsize)
    
    # Sort by index for time-based series (e.g. years)
    if sort_index:
        series = series.sort_index()
    
    # Plot as bar chart
    series.plot(kind = "bar", ax = ax, color = color)
    
    ax.set_title(title, fontsize = 15)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi = 300, bbox_inches = "tight")
    plt.show()