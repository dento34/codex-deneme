#!/usr/bin/env python3
"""Resize tarot card images to standard card dimensions.

This script loads images from an input directory, resizes them to the
classic Rider-Waite-Smith tarot card size (2.75" x 4.75" at 300 DPI) and
saves the results in an output directory. Smaller images are upscaled using
high-quality Lanczos resampling while preserving the original aspect ratio.
The images are centered on a white background to match the card dimensions.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Tuple

from PIL import Image, ImageOps

# Default card dimensions in pixels for 300 DPI (2.75" x 4.75")
DEFAULT_SIZE: Tuple[int, int] = (825, 1425)
DEFAULT_DPI = 300


def process_image(path: Path, output_dir: Path, size: Tuple[int, int], dpi: int) -> None:
    """Resize a single image and save it to ``output_dir``.

    Args:
        path: Path to the source image.
        output_dir: Directory to save the resized image.
        size: Target (width, height) in pixels.
        dpi: DPI metadata to embed in the saved image.
    """
    img = Image.open(path).convert("RGB")

    # Resize while maintaining aspect ratio
    contained = ImageOps.contain(img, size, method=Image.Resampling.LANCZOS)

    # Center the resized image on a white background matching the target size
    canvas = Image.new("RGB", size, "white")
    offset = ((size[0] - contained.width) // 2, (size[1] - contained.height) // 2)
    canvas.paste(contained, offset)

    output_dir.mkdir(parents=True, exist_ok=True)
    out_path = output_dir / path.name
    canvas.save(out_path, dpi=(dpi, dpi))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path("rider_waite_smith_cards"),
        help="Directory containing the original images",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("rws_cards_resized"),
        help="Directory to write the resized images",
    )
    parser.add_argument(
        "--width",
        type=int,
        default=DEFAULT_SIZE[0],
        help="Target card width in pixels (default: 825)",
    )
    parser.add_argument(
        "--height",
        type=int,
        default=DEFAULT_SIZE[1],
        help="Target card height in pixels (default: 1425)",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=DEFAULT_DPI,
        help="DPI metadata for the output images (default: 300)",
    )

    args = parser.parse_args()
    size = (args.width, args.height)

    if not args.input_dir.exists():
        raise SystemExit(f"Input directory not found: {args.input_dir}")

    for img_path in args.input_dir.iterdir():
        if img_path.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp", ".bmp"}:
            continue
        process_image(img_path, args.output_dir, size, args.dpi)


if __name__ == "__main__":
    main()
