# JXR UltraHDR Converter

A simple one-click Windows utility for automatically converting `.jxr` image files into Ultra HDR image output.

Place your `.jxr` files inside the **Input** folder, run `RUN.bat`, and the converter automatically processes new files, tracks previously converted files, and saves the results to the **Output** folder.

---

## ✨ Features

* ⚡ **One-Click Conversion**
  Run `RUN.bat` to automatically process supported `.jxr` files.

* 📁 **Simple Input → Output Workflow**
  Place `.jxr` files inside the `Input` folder and receive converted files in the `Output` folder.

* 🔄 **Batch Processing**
  Automatically processes multiple `.jxr` files without requiring manual file-by-file conversion.

* 🧠 **Duplicate Conversion Prevention**
  Uses JSON-based tracking to identify files that have already been processed and prevents unnecessary duplicate conversions.

* 🕒 **Metadata Preservation**
  Preserves supported metadata, including original filenames and timestamps during processing.

* 🪟 **Windows-Friendly**
  Uses a simple batch file launcher, so the converter can be started by double-clicking `RUN.bat`.

* 📦 **Portable Project Structure**
  The project is designed to locate its required UltraHDR executable from within its own folder structure, allowing it to be moved and used from different locations.

---

## 📂 Project Structure

```text
JXR-UltraHDR-Converter/
│
├── Input/                  # Place .jxr files here
│
├── Output/                 # Converted files are saved here
│
├── Logs/                   # Conversion logs and tracking data
│   └── tracker.json
│
├── src/                    # Application source code
│
├── ultrahdr/               # UltraHDR executable and required files
│
├── RUN.bat                 # One-click launcher
│
├── requirements.txt        # Python dependencies
│
├── README.md
│
└── .gitignore
```

---

## 🛠️ Requirements

Before running the project, make sure you have:

* Windows
* Python installed
* The project dependencies installed

The required Python packages are:

* NumPy
* OpenCV
* Pillow
* ImageIO

---

## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/RehanK09/JXR-UltraHDR-Converter.git
```

Or download the repository as a ZIP file and extract it anywhere on your computer.

---

### 2. Open a Terminal Inside the Project Folder

Navigate to the project directory.

Example:

```bash
cd JXR-UltraHDR-Converter
```

---

### 3. Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

This installs all required Python packages automatically.

---

## ▶️ Usage

Using the converter is simple.

### Step 1 — Add Your JXR Files

Place your `.jxr` files inside:

```text
Input/
```

For example:

```text
Input/
├── Screenshot1.jxr
├── Screenshot2.jxr
└── Screenshot3.jxr
```

---

### Step 2 — Run the Converter

Double-click:

```text
RUN.bat
```

The application will automatically start processing the files.

---

### Step 3 — Automatic Processing

The converter follows this workflow:

```text
Input Folder
     │
     ▼
Detect .JXR Files
     │
     ▼
Check JSON Tracking Record
     │
     ├── Already Processed ──► Skip
     │
     ▼
Convert New Files
     │
     ▼
Preserve Supported Metadata
     │
     ▼
Save Converted Files
     │
     ▼
Output Folder
```

---

## 🧠 Smart Conversion Tracking

The application automatically keeps track of processed files using a JSON-based tracking system.

This prevents the same `.jxr` file from being unnecessarily converted again when the program is run multiple times.

Example:

```text
Input/
│
├── Screenshot1.jxr   → Already Converted → Skipped
├── Screenshot2.jxr   → Already Converted → Skipped
└── Screenshot3.jxr   → New File → Converted
```

The tracking data is created and updated automatically during normal operation.

---

## 🖼️ Metadata Preservation

During conversion, the project is designed to preserve supported information from the original files.

This includes:

* Original filenames
* Timestamps
* Supported image metadata

The goal is to retain useful information from the original image while making the converted output easier to use.

---

## ⚙️ How It Works

The project uses an automated processing pipeline:

```text
1. User adds .JXR files to Input/
              │
              ▼
2. User runs RUN.bat
              │
              ▼
3. Python application scans Input/
              │
              ▼
4. JSON tracker checks conversion history
              │
        ┌─────┴─────┐
        │           │
   Already Done    New File
        │           │
        ▼           ▼
      Skip       Convert
                    │
                    ▼
            Preserve Metadata
                    │
                    ▼
              Save to Output/
```

This allows multiple files to be processed automatically while avoiding duplicate conversions.

---

## 🧰 Technologies Used

* **Python**
* **NumPy**
* **OpenCV**
* **Pillow**
* **ImageIO**
* **JSON**
* **Windows Batch Scripting**
* **UltraHDR Processing Tools**

---

## 🚀 Example Workflow

After installing dependencies once:

```text
1. Add new .jxr screenshots to Input/
```

```text
2. Double-click RUN.bat
```

```text
3. The converter checks which files were already processed
```

```text
4. Previously converted files are skipped
```

```text
5. New files are automatically converted
```

```text
6. Converted files are saved to Output/
```

The JSON tracker is updated automatically for future runs.

---

## 🔮 Future Improvements

Possible future enhancements include:

* [ ] Drag-and-drop file support
* [ ] Graphical user interface
* [ ] Conversion progress indicator
* [ ] Support for additional output formats
* [ ] Custom output directory selection
* [ ] Detailed conversion logs
* [ ] Error reporting
* [ ] Custom conversion settings
* [ ] Standalone executable version

---

## 📌 Notes

* Place supported `.jxr` files inside the `Input` folder.
* Run `RUN.bat` to start the conversion process.
* Converted files are saved automatically to the `Output` folder.
* Previously processed files are tracked to avoid duplicate conversions.
* Do not remove or modify files inside the `ultrahdr` folder unless you know their purpose.
* Python dependencies only need to be installed once using:

```bash
pip install -r requirements.txt
```

---

## 👤 Author

**Rehan Khan**

GitHub: **[https://github.com/RehanK09](https://github.com/RehanK09)**

---

## ⭐ Support

If you find this project useful, consider giving the repository a star!
