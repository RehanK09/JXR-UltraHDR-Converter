def classify(stats):

    if stats["bright_ratio"]>0.25:
        return "Bright HDR"

    if stats["dark_ratio"]>0.70:
        return "Dark HDR"

    return "Mixed HDR"