import argparse


def main(extension="png") -> None:
    print("Making movie...")

    return


def cli():
    parser = argparse.ArgumentParser(description="Make a movie from a set of images.")

    parser.add_argument(
        "-e",
        "--extension",
        type=str,
        default="png",
        help="Extension of the images to be used.",
    )

    args = parser.parse_args()

    main(
        extension=args.extension,
    )


if __name__ == "__main__":
    cli()
