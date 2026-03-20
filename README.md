<div align="center">
  
# 🚗 Automatic Number Plate Recognition (ANPR)

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8.0-green)
![Status](https://img.shields.io/badge/Status-Complete-success)

A complete, stage-by-stage Automatic Number Plate Recognition extraction pipeline based strictly on classical computer vision methods and Tesseract OCR. This project follows a robust six-stage pipeline perfectly suited for real-world deployments such as Rwandan vehicle plate extraction, parking systems, and toll booths.

**Note on Testing Screenshots:** Due to the lack of available live traffic and stationary cars in the developmental environment, we were unable to capture real-world pipeline execution screenshots on actual plates. The testing phase supports live cameras or pre-recorded videos to validate extraction manually.

</div>

---

## 📖 The Architecture Pipeline

The project relies on geometric properties and strict OCR validation mechanisms to ensure robust extraction without necessarily adopting heavy deep learning models. The system strictly processes through these stages:

### 1️⃣ Detection (`src/detect.py`)
Finds image regions that possess the geometric structure of a plate (rectangular, dense contours, known aspect ratio bounds).

### 2️⃣ Alignment (`src/align.py`)
After identifying candidates, we apply perspective warping to transform the quadrangle contours into a flattened, level rectangle, minimizing rotational skew for OCR.

### 3️⃣ OCR Extraction (`src/ocr.py`)
Uses PyTesseract with explicit whitelists (`psm 8`, `oem 3`, uppercase alphanumeric boundaries) to read characters directly off the flattened candidate.

### 4️⃣ Regex Validation (`src/validate.py`)
Tests OCR output strings against known plate patterns. Designed effectively for African layout models like standard Rwandan sequences: `[A-Z]{3}[0-9]{3}[A-Z]`.

### 5️⃣ Temporal Confirmation & CSV Save (`src/temporal.py`)
Reads a live buffer across multiple frames to suppress "OCR flicker." It performs majority voting to confirm a plate number continuously over time. Finally, the confirmed string is logged efficiently inside `data/plates.csv`.

---

## 🚀 Getting Started

### 1. Requirements

Ensure you have Tesseract installed on your base OS (`sudo apt install tesseract-ocr` on Linux), then install the python libraries into your environment:

```bash
pip install -r requirements.txt
```

### 2. Running Live or on Pre-Recorded Files

All scripts can run in two modes:

* **Live Webcam Input (Default)**
  ```bash
  python -m src.temporal
  ```

* **Pre-Recorded Video / Edge Testing**
  You can pass any relative or absolute video path directly via the CLI:
  ```bash
  python -m src.temporal testing_footage.mp4
  ```

This optional video argument bypasses `0` to instantly process pre-recorded field evidence!
