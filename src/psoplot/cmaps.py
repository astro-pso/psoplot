"""Custom colormaps for psoplot."""

from __future__ import annotations

from matplotlib.colors import LinearSegmentedColormap

midnight_ice = LinearSegmentedColormap.from_list(
    "midnight_ice",
    (
        # Edit this gradient at https://eltos.github.io/gradient/#000000-00AAB2-E7E4CA
        (0.000, (0.000, 0.000, 0.000)),
        (0.500, (0.000, 0.667, 0.698)),
        (1.000, (0.906, 0.894, 0.792)),
    ),
)

midnight_sand = LinearSegmentedColormap.from_list(
    "midnight_sand",
    (
        # Edit this gradient at https://eltos.github.io/gradient/#000000-00AAB2-F4EB9F
        (0.000, (0.000, 0.000, 0.000)),
        (0.500, (0.000, 0.667, 0.698)),
        (1.000, (0.957, 0.922, 0.624)),
    ),
)

azure_gold = LinearSegmentedColormap.from_list(
    "azure_gold",
    (
        # Edit this gradient at https://eltos.github.io/gradient/#1170F1-E7E4CA-FFF20D
        (0.000, (0.067, 0.439, 0.945)),
        (0.500, (0.906, 0.894, 0.792)),
        (1.000, (1.000, 0.949, 0.051)),
    ),
)

teal_rust = LinearSegmentedColormap.from_list(
    "teal_rust",
    (
        # Edit this gradient at https://eltos.github.io/gradient/#057B94-E7E4CA-A24909
        (0.000, (0.020, 0.482, 0.580)),
        (0.500, (0.906, 0.894, 0.792)),
        (1.000, (0.635, 0.286, 0.035)),
    ),
)

slate_amber = LinearSegmentedColormap.from_list(
    "slate_amber",
    (
        # Edit this gradient at https://eltos.github.io/gradient/#404040-E7E4CA-FFBA25
        (0.000, (0.251, 0.251, 0.251)),
        (0.500, (0.906, 0.894, 0.792)),
        (1.000, (1.000, 0.729, 0.145)),
    ),
)

blue_amber = LinearSegmentedColormap.from_list(
    "blue_amber",
    (
        # Edit this gradient at https://eltos.github.io/gradient/#0046BD-E7E4CA-D16B0A
        (0.000, (0.000, 0.275, 0.741)),
        (0.500, (0.906, 0.894, 0.792)),
        (1.000, (0.820, 0.420, 0.039)),
    ),
)

ember_cyan = LinearSegmentedColormap.from_list(
    "ember_cyan",
    (
        # Edit this gradient at https://eltos.github.io/gradient/#DA8B0A-000000-00A1FF
        (0.000, (0.855, 0.545, 0.039)),
        (0.500, (0.000, 0.000, 0.000)),
        (1.000, (0.000, 0.631, 1.000)),
    ),
)

aurora = LinearSegmentedColormap.from_list(
    "aurora",
    (
        # Edit this gradient at https://eltos.github.io/gradient/#0:00F9FF-30:0F0061-50:000000-70:804301-100:FFDC4E
        (0.000, (0.000, 0.976, 1.000)),
        (0.300, (0.059, 0.000, 0.380)),
        (0.500, (0.000, 0.000, 0.000)),
        (0.700, (0.502, 0.263, 0.004)),
        (1.000, (1.000, 0.863, 0.306)),
    ),
)

stormfire = LinearSegmentedColormap.from_list(
    "stormfire",
    (
        (0.000, (0.000, 0.976, 1.000)),
        (0.300, (0.000, 0.384, 1.000)),
        (0.500, (0.000, 0.000, 0.000)),
        (0.700, (0.824, 0.420, 0.000)),
        (1.000, (0.992, 0.835, 0.000)),
    ),
)

sun_ice = LinearSegmentedColormap.from_list(
    "sun_ice",
    (
        # Edit this gradient at https://eltos.github.io/gradient/#0:FFE048-25:DA8B0A-50:000000-75.4:00A1FF-100:66FFED
        (0.000, (1.000, 0.878, 0.282)),
        (0.250, (0.855, 0.545, 0.039)),
        (0.500, (0.000, 0.000, 0.000)),
        (0.754, (0.000, 0.631, 1.000)),
        (1.000, (0.400, 1.000, 0.929)),
    ),
)

rose_cream = LinearSegmentedColormap.from_list(
    "rose_cream",
    (
        # Edit this gradient at https://eltos.github.io/gradient/#000000-A26969-D1AD94-E9E9B8-FFFFFF
        (0.000, (0.000, 0.000, 0.000)),
        (0.250, (0.635, 0.412, 0.412)),
        (0.500, (0.820, 0.678, 0.580)),
        (0.750, (0.914, 0.914, 0.722)),
        (1.000, (1.000, 1.000, 1.000)),
    ),
)

viridis_plus = LinearSegmentedColormap.from_list(
    "viridis_plus",
    (
        (0.000, (0.267, 0.004, 0.329)),
        (0.200, (0.231, 0.322, 0.545)),
        (0.400, (0.129, 0.569, 0.549)),
        (0.600, (0.369, 0.788, 0.384)),
        (0.800, (0.992, 0.906, 0.145)),
        (1.000, (0.996, 1.000, 0.902)),
    ),
)

snowfall = LinearSegmentedColormap.from_list(
    "snowfall",
    (
        (0.000, (0.969, 0.988, 0.941)),
        (0.200, (0.800, 0.922, 0.773)),
        (0.400, (0.482, 0.800, 0.769)),
        (0.600, (0.169, 0.549, 0.745)),
        (0.800, (0.031, 0.251, 0.506)),
        (1.000, (0.000, 0.000, 0.000)),
    ),
)

blossom = LinearSegmentedColormap.from_list(
    "blossom",
    (
        (0.000, (0.000, 0.000, 0.000)),
        (0.125, (0.118, 0.000, 0.000)),
        (0.250, (0.482, 0.310, 0.310)),
        (0.375, (0.675, 0.435, 0.435)),
        (0.500, (0.788, 0.584, 0.533)),
        (0.625, (0.847, 0.749, 0.616)),
        (0.750, (0.898, 0.882, 0.690)),
        (0.875, (0.953, 0.953, 0.847)),
        (1.000, (1.000, 1.000, 1.000)),
    ),
)

magenta_cyan = LinearSegmentedColormap.from_list(
    "magenta_cyan",
    (
        (0.000, (0.627, 0.145, 0.569)),
        (0.250, (0.733, 0.290, 0.325)),
        (0.500, (1.000, 1.000, 1.000)),
        (0.750, (0.259, 0.659, 0.627)),
        (1.000, (0.133, 0.196, 0.557)),
    ),
)

purple_cyan = LinearSegmentedColormap.from_list(
    "purple_cyan",
    (
        (0.000, (0.549, 0.000, 0.682)),
        (0.250, (1.000, 0.000, 0.078)),
        (0.500, (1.000, 1.000, 1.000)),
        (0.750, (0.000, 1.000, 0.922)),
        (1.000, (0.133, 0.196, 0.557)),
    ),
)

neon_night = LinearSegmentedColormap.from_list(
    "neon_night",
    (
        # Edit this gradient at https://eltos.github.io/gradient/#FFFFFF-00FFFF-2AD4FF-55AAFF-8080FF-AA55FF-D42AFF-FF00FF-000000
        (0.000, (1.000, 1.000, 1.000)),
        (0.125, (0.000, 1.000, 1.000)),
        (0.250, (0.165, 0.831, 1.000)),
        (0.375, (0.333, 0.667, 1.000)),
        (0.500, (0.502, 0.502, 1.000)),
        (0.625, (0.667, 0.333, 1.000)),
        (0.750, (0.831, 0.165, 1.000)),
        (0.875, (1.000, 0.000, 1.000)),
        (1.000, (0.000, 0.000, 0.000)),
    ),
)

cividis_wide = LinearSegmentedColormap.from_list(
    "cividis_wide",
    (
        # Edit this gradient at https://eltos.github.io/gradient/#000000-00224E-2A3F6D-575D6D-7D7C78-A59C74-D2C060-FEE838-FFFFFF
        (0.000, (0.000, 0.000, 0.000)),
        (0.125, (0.000, 0.133, 0.306)),
        (0.250, (0.165, 0.247, 0.427)),
        (0.375, (0.341, 0.365, 0.427)),
        (0.500, (0.490, 0.486, 0.471)),
        (0.625, (0.647, 0.612, 0.455)),
        (0.750, (0.824, 0.753, 0.376)),
        (0.875, (0.996, 0.910, 0.220)),
        (1.000, (1.000, 1.000, 1.000)),
    ),
)

ember = LinearSegmentedColormap.from_list(
    "ember",
    (
        # Edit this gradient at https://eltos.github.io/gradient/#FFFFFF-FFF5F0-FDD4C2-FCA082-FB6A4A-E32F27-B21218-67000D-000000
        (0.000, (1.000, 1.000, 1.000)),
        (0.125, (1.000, 0.961, 0.941)),
        (0.250, (0.992, 0.831, 0.761)),
        (0.375, (0.988, 0.627, 0.510)),
        (0.500, (0.984, 0.416, 0.290)),
        (0.625, (0.890, 0.184, 0.153)),
        (0.750, (0.698, 0.071, 0.094)),
        (0.875, (0.404, 0.000, 0.051)),
        (1.000, (0.000, 0.000, 0.000)),
    ),
)

sunset = LinearSegmentedColormap.from_list(
    "sunset",
    (
        # Edit this gradient at https://eltos.github.io/gradient/#FFFFFF-FFFFCC-FFE692-FEBF5A-FD8D3C-F43D25-CA0923-800026-000000
        (0.000, (1.000, 1.000, 1.000)),
        (0.125, (1.000, 1.000, 0.800)),
        (0.250, (1.000, 0.902, 0.573)),
        (0.375, (0.996, 0.749, 0.353)),
        (0.500, (0.992, 0.553, 0.235)),
        (0.625, (0.957, 0.239, 0.145)),
        (0.750, (0.792, 0.035, 0.137)),
        (0.875, (0.502, 0.000, 0.149)),
        (1.000, (0.000, 0.000, 0.000)),
    ),
)

siesta = LinearSegmentedColormap.from_list(
    "siesta",
    (
        # Edit this gradient at https://eltos.github.io/gradient/#FFFFFF-FFFFD9-E0F3B2-97D6B9-41B6C4-1F80B8-24429B-081D58-000000
        (0.000, (1.000, 1.000, 1.000)),
        (0.125, (1.000, 1.000, 0.851)),
        (0.250, (0.878, 0.953, 0.698)),
        (0.375, (0.592, 0.839, 0.725)),
        (0.500, (0.255, 0.714, 0.769)),
        (0.625, (0.122, 0.502, 0.722)),
        (0.750, (0.141, 0.259, 0.608)),
        (0.875, (0.031, 0.114, 0.345)),
        (1.000, (0.000, 0.000, 0.000)),
    ),
)

icefire = LinearSegmentedColormap.from_list(
    "icefire",
    (
        (0.000, (0.153, 0.475, 0.812)),
        (0.330, (1.000, 0.094, 0.000)),
        (0.660, (1.000, 0.816, 0.247)),
        (1.000, (1.000, 1.000, 1.000)),
    ),
)

forest_dusk = LinearSegmentedColormap.from_list(
    "forest_dusk",
    (
        # Edit this gradient at https://eltos.github.io/gradient/#0:003C30-25:5BB3A8-50:F5F5F4-66.7:CEA053-83.3:834801-100:3A0061
        (0.000, (0.000, 0.235, 0.188)),
        (0.250, (0.357, 0.702, 0.659)),
        (0.500, (0.961, 0.961, 0.957)),
        (0.667, (0.808, 0.627, 0.325)),
        (0.833, (0.514, 0.282, 0.004)),
        (1.000, (0.227, 0.000, 0.380)),
    ),
)

COLORMAPS = {
    "midnight_ice": midnight_ice,
    "midnight_sand": midnight_sand,
    "azure_gold": azure_gold,
    "teal_rust": teal_rust,
    "slate_amber": slate_amber,
    "blue_amber": blue_amber,
    "ember_cyan": ember_cyan,
    "aurora": aurora,
    "stormfire": stormfire,
    "sun_ice": sun_ice,
    "rose_cream": rose_cream,
    "viridis_plus": viridis_plus,
    "snowfall": snowfall,
    "blossom": blossom,
    "magenta_cyan": magenta_cyan,
    "purple_cyan": purple_cyan,
    "neon_night": neon_night,
    "cividis_wide": cividis_wide,
    "ember": ember,
    "sunset": sunset,
    "siesta": siesta,
    "icefire": icefire,
    "forest_dusk": forest_dusk,
}


def list_colormaps() -> tuple[str, ...]:
    """Return the available colormap names."""

    return tuple(COLORMAPS.keys())


def get_colormap(name: str) -> LinearSegmentedColormap:
    """Return a colormap by name."""
    """Return a colormap by name.

    Raises
    ------
    ValueError
        If *name* is not one of the available colormaps. The error message
        includes the unknown name and the list of available colormap names.
    """

    try:
        return COLORMAPS[name]
    except KeyError as exc:
        available = ", ".join(sorted(list_colormaps()))
        raise ValueError(
            f"Unknown colormap {name!r}. Available colormaps are: {available}."
        ) from exc


__all__ = [
    "midnight_ice",
    "midnight_sand",
    "azure_gold",
    "teal_rust",
    "slate_amber",
    "blue_amber",
    "ember_cyan",
    "aurora",
    "stormfire",
    "sun_ice",
    "rose_cream",
    "viridis_plus",
    "snowfall",
    "blossom",
    "magenta_cyan",
    "purple_cyan",
    "neon_night",
    "cividis_wide",
    "ember",
    "sunset",
    "siesta",
    "icefire",
    "forest_dusk",
    "COLORMAPS",
    "list_colormaps",
    "get_colormap",
]
