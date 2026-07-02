import numpy as np

def analyze(img):

    rgb = img[...,0:3]

    return {

        "minimum": float(rgb.min()),

        "maximum": float(rgb.max()),

        "mean": float(rgb.mean()),

        "median": float(np.median(rgb)),

        "p90": float(np.percentile(rgb,90)),

        "p95": float(np.percentile(rgb,95)),

        "p99": float(np.percentile(rgb,99))

    }


def is_hdr(img):

    return img[...,0:3].max() > 1.0