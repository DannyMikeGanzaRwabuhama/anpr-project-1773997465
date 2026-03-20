# ANPR Project Pipeline

This repository implements an Automatic Number Plate Recognition (ANPR) pipeline strictly following the stages described in the course reference material:
**Detection -> Alignment -> OCR -> Validation -> Temporal -> Save**

## Pipeline Stages

1. **Detection** (`src/detect.py`)
   Finds plate candidates based on area, aspect ratio, and edge detection contours.
   ![Detection](screenshots/detect.jpg)

2. **Alignment** (`src/align.py`)
   Isolates the largest candidate bounding box and applies perspective transform to correctly warp and align the plate for OCR processing.
   ![Alignment](screenshots/align.jpg)

3. **OCR** (`src/ocr.py`)
   Uses PyTesseract to extract text from the thresholded and aligned plate image.
   ![OCR](screenshots/ocr.jpg)

4. **Validation** (`src/validate.py`)
   Validates the raw PyTesseract text against standard license plate formats using regular expressions (e.g., `[A-Z]{3}[0-9]{3}[A-Z]`).
   ![Validation](screenshots/validate.jpg)

5. **Temporal Validation & Save** (`src/temporal.py`)
   Maintains a short rolling buffer of frame outputs. Applies majority voting to confirm a plate number over sequential frames, eliminating OCR flicker or noise, and saves the confirmed output to `data/plates.csv`.
   ![Temporal Validation](screenshots/temporal.jpg)

## Running the Code

1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run any of the pipeline scripts to view the stage outputs sequentially. By default, it uses live camera `0`, but you can pass a path to a pre-recorded video:
   ```bash
   python src/temporal.py [optional_video_path.mp4]
   ```
