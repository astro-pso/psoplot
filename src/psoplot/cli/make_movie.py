import argparse
import re
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Optional, Tuple


def _frame_sort_key(frame_path: Path) -> Tuple[str, int]:
    """Return a natural sort key for frames with optional numeric suffixes."""
    match = re.search(r"(\d+)$", frame_path.stem)
    if match is None:
        return (frame_path.stem, -1)

    return (frame_path.stem[: -len(match.group(1))], int(match.group(1)))


def _escape_ffmpeg_path(path: Path) -> str:
    """Escape path strings for safe use in ffmpeg concat list files."""
    return str(path).replace("'", r"'\''")


def main(
    base_image: str,
    extension: str = "png",
    output: Optional[str] = None,
    fps: float = 24.0,
) -> None:
    """Create an MP4 movie from matching image frames using ffmpeg."""
    if fps <= 0:
        raise ValueError("fps must be greater than 0.")

    base_path = Path(base_image)
    frame_dir = base_path.parent if base_path.parent != Path("") else Path(".")

    if base_path.suffix:
        extension = base_path.suffix.lstrip(".")
        base_name = base_path.stem
    else:
        base_name = base_path.name
        extension = extension.lstrip(".")

    frames = sorted(frame_dir.glob(f"{base_name}*.{extension}"), key=_frame_sort_key)
    if not frames:
        raise FileNotFoundError(
            f"No frames found for base image '{base_name}' with extension '{extension}' in '{frame_dir}'."
        )

    ffmpeg_path = shutil.which("ffmpeg")
    if ffmpeg_path is None:
        raise RuntimeError("ffmpeg was not found in PATH.")

    output_path = Path(output) if output else frame_dir / f"{base_name}.mp4"
    duration = 1 / fps

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".txt", delete=False
    ) as temp_file:
        for frame in frames:
            temp_file.write(f"file '{_escape_ffmpeg_path(frame.resolve())}'\n")
            temp_file.write(f"duration {duration}\n")
        temp_file.write(f"file '{_escape_ffmpeg_path(frames[-1].resolve())}'\n")
        temp_list_file = temp_file.name

    ffmpeg_cmd = [
        ffmpeg_path,
        "-y",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        temp_list_file,
        "-pix_fmt",
        "yuv420p",
        str(output_path),
    ]
    try:
        subprocess.run(ffmpeg_cmd, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as error:
        raise RuntimeError(
            "ffmpeg failed to create the movie. "
            f"stderr: {error.stderr.strip() if error.stderr else 'N/A'}"
        ) from error
    finally:
        Path(temp_list_file).unlink(missing_ok=True)

    print(f"Created '{output_path}' from {len(frames)} frame(s).")


def cli():
    parser = argparse.ArgumentParser(description="Make a movie from a set of images.")
    parser.add_argument(
        "base_image",
        type=str,
        help="Base image name (with or without extension), e.g. 'frame' or 'frame_0001.png'.",
    )

    parser.add_argument(
        "-e",
        "--extension",
        type=str,
        default="png",
        help="Extension of the images to be used.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default=None,
        help="Output movie path. Defaults to '<base_image>.mp4'.",
    )
    parser.add_argument(
        "--fps",
        type=float,
        default=24.0,
        help="Frames per second for the generated movie.",
    )

    args = parser.parse_args()

    main(
        base_image=args.base_image,
        extension=args.extension,
        output=args.output,
        fps=args.fps,
    )


if __name__ == "__main__":
    cli()
