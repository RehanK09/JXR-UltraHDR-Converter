from pathlib import Path

from pathlib import Path
import json


def save_json(stats, path):

    Path(path).parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(path, "w") as f:

        json.dump(
            stats,
            f,
            indent=4
        )


def save_report(stats, output):

    output = Path(output)

    output.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with open(output, "w") as f:

        for k, v in stats.items():

            f.write(f"{k}: {v}\n")