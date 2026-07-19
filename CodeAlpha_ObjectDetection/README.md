# Object Detection and Tracking using YOLOv8 + SORT

## Overview

This project performs real-time object detection and tracking using a webcam or video.

YOLOv8 detects the objects.

SORT assigns a unique ID to every detected object.

---

## Features

- Real-time webcam detection
- Object Tracking
- Unique Tracking IDs
- Bounding Boxes
- YOLOv8
- SORT Tracker
- OpenCV

---

## Technologies

- Python
- OpenCV
- YOLOv8
- Ultralytics
- SORT

---

## Installation

Clone repository

```bash
git clone https://github.com/yourname/ObjectDetectionTracking.git
```

Install requirements

```bash
pip install -r requirements.txt
```

Download

```
yolov8n.pt
```

Place inside

```
models/
```

Run

```bash
python main.py
```

Press ESC to exit.

---

## Workflow

Video

↓

YOLO Detection

↓

Bounding Boxes

↓

SORT Tracking

↓

Tracking IDs

↓

Display Output

---

## Future Improvements

- DeepSORT
- Vehicle Counting
- Speed Estimation
- Face Recognition
- People Counting
- Parking Management
