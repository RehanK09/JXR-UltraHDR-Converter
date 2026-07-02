from pathlib import Path
import subprocess
import tempfile
import shutil
import numpy as np

from src.config import ULTRAHDR_EXE


class UltraHDR:

    def __init__(self):

        self.exe = Path(ULTRAHDR_EXE)

        if not self.exe.exists():
            raise FileNotFoundError(
                f"UltraHDR executable not found:\n{self.exe}"
            )

    def write_half_float(self, img):

        temp = Path(tempfile.mktemp(suffix=".raw"))

        img.astype(np.float16).tofile(temp)

        return temp

    def encode(
        self,
        img,
        width,
        height,
        output
    ):

        raw = self.write_half_float(img)

        output = Path(output)

        cmd = [

            str(self.exe),

            "-m","0",

            "-p",str(raw),

            "-a","4",

            "-t","0",

            "-C","1",

            "-w",str(width),

            "-h",str(height),

            "-q","100",

            "-Q","100",

            "-D","1",

            "-z",str(output)

        ]

        result = subprocess.run(

            cmd,

            capture_output=True,

            text=True

        )

        raw.unlink(missing_ok=True)

        if result.returncode != 0:

            raise RuntimeError(result.stderr)

        return output.exists()