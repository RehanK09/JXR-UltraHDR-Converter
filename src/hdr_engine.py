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

        img = img.astype(np.float32)

        return img

    def auto_exposure(self, img):
        return img

    def filmic(self, img):
        return img

    def recover_highlights(self, img):
        return img

    def recover_midtones(self, img):
        return img

    def preserve_blacks(self, img):
        return img

    def preserve_saturation(self, img):
        return img

    def process(self, img):

        img = self.normalize(img)

        return img