import matplotlib.pyplot as plt


class SlicePlot:
    def __init__(self) -> None:
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect("equal")
        self.ax.set_axis_off()
        self.ax.set_xlim(-1, 1)
        self.ax.set_ylim(-1, 1)
        self.ax.set_xticks([])
        self.ax.set_yticks([])

    def plot(self, x, y, color="black") -> plt.Figure:
        self.ax.plot(x, y, color=color)
        return self.fig
