# OCR Screenshot Tool

This is a simple Python script that allows you to take a screenshot of a selected area on your screen, extract text from the screenshot using OCR, and copy the extracted text to your clipboard. It is designed to work on systems with an X11 window manager.

---

## Prerequisites

### System Requirements
- **Operating System**: Linux with X11 window manager
- **Required System Packages**:
  - `scrot` (for capturing screenshots)
  - `xclip` (for copying text to the clipboard)
  - `tesseract-ocr` (for performing OCR)

Install these dependencies using your package manager:

```bash
sudo apt update
sudo apt install scrot xclip tesseract-ocr
````

### Python Requirements

*   **Python Version**: Python 3.6 or newer
*   **Python Libraries**:
    *   `pillow`
    *   `pytesseract`
    *   `pyperclip`

Install these libraries using `pip`:

```bash
pip install -r requirements.txt
```

* * *

Installation
------------

1.  Clone the repository or download the script:
    
    ```bash
    git clone https://github.com/your-repo/ocr-screenshot-tool.git
    cd ocr-screenshot-tool
    ```
    
2.  Install Python dependencies:
    
    ```bash
    pip install -r requirements.txt
    ```
    
3.  Ensure the script is executable:
    
    ```bash
    chmod +x ocr_screenshot.py
    ```
    

* * *

Usage
-----

1.  Run the script:
    
    ```bash
    ./ocr_screenshot.py
    ```
    
2.  Use your mouse to select the area on the screen you want to capture.
    
3.  The script will:
    
    *   Save the screenshot temporarily to `/tmp/screenshot.png`.
    *   Extract text from the image using Tesseract OCR.
    *   Copy the extracted text to the clipboard.
4.  If successful, you’ll see the extracted text printed in the terminal and copied to your clipboard.
    

* * *

Example Output
--------------

When you select an area containing text like:

```
Hello, world!
```

The terminal will display:

```mathematica
Extracted Text:
Hello, world!
```

And the text will be available for pasting with `Ctrl+V`.

* * *

Customization
-------------

*   **Temporary File Path**: Modify the `screenshot_path` in the script to save the screenshot to a different location.
*   **Tesseract Options**: Customize Tesseract's OCR behavior by passing options to the `pytesseract.image_to_string()` function in the script.

* * *

Troubleshooting
---------------

*   **"scrot command not found"**: Install `scrot`:
    
    ```bash
    sudo apt install scrot
    ```
    
*   **"Tesseract not recognized"**: Ensure `tesseract-ocr` is installed:
    
    ```bash
    sudo apt install tesseract-ocr
    ```
    
*   **Permission Denied**: Ensure the script is executable:
    
    ```bash
    chmod +x ocr_screenshot.py
    ```
    
