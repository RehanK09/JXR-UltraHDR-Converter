import numpy as np


def analyze(img):

    rgb = img[..., :3]

    rgb = rgb.astype(np.float32)

    lum = (
        rgb[..., 0] * 0.2126 +
        rgb[..., 1] * 0.7152 +
        rgb[..., 2] * 0.0722
    )

    stats = {}

    stats["minimum"] = float(rgb.min())
    stats["maximum"] = float(rgb.max())

    stats["mean"] = float(rgb.mean())
    stats["median"] = float(np.median(rgb))

    stats["p90"] = float(np.percentile(rgb, 90))
    stats["p95"] = float(np.percentile(rgb, 95))
    stats["p99"] = float(np.percentile(rgb, 99))

    stats["lum_mean"] = float(lum.mean())
    stats["lum_median"] = float(np.median(lum))

    stats["dark_ratio"] = float(np.mean(lum < 0.02))
    stats["bright_ratio"] = float(np.mean(lum > 1.0))

    stats["dynamic_range"] = float(
        np.percentile(lum, 99.9) /
        max(np.percentile(lum, 1), 0.00001)
    )

    return stats


def is_hdr(img):

    return img[..., :3].max() > 1.0

def luminance(rgb):

    return (
        rgb[...,0]*0.2126 +
        rgb[...,1]*0.7152 +
        rgb[...,2]*0.0722
    )


def normalize_luminance(rgb):

    lum = luminance(rgb)

    scale = np.divide(
        1.0,
        np.maximum(lum,0.00001)
    )

    return rgb, lum, scale