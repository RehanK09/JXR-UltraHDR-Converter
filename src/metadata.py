from pathlib import Path
import os
import shutil


def copy_file_times(src, dst):
    src = Path(src)
    dst = Path(dst)

    stat = src.stat()

    os.utime(
        dst,
        (stat.st_atime, stat.st_mtime)
    )


def copy_metadata(src, dst):
    try:
        shutil.copystat(src, dst)
    except Exception:
        pass