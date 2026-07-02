import imagecodecs

from src.hdr_engine import HDREngine


def load_jxr(path):

    with open(path, "rb") as f:
        data = f.read()

    img = imagecodecs.jpegxr_decode(data)

    engine = HDREngine()

    img = engine.load(img)

    img = engine.process(img)

    return img, engine