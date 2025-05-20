# Import for plotting and styles
import matplotlib.pyplot as plt


def _subplots(
    col_width: float,
    col_height: float,
    nrows: int = 1,
    ncols: int = 1,
    double_column: bool = False,
    sharex=False,
    sharey=False,
    squeeze=True,
    width_ratio=None,
    height_ratio=None,
    elongate=None,
    subplot_kw=None,
    gridspec_kw=None,
    **fig_kw,
):
    """
    Create a styled figure and a set of subplots using the given style and column dimensions.

    Parameters
    ----------
    col_width : float
        Width of a single column in inches.
    col_height : float
        Height of a single column in inches.
    ...same parameters as matplotlib.pyplot.subplots...
    """
    fig, axs = plt.subplots(
        nrows,
        ncols,
        sharex=sharex,
        sharey=sharey,
        squeeze=squeeze,
        width_ratios=width_ratio,
        height_ratios=height_ratio,
        subplot_kw=subplot_kw,
        gridspec_kw=gridspec_kw,
        **fig_kw,
    )
    # If figsize not provided, set based on column dims
    if "figsize" not in fig_kw:
        fig.set_size_inches(
            col_width * (2 if double_column else 1),
            col_height if elongate is None else elongate * col_height,
        )

    return fig, axs
