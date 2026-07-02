import imagecodecs

from src.hdr_engine import HDREngine
from src.ultrahdr import UltraHDR


def load_jxr(path):

    with open(path, "rb") as f:
        data = f.read()

    img = imagecodecs.jpegxr_decode(data)

    engine = HDREngine()

    hdr = engine.load(img.copy())

    sdr = engine.process(img.copy())

    return hdr, sdr, engine


def encode_ultrahdr(hdr, sdr, output):

    h, w, _ = hdr.shape

    UltraHDR().encode(
        hdr,
        sdr,
        w,
        h,
        output
    )