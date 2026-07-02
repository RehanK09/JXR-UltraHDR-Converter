from pathlib import Path

from PIL import Image

from src.metadata import copy_metadata, copy_file_times
from src.tracker import Tracker
from src.converter import load_jxr, encode_ultrahdr

INPUT = Path("Input")
OUTPUT = Path("Output")

OUTPUT.mkdir(exist_ok=True)

# Delete all old preview PNGs
for png in OUTPUT.glob("*_preview.png"):
    png.unlink(missing_ok=True)

tracker = Tracker()

for file in INPUT.glob("*.jxr"):

    if tracker.done(file.name):
        print(f"Skipping {file.name}")
        continue

    print(f"\nProcessing {file.name}")

    hdr, sdr, engine = load_jxr(file)

    preview = (
        sdr[..., :3] * 255
    ).clip(0, 255).astype("uint8")

    preview_path = OUTPUT / f"{file.stem}_preview.png"

    Image.fromarray(preview).save(preview_path)

    jpg_path = OUTPUT / f"{file.stem}.jpg"

    # Remove old jpg if it exists
    jpg_path.unlink(missing_ok=True)

    encode_ultrahdr(
        hdr,
        sdr,
        jpg_path
    )

    copy_metadata(
        file,
        jpg_path
    )

    copy_file_times(
        file,
        jpg_path
    )

    tracker.mark(file.name)

    # Preview is only temporary
    preview_path.unlink(missing_ok=True)

    print(f"✓ Finished {file.name}")

print("\n===================================")
print("All conversions completed.")
print("===================================")