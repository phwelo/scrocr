#!/usr/bin/env python3

import os
import subprocess
import pytesseract
from PIL import Image
import pyperclip

def capture_screenshot():
    """Capture a screenshot of a user-selected area using scrot."""
    screenshot_path = "/tmp/screenshot.png"
    print("Select the area for screenshot using your mouse...")
    
    # Use scrot to capture the selected area
    try:
        subprocess.run(["scrot", "-s", screenshot_path], check=True)
        return screenshot_path
    except subprocess.CalledProcessError:
        print("Screenshot selection canceled.")
        return None

def extract_text_from_image(image_path):
    """Extract text from an image using Tesseract OCR."""
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        print(f"Error during OCR: {e}")
        return None

def copy_to_clipboard(text):
    """Copy the extracted text to the clipboard using xclip."""
    try:
        subprocess.run(["xclip", "-selection", "clipboard"], input=text.encode(), check=True)
        print("Text copied to clipboard.")
    except Exception as e:
        print(f"Error copying to clipboard: {e}")

def main():
    # Capture a screenshot
    screenshot_path = capture_screenshot()
    if not screenshot_path:
        return
    
    # Extract text from the screenshot
    text = extract_text_from_image(screenshot_path)
    if text:
        print("Extracted Text:")
        print(text)
        # Copy text to clipboard
        copy_to_clipboard(text)
    else:
        print("No text could be extracted.")

if __name__ == "__main__":
    main()
