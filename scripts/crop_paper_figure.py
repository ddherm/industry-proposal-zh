"""Export a PDF page, or a figure within it, using normalized display coordinates."""

import argparse
import math
from pathlib import Path

import pypdfium2 as pdfium


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--page", required=True, type=int, help="PDF page number, starting at 1")
    parser.add_argument("--box", type=float, nargs=4, metavar=("LEFT", "TOP", "RIGHT", "BOTTOM"),
                        default=(0, 0, 1, 1), help="Edges as fractions of the visible page")
    parser.add_argument("--dpi", type=int, default=300)
    parser.add_argument("--out", type=Path, required=True, help="New output PNG filename")
    args = parser.parse_args()

    left, top, right, bottom = args.box
    if not (0 <= left < right <= 1 and 0 <= top < bottom <= 1):
        parser.error("Box edges must be ordered and within 0..1.")
    if args.dpi < 1:
        parser.error("DPI must be a positive integer.")
    if args.out.suffix.lower() != ".png":
        parser.error("Output must be a PNG file.")

    with pdfium.PdfDocument(args.pdf) as document:
        if not 1 <= args.page <= len(document):
            parser.error(f"Choose a page from 1 to {len(document)}.")
        page = document[args.page - 1]
        width, height = page.get_size()
        scale = args.dpi / 72
        # Render only the selection. PDFium expects trim amounts from the four edges.
        crop = (left * width, (1 - bottom) * height, (1 - right) * width, top * height)
        if (math.ceil(width * scale) <= math.ceil(crop[0] * scale) + math.ceil(crop[2] * scale)
                or math.ceil(height * scale) <= math.ceil(crop[1] * scale) + math.ceil(crop[3] * scale)):
            parser.error("The selected area is smaller than a pixel at this DPI.")
        bitmap = page.render(scale=scale, crop=crop)
        with bitmap.to_pil() as image:
            try:
                output = args.out.open("xb")
            except FileExistsError:
                parser.error(f"Output already exists: {args.out}")
            with output:
                image.save(output, format="PNG", dpi=(args.dpi, args.dpi))


if __name__ == "__main__":
    main()
