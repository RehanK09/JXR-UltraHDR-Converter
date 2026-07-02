from pathlib import Path
from PIL import Image
import numpy as np

from src.config import INPUT_DIR
from src.config import OUTPUT_DIR

from src.converter import load_jxr


def main():

    OUTPUT_DIR.mkdir(exist_ok=True)

    files = list(INPUT_DIR.glob("*.jxr"))

    if not files:
        print("No JXR files.")
        return

    img, engine = load_jxr(files[0])

    rgb = np.clip(img[..., :3], 0, 1)

    rgb = (rgb * 255).astype(np.uint8)

    Image.fromarray(rgb).save(
        OUTPUT_DIR / "preview.png",
        optimize=True
    )

    print()

    print("=" * 60)

    for k, v in engine.get_stats().items():
        print(f"{k:20}: {v}")

    print("=" * 60)

    print()

    print("Preview saved.")


if __name__ == "__main__":
    main()