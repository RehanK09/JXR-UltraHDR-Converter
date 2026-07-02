import numpy as np


class Calibration:

    def __init__(self):
        self.results = []

    def score(self, original, processed):

        o = original[..., :3].astype(np.float32)
        p = processed[..., :3].astype(np.float32)

        mse = np.mean((o - p) ** 2)

        mae = np.mean(np.abs(o - p))

        return {
            "mse": float(mse),
            "mae": float(mae)
        }