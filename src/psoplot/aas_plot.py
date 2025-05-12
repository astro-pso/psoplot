# Plotting utilities for AAS paper, e.g. ApJ, ApJL, ApJS

import matplotlib.pyplot as plt

import psoplot

plt.style.use("psoplot.aas_publication")

AAS_COL_WIDTH = 242.7 / 72.27
AAS_COL_HEIGHT = 4.8 / 6.4 * AAS_COL_WIDTH


def subplots(
    nrows=1,
    ncols=1,
    double_column=False,
    sharex=False,
    sharey=False,
    squeeze=True,
    width_ratio=None,
    height_ratio=None,
    elongate=None,
    subplot_kw=None,
    gridspec_kw=None,
    **fig_kw,
) -> (plt.Figure, plt.Axes):
    """
    Create a figure and a set of subplots. Essentially a wrapper around
    `matplotlib.pyplot.subplots` with some additional functionality,
    such as selecting a single or double column width for the figure.

    Parameters
    ----------
    nrows : int, default: 1
        Number of rows of the subplot grid
    ncols : int, default: 1
        Number of columns of the subplot grid
    double_column : bool, default: False
        If True, the figure will be created with a width of two columns,
        otherwise with a width of one. Ignored if `fig_kw` contains a
        `figsize` key
    sharex : bool or {'none', 'all', 'row', 'col'}, default: False
        Controls sharing of properties among x (sharex=True),
        y (sharey=True) axes
    sharey : bool or {'none', 'all', 'row', 'col'}, default: False
        Controls sharing of properties among x (sharex=True),
        y (sharey=True) axes
    squeeze : bool, default: True
        If True, extra dimensions are squeezed out from the returned Axes object
    width_ratios : array-like of length *ncols*, optional
        Defines the relative widths of the columns. Each column gets a
        relative width of ``width_ratios[i] / sum(width_ratios)``.
        If not given, all columns will have the same width.  Equivalent
        to ``gridspec_kw={'width_ratios': [...]}``.
    height_ratios : array-like of length *nrows*, optional
        Defines the relative heights of the rows. Each row gets a
        relative height of ``height_ratios[i] / sum(height_ratios)``.
        If not given, all rows will have the same height. Equivalent
        to ``gridspec_kw={'height_ratios': [...]}``.
    elongate : float, default: None
        Vertical elongation factor. If None, the height is set to
        `AAS_COL_HEIGHT`. A value of 1 corresponds to the height of
        `AAS_COL_HEIGHT`. Ignored if `fig_kw` contains a `figsize` key
    subplot_kw : dict, default: None
        Dict with keywords passed to the `add_subplot` call used to create
        each subplot
    gridspec_kw : dict, default: None
        Dict with keywords passed to the `GridSpec` constructor used to create
        the grid the subplots are placed on
    fig_kw : dict, default: None
        Dict with keywords passed to the `figure` call

    Returns
    -------
    fig : `~matplotlib.figure.Figure`
        The created figure
    axs : array of `~matplotlib.axes.Axes`

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

    if "figsize" not in fig_kw:
        fig.set_size_inches(
            AAS_COL_WIDTH * (2 if double_column else 1),
            AAS_COL_HEIGHT if elongate is None else elongate * AAS_COL_HEIGHT,
        )

    return fig, axs
