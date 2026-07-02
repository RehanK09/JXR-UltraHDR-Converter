import json
from pathlib import Path
from datetime import datetime

TRACKER = Path("Logs/tracker.json")


class Tracker:

    def __init__(self):

        TRACKER.parent.mkdir(exist_ok=True)

        if not TRACKER.exists():
            TRACKER.write_text("{}")

        try:
            text = TRACKER.read_text().strip()

            if text == "":
                text = "{}"

            self.data = json.loads(text)

        except Exception:

            self.data = {}

            TRACKER.write_text("{}")

    def done(self, name):

        return name in self.data

    def mark(self, name):

        self.data[name] = {
            "status": "done",
            "time": datetime.now().isoformat()
        }

        TRACKER.write_text(
            json.dumps(
                self.data,
                indent=4
            )
        )