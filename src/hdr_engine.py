import numpy as np
from src.image_processing import analyze
from src import tone_mapping

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
        p50 = self.stats["median"]
        p95 = self.stats["p95"]
        p99 = self.stats["p99"]
        target = 0.82

        exposure = target / max(p95, 0.01)

        if p99 > 4:
            exposure *= 0.92
        if p50 < 0.02:
            exposure *= 1.08

        rgb *= exposure
        img[..., :3] = rgb
        return img

    def filmic(self, img):
        rgb = img[..., :3]
        x = np.maximum(rgb - 0.004, 0.0)
        rgb = tone_mapping.aces(x)
        img[..., :3] = np.clip(rgb, 0, 1)
        return img
    
    def recover_highlights(self, img):
        rgb = img[..., :3]
        mask = rgb > 0.85
        rgb[mask] = 0.85 + np.tanh((rgb[mask] - 0.85) * 1.7) * 0.15
        img[..., :3] = rgb
        return img

    def recover_midtones(self, img):
        rgb = img[..., :3]
        mask = (rgb > 0.15) & (rgb < 0.75)
        rgb[mask] = np.power(rgb[mask], 0.93)
        img[..., :3] = rgb
        return img

    def preserve_blacks(self, img):
        rgb = img[..., :3]
        shadows = rgb < 0.10
        rgb[shadows] = np.power(rgb[shadows], 0.82)
        img[..., :3] = np.clip(rgb, 0, 1)
        return img

    def preserve_saturation(self, img):
        rgb = img[..., :3]
        gray = (
            rgb[..., 0] * 0.2126 +
            rgb[..., 1] * 0.7152 +
            rgb[..., 2] * 0.0722
        )
        gray = gray[..., None]
        amount = 1.08
        rgb = gray + (rgb - gray) * amount
        rgb = np.clip(rgb, 0, 1)
        img[..., :3] = rgb
        return img

    def process(self, img):
        img = self.normalize(img)
        img = self.auto_exposure(img)
        img = self.filmic(img)
        img = self.recover_highlights(img)
        img = self.recover_midtones(img)
        img = self.preserve_blacks(img)
        img = self.preserve_saturation(img)
        return img
