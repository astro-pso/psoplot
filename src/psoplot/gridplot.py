import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

import psoplot

if matplotlib.__version__ < "3.7":
    import os

    plt.style.use(os.path.join(psoplot.__path__[0], "aanda_publication.mplstyle"))
else:
    plt.style.use("psoplot.aanda_publication")


class GridPlot:
    kwargs = {
        "margins": {
            "left": 0.125,
            "right": 0.1,
            "bottom": 0.11,
            "top": 0.12,
        },
        "wspace": 0.2,
        "hspace": 0.2,
        "spaces_in_inches": True,
    }

    def __init__(self, arg, fig_w=None, fig_h=None, **kwargs) -> None:
        """
        Generates axes grid for given aspect ratio array containing
        all aspect ratios of all individual axes and obeys either
        figureheight or figurewidth.

        Parameters:
        -----------
        arg : numpy array
            array of aspect ratios of the different axes
        fig_w : float, optional
            Figure width in inches, by default None
        fig_h : float, optional
            Figure height in inches, by default None

        Keyword Arguments:
        ------------------
        margins : dict, optional
            boarder margins for figure, by default
            {'left': 0.125, 'right' : 0.1, 'bottom' : 0.11, 'top' : 0.12}
        wspace : float, optional
            horizontal spaceing between axes in inches, by default 0.2
        hspace : float, optional
            vertical spacing between axes in inches, by default 0.2


        """

        self.num: int
        self.isarray = hasattr(arg, "shape") and not np.isscalar(arg)
        self.fig_w = fig_w
        self.fig_h = fig_h

        self.kwargs.update(kwargs)
        for key, value in list(self.kwargs.items()):
            setattr(GridPlot, key, value)

        if self.isarray:
            if len(arg.shape[:2]) == 1:
                self.arg = np.tile(arg, (1, 1))
            else:
                self.arg = arg

            self.shape = np.shape(arg)
            self.nr, self.nc = self.arg.shape[:2]

            if self.nc == 1:
                self.wspace = 0
            if self.nr == 1:
                self.hspace = 0

        else:
            self.arg = arg
            self.shape = (1,)
            self.nr = 1
            self.nc = 1

        if (fig_w is not None) and (fig_h is None):
            self.newsize, self.w_ratios, self.h_ratios = (
                self._getGridSpecForGivenAspectRatiosEqualHeight()
            )
        elif (fig_w is None) and (fig_h is not None):
            self.newsize, self.w_ratios, self.h_ratios = (
                self._getGridSpecForGivenAspectRatiosEqualWidth()
            )
        else:
            raise ValueError(
                "Invalid arguments: Either Figureheight or Figurewidth must be given..."
            )

        self._genGrid()

    def _getGridSpecForGivenAspectRatiosEqualHeight(self):
        ### make some checks here first....
        if self.isarray:
            h = np.ones_like(self.arg)

            if self.spaces_in_inches:
                fw_in_margin = self.fig_w * (
                    1.0 - self.margins["left"] - self.margins["right"]
                )
                wspace_abs = self.wspace
                self.wspace *= (
                    self.nc / fw_in_margin
                )  # -> this is later on used for creating the figure

            else:
                fw_in_margin = self.fig_w * (
                    1.0 - self.margins["left"] - self.margins["right"]
                )
                wspace_abs = fw_in_margin / self.nc * self.wspace

            fw_effective = fw_in_margin - wspace_abs

            h *= (fw_effective / np.sum(self.arg, axis=-1))[..., None]

            w = h * self.arg
            H = np.sum(h[:, 0])
            h_ratios = h / H
            w_ratios = w / fw_effective
            self.h = h
            self.w = w

            if self.spaces_in_inches:
                hspace_abs = self.hspace
                self.hspace = self.hspace / np.mean(h[:, 0])

            else:
                hspace_abs = np.mean(h[:, 0]) * self.hspace

            newsize = [
                self.fig_w,
                (H + hspace_abs) / (1.0 - self.margins["bottom"] - self.margins["top"]),
            ]

        else:
            h_ratios = 1
            w_ratios = 1
            newsize = [
                self.fig_w,
                (self.fig_w * (1.0 - self.margins["left"] - self.margins["right"]))
                * self.arg
                / (1.0 - self.margins["bottom"] - self.margins["top"]),
            ]

        return newsize, w_ratios, h_ratios

    def _getGridSpecForGivenAspectRatiosEqualWidth(self):
        ### make some checks here first....
        if self.isarray:
            w = np.ones_like(self.arg)
            fh_in_margin = self.fig_h * (
                1.0 - self.margins["bottom"] - self.margins["top"]
            )

            if self.spaces_in_inches:
                hspace_abs = self.hspace
                self.hspace = self.nr / fh_in_margin
            else:
                hspace_abs = self.fig_h / self.nr * self.hspace

            fh_effective = fh_in_margin - hspace_abs

            w *= (fh_effective / np.sum(1.0 / self.arg, axis=0))[None, ...]

            h = w / self.arg
            W = np.sum(w[0])
            h_ratios = h / fh_effective
            w_ratios = w / W
            self.h = h
            self.w = w

            if self.spaces_in_inches:
                wspace_abs = self.wspace
                self.wspace = self.wspace / np.mean(w[0])
            else:
                wspace_abs = np.mean(w[0]) * self.wspace

            newsize = [
                (W + wspace_abs) / (1.0 - self.margins["right"] - self.margins["left"]),
                self.fig_h,
            ]

        else:
            h_ratios = 1
            w_ratios = 1

            newsize = [
                self.fig_h
                * (1.0 - self.margins["top"] - self.margins["bottom"])
                / self.arg
                * (1 + self.margins["left"] + self.margins["right"]),
                self.fig_h,
            ]

        return newsize, w_ratios, h_ratios

    def _get_margins(self):
        rel_margins = {
            "left": self.margins["left"],
            "bottom": self.margins["bottom"],
            "right": (1.0 - self.margins["right"]),
            "top": (1.0 - self.margins["top"]),
        }
        return rel_margins

    def _genGrid(self):
        fig = plt.figure(figsize=self.newsize)
        fig.subplots_adjust(**self._get_margins())

        if self.isarray:
            if (self.fig_w is not None) and (self.fig_h is None):
                gs0 = gridspec.GridSpec(
                    self.nr,
                    1,
                    figure=fig,
                    height_ratios=self.h_ratios[:, 0],
                    hspace=self.hspace,
                )
                ### constructing grid for given figure width
                axs = []
                for i in range(self.nr):
                    gs = gridspec.GridSpecFromSubplotSpec(
                        1,
                        self.nc,
                        subplot_spec=gs0[i],
                        width_ratios=self.w_ratios[i],
                        wspace=self.wspace,
                    )
                    axs_i = []
                    for j in range(self.nc):
                        axs_i.append(fig.add_subplot(gs[j]))
                    axs.append(axs_i)

            elif (self.fig_w is None) and (self.fig_h is not None):
                gs0 = gridspec.GridSpec(
                    1,
                    self.nc,
                    figure=fig,
                    width_ratios=self.w_ratios[0],
                    wspace=self.wspace,
                )
                ### constructing grid for given figure width
                axs = []
                for j in range(self.nc):
                    gs = gridspec.GridSpecFromSubplotSpec(
                        self.nr,
                        1,
                        subplot_spec=gs0[j],
                        height_ratios=self.h_ratios[:, j],
                        hspace=self.hspace,
                    )
                    axs_j = []
                    for i in range(self.nr):
                        axs_j.append(fig.add_subplot(gs[i]))
                    axs.append(axs_j)

                axs = np.transpose(axs)

            else:
                raise ValueError(
                    "Invalid arguments: Either Figureheight or Figurewidth must be given..."
                )

        else:
            gs0 = gridspec.GridSpec(1, 1, figure=fig)
            axs = fig.add_subplot(gs0)

        self.fig = fig

        if self.nr == 1 or self.nc == 1:
            self.axs = np.asarray(axs).reshape(self.shape).flatten()

        else:
            self.axs = np.asarray(axs).reshape(self.shape)

    def getAxes(self):
        """
        Returns the figure and the axes objects
        """
        return self.fig, self.axs

    def merge_columns(self, idxr, idxc):
        """
        Merges columns of axes grid

        Parameters:
        -----------
        idxr : int
            index of row
        idxc : list
            list of indices of columns to be merged

        Returns:
        --------
        fig : matplotlib.figure.Figure
            figure object
        axs : numpy.ndarray
            array of axes objects
        """
        ###sanity checks:
        hasshape = np.logical_and.reduce(
            (
                isinstance(idxr, int),
                isinstance(idxc, list),
                all(isinstance(idx, int) for idx in idxc),
                len(idxc) == 2,
            )
        )
        if hasshape:
            if idxc[1] == -1:
                idxc[1] = self.nc
            if idxr == -1:
                idxr = self.nr - 1

            idxinrange = np.logical_and.reduce(
                (
                    idxr >= 0,
                    idxr < self.nr,
                    idxc[0] >= 0,
                    idxc[1] <= self.nc,
                )
            )

            if idxinrange and idxc[0] < idxc[1]:
                ismergingpossible = np.logical_and.reduce(
                    (
                        all(
                            [
                                height == self.h[idxr, idxc[0] : idxc[1]][0]
                                for height in self.h[idxr, idxc[0] : idxc[1]]
                            ]
                        ),
                        np.logical_or(self.nc > 1, self.nr > 1),
                    )
                )
                if ismergingpossible:
                    gs = self.axs[idxr, idxc[0]].get_gridspec()

                    for ax in self.axs[idxr, idxc[0] : idxc[1]].flatten():
                        ax.remove()

                    self.axs[idxr, idxc[0]] = self.fig.add_subplot(
                        gs[0, idxc[0] : idxc[1]]
                    )
                    return self.fig, self.axs
                else:
                    raise ValueError(
                        "Merging columns is not possible due to different axes heights"
                    )
            else:
                raise ValueError("Invalid Input: ToDo errormessage")
        else:
            raise ValueError(
                "Invalid Input: Given is idxr = {}, idxc={}.\n\tExpected is idxr = int and idxc=[int, int]".format(
                    idxr, idxc
                )
            )

    def merge_rows(self, idxr, idxc):
        """
        Merges rows of axes grid

        Parameters:
        -----------
        idxr : list
            list of indices of rows to be merged
        idxc : int
            index of column

        Returns:
        --------
        fig : matplotlib.figure.Figure
            figure object
        axs : numpy.ndarray
            array of axes objects
        """
        ###sanity checks:
        hasshape = np.logical_and.reduce(
            (
                isinstance(idxc, int),
                isinstance(idxr, list),
                all(isinstance(idx, int) for idx in idxr),
                len(idxr) == 2,
            )
        )
        if hasshape:
            if idxr[1] == -1:
                idxr = self.nr
            if idxc == -1:
                idxc = self.nc - 1

            idxinrange = np.logical_and.reduce(
                (
                    idxc >= 0,
                    idxc < self.nc,
                    idxr[0] >= 0,
                    idxr[1] <= self.nr,
                )
            )

            if idxinrange and idxr[0] < idxr[1]:
                ismergingpossible = np.logical_and.reduce(
                    (
                        all(
                            [
                                width == self.w[idxr[0] : idxr[1], idxc][0]
                                for width in self.w[idxr[0] : idxr[1], idxc]
                            ]
                        ),
                        np.logical_or(self.nc > 1, self.nr > 1),
                    )
                )
                if ismergingpossible:
                    gs = self.axs[idxr[0], idxc].get_gridspec()

                    for ax in self.axs[idxr[0] : idxr[1], idxc].flatten():
                        ax.remove()

                    self.axs[idxr[0], idxc] = self.fig.add_subplot(
                        gs[idxr[0] : idxr[1], 0]
                    )
                    return self.fig, self.axs
                else:
                    raise ValueError(
                        "Merging rows is not possible due to different axes widths"
                    )
            else:
                raise ValueError("Invalid Input: ToDo errormessage")
        else:
            raise ValueError(
                "Invalid Input: Given is idxr = {}, idxc={}.\n\tExpected is idxr = int and idxc=[int, int]".format(
                    idxr, idxc
                )
            )

    def merge(self, idxr, idxc):
        ###sanity checks:
        hasshape = np.logical_and.reduce(
            (
                isinstance(idxc, list),
                isinstance(idxr, list),
                all(isinstance(idx, int) for idx in idxr),
                all(isinstance(idx, int) for idx in idxc),
                len(idxr) == 2,
                len(idxc) == 2,
            )
        )
        if hasshape:
            if idxr[1] == -1:
                idxr = self.nr
            if idxc[1] == -1:
                idxc = self.nc

            idxinrange = np.logical_and.reduce(
                (
                    idxc[0] >= 0,
                    idxc[1] <= self.nc,
                    idxr[0] >= 0,
                    idxr[1] <= self.nr,
                    idxc[0] < idxc[1],
                    idxr[0] < idxr[1],
                )
            )

            if idxinrange:
                # ismergingpossible = np.logical_and.reduce((all([width==self.w[idxr[0]:idxr[1],idxc][0] for width in self.w[idxr[0]:idxr[1],idxc]]), np.logical_or(self.nc>1, self.nr>1)))
                ismergingpossible = True
                if ismergingpossible:
                    gs = self.axs[idxr[0], idxc[0]].get_gridspec()
                    for ax in self.axs[idxr[0] : idxr[1], idxc[0] : idxc[1]].flatten():
                        ax.remove()

                    print(idxr, idxc, gs[idxr[0] : idxr[1], idxc[0] : idxc[1]])
                    # self.axs[1,0] = self.fig.add_subplot(gs[1:,])
                    self.axs[idxr[0], idxc[0]] = self.fig.add_subplot(
                        gs[idxr[0] : idxr[1], idxc[0] : idxc[1]]
                    )

                    return self.fig, self.axs
                else:
                    raise ValueError(
                        "Merging rows is not possible due to different axes widths"
                    )
            else:
                raise ValueError("Invalid Input: ToDo errormessage")
        else:
            raise ValueError(
                "Invalid Input: Given is idxr = {}, idxc={}.\n\tExpected is idxr = int and idxc=[int, int]".format(
                    idxr, idxc
                )
            )
