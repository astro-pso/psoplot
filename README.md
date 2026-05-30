# psoplot
PSO Plotting Utils

## Installation
```bash
pip install psoplot
``````
## Usage

If you only want to use a style, you can use the following code:
```python
import matplotlib.pyplot as plt
import psoplot

plt.style.use("psoplot.aanda_publication")

# [Your plotting code here]

```

If you want to use e.g. a convenient wrapper for generating subplots, you can use the following code:
```python
import psoplot.aanda_plot as aplt

fig, (ax1, ax2) = aplt.subplots(2, 1)
```

Which is essentially a wrapper around ``plt.subplots`` with some convenience settings regarding the
size of the figure.

## Available styles
- `psoplot.aanda_publication`: A style for A&A publication
- `psoplot.aas_publication`: A style for AAS publication, e.g. ApJ, ApJL, ApJS

For example plots, see the (https://astro-pso.github.io/psoplot)[examples] page.

## CLI: make-movie

Use `make-movie` to build an MP4 from image frames sharing the same base name.

```bash
make-movie frame_ --extension png --fps 24 --output movie.mp4
```

The command searches for matching frames like `frame_*.<extension>` in the same directory,
sorts them, and runs `ffmpeg` to produce the MP4 file.
