"""This file is part of brailler, a simple tool to convert images to braille.

See README.md and LICENSE for more details.
"""


from typing import Callable

import argparse
import sys


from skimage import feature, filters, io, transform  # type: ignore

import numpy


from brailler import braille


EXIT_SUCCESS: int = 0
EXIT_FAILURE: int = 1

USAGE: str = """\
brailler [OPTIONS] [FILE...]

Convert images to braille.

OPTIONS
  -a, --algorithm canny|farid|laplace|luminance|prewitt|roberts|scharr|sobel
    Sets which algorithm to use in the edge detection (defaults to sobel)

  -t, --threshold NUMBER
    Sets which threshold should lit a dot in the braille output

  -s, --scale
    Scales image up or down to braille output

  -h, --help
    Displays this help text and then exits
"""


ALGORITHMS: dict[str, Callable] = {
    "canny": feature.canny,
    "farid": filters.farid,
    "laplace": filters.laplace,
    "luminance": (lambda img: img),  # luminance is dealt with threshold alone
    "prewitt": filters.prewitt,
    "roberts": filters.roberts,
    "scharr": filters.scharr,
    "sobel": filters.sobel,
}


def braillefy(file: str, algorithm: str,
              threshold: float, scale: float) -> str | None:
    """Converts input image to braille characters."""

    algorithm = algorithm.lower()

    if algorithm not in ALGORITHMS:
        algorithm = "sobel"

    image: numpy.ndarray = io.imread(file, as_gray=True)
    edgemap: numpy.ndarray = ALGORITHMS[algorithm](image)
    rescaled: numpy.ndarray = transform.rescale(edgemap, scale,
                                                anti_aliasing=False)
    filtered: numpy.ndarray = rescaled > threshold
    braillemat: numpy.ndarray | None = braille.matconvert(filtered)

    if braillemat is None:
        return ""

    stringfied: str | None = braille.stringfy(braillemat)

    return stringfied


def parse_argv(argv: list[str]) -> argparse.Namespace:
    """Parse arguments."""

    parser = argparse.ArgumentParser(usage=USAGE,
                                     add_help=False,
                                     allow_abbrev=False)

    parser.add_argument("-a", "--algorithm", default="sobel")
    parser.add_argument("-t", "--threshold", default="0.25")
    parser.add_argument("-s", "--scale", default="0.5")
    parser.add_argument("-h", "--help", action="store_true")

    parser.add_argument("files", metavar="FILE", type=str, nargs="+")

    return parser.parse_args(argv[1:])


def main(argv: list[str]) -> int:
    """Entry point."""

    options = parse_argv(argv)

    if options.help:
        print(USAGE, file=sys.stderr)

        return EXIT_FAILURE

    for file in options.files:
        try:
            output: str | None = braillefy(file, options.algorithm,
                                           float(options.threshold),
                                           float(options.scale))

            if output is None:
                print("Could not convert", file, file=sys.stderr)

        except (ValueError, TypeError) as error:
            if options.threshold is None:
                print("error: Threshold needs to be set.", file=sys.stderr)

            if options.scale is None:
                print("error: Scale needs to be set.", file=sys.stderr)

            print("error:", error, file=sys.stderr)

            return EXIT_FAILURE

        print(output)

    return EXIT_SUCCESS
