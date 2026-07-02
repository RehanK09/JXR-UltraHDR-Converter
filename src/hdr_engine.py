import numpy as np

from src.image_processing import analyze


class HDREngine:

    def __init__(self):

        self.stats = None

    def load(self, img):

        img = img.astype(np.float32)

        self.stats = analyze(img)

        return img

    def normalize(self, img):

        rgb = img[..., :3]

        rgb = np.clip(rgb, 0.0, None)

        img[..., :3] = rgb

        return img

    def get_stats(self):

        return self.stats