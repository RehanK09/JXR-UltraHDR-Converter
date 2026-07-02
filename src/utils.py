from pathlib import Path

def ensure_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)

def filename(path):
    return Path(path).stem

def extension(path):
    return Path(path).suffix.lower()

def print_header(text):
    print()
    print("="*60)
    print(text)
    print("="*60)

def print_ok(text):
    print("[OK] ", text)

def print_error(text):
    print("[ERROR]", text)