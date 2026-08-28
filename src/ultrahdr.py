from pathlib import Path
import subprocess
import tempfile
import numpy as np


class UltraHDR:

    def __init__(self):

        # Project root:
        # JXR-UltraHDR-Converter/
        project_root = Path(__file__).resolve().parent.parent

        # Search for ultrahdr_app.exe anywhere inside the project's
        # ultrahdr folder.
        ultrahdr_folder = project_root / "ultrahdr"

        matches = list(ultrahdr_folder.rglob("ultrahdr_app.exe"))

        if not matches:
            raise FileNotFoundError(
                "UltraHDR executable not found.\n\n"
                f"Expected it somewhere inside:\n"
                f"{ultrahdr_folder}\n\n"
                "Make sure ultrahdr_app.exe is included in the "
                "'ultrahdr' folder."
            )

        # Use the first matching executable
        self.exe = matches[0]

        print(f"Using UltraHDR executable:")
        print(self.exe)
        print()

    def write_half_float(self, img):

        temp = Path(tempfile.mktemp(suffix=".raw"))

        img.astype(np.float16).tofile(temp)

        return temp

    def encode(
        self,
        hdr,
        sdr,
        width,
        height,
        output
    ):

        raw = self.write_half_float(hdr)

        output = Path(output)

        cmd = [

            str(self.exe),

            "-m", "0",

            "-p", str(raw),

            "-a", "4",

            "-t", "0",

            "-C", "1",

            "-w", str(width),

            "-h", str(height),

            "-q", "100",

            "-Q", "100",

            "-D", "1",

            "-z", str(output)

        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        raw.unlink(missing_ok=True)

        if result.returncode != 0:

            raise RuntimeError(
                "UltraHDR conversion failed:\n\n"
                + result.stderr
            )

        return output.exists()
