from pathlib import Path

# =====================================================
# PROJECT PATHS
# =====================================================

ROOT = Path(__file__).resolve().parent.parent

INPUT_DIR = ROOT / "Input"
OUTPUT_DIR = ROOT / "Output"
TEMP_DIR = ROOT / "Temp"
LOG_DIR = ROOT / "Logs"
DEBUG_DIR = ROOT / "Debug"

ULTRAHDR_DIR = ROOT / "ultrahdr"

ULTRAHDR_EXE = ULTRAHDR_DIR / "ultrahdr_app.exe"
METADATA_CFG = ULTRAHDR_DIR / "metadata.cfg"

# =====================================================
# IMAGE SETTINGS
# =====================================================

JPEG_QUALITY = 100
GAINMAP_QUALITY = 100

HDR_COLOR_GAMUT = "P3"

DEBUG = True

AUTO_EXPOSURE = True

AUTO_BLACK_POINT = True

AUTO_WHITE_POINT = True

LOCAL_CONTRAST = True

FILMIC = True

SAVE_SDR_PREVIEW = True

SAVE_HDR_STATS = True

# =====================================================