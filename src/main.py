from pathlib import Path

from src.config import INPUT_DIR
from src.converter import load_jxr


def main():

    files = list(INPUT_DIR.glob("*.jxr"))

    if not files:
        print("No JXR files found.")
        return

    img, engine = load_jxr(files[0])

    print("\n===== HDR Statistics =====")

    for k, v in engine.get_stats().items():
        print(f"{k:10} : {v}")

    print("==========================")

    print("Image Shape :", img.shape)

    print("Image Type  :", img.dtype)


if __name__ == "__main__":
    main()