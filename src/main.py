from pathlib import Path

from PIL import Image

from src.converter import (
    load_jxr,
    encode_ultrahdr
)

INPUT = Path("Input")
OUTPUT = Path("Output")

OUTPUT.mkdir(exist_ok=True)

for file in INPUT.glob("*.jxr"):

    print(f"\nProcessing {file.name}")

    hdr, sdr, engine = load_jxr(file)

    h, w, _ = hdr.shape

    preview = (
        sdr[..., :3] * 255
    ).clip(0,255).astype("uint8")

    Image.fromarray(preview).save(
        OUTPUT / f"{file.stem}_preview.png"
    )

    encode_ultrahdr(
        hdr,
        sdr,
        OUTPUT / f"{file.stem}.jpg"
    )

    print("Done.")