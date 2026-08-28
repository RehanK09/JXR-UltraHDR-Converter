# JXR UltraHDR Converter

A simple one-click Windows utility for converting `.jxr` image files into `.png` files while preserving important file metadata, timestamps, and filenames.

Designed for a clean, automated workflow: drop your `.jxr` files into the **Input** folder, run `RUN.bat`, and let the converter handle the rest.

---

## ✨ Features

- ⚡ **One-Click Conversion**  
  Run `RUN.bat` to automatically process all supported `.jxr` files.

- 📁 **Simple Input → Output Workflow**  
  Place `.jxr` files inside the `Input` folder and find the converted files in the output location after processing.

- 🔄 **Batch Processing**  
  Process multiple image files automatically without converting them one by one.

- 🧠 **Duplicate Conversion Prevention**  
  Uses JSON-based tracking to keep a record of previously processed files and avoid converting the same input again.

- 🕒 **Metadata Preservation**  
  Preserves important original information such as filenames, timestamps, and supported metadata during processing.

- 🪟 **Windows-Friendly**  
  No complicated command-line workflow required. Simply run the included batch file.

---

## 📂 Project Structure

```text
JXR-UltraHDR-Converter/
│
├── Input/                 # Place your .jxr files here
│
├── src/                   # Source code and processing logic
│
├── ultrahdr/              # Core Ultra HDR binary/configuration files
│
├── README.md
├── RUN.bat                # One-click application launcher
├── requirements.txt       # Python dependencies
└── .gitignore
