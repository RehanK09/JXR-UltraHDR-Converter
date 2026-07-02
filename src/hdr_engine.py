import numpy as np

from src.image_processing import analyze


class HDREngine:

    def __init__(self):

        self.stats = None

    def load(self, img):

        img = img.astype(np.float32)

        self.stats = analyze(img)

        return img

    def get_stats(self):

        return self.stats

    def normalize(self, img):

        img[..., :3] = np.clip(img[..., :3], 0, None)

        return img

    def auto_exposure(self, img):

        rgb = img[..., :3]

        target = 0.82

        exposure = target / max(self.stats["p95"], 0.001)

        rgb *= exposure

        img[..., :3] = rgb

        return img

    def filmic(self, img):

        rgb = img[..., :3]

        x = np.maximum(rgb - 0.004, 0.0)

        rgb = (x * (6.2 * x + 0.5)) / (x * (6.2 * x + 1.7) + 0.06)

        img[..., :3] = np.clip(rgb, 0, 1)

        return img

    def preserve_blacks(self, img):

        rgb = img[..., :3]

        mask = rgb < 0.08

        rgb[mask] *= 1.18

        img[..., :3] = rgb

        return img

    def process(self, img):

        img = self.normalize(img)

        img = self.auto_exposure(img)

        img = self.filmic(img)

        img = self.preserve_blacks(img)

        return img