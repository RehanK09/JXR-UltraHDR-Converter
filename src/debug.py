from pathlib import Path


def save_report(stats, output):

    output = Path(output)

    output.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(output, "w") as f:

        for k, v in stats.items():

            f.write(f"{k}: {v}\n")