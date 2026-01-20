# Object Detection and Distance Estimation for Robotics Navigation

**Author: Shahroze Baig**

---

## Project Overview

This project implements a camera-based perception pipeline for robotics navigation. The system detects navigation-relevant objects from monocular camera input and estimates their distance from the robot using geometric principles. The solution is designed with real-time performance and edge deployment in mind.

The project includes:

* Object detection using a pretrained deep learning model
* Monocular distance estimation using camera geometry
* Image and video inference pipelines
* Modular design suitable for robotics systems
* Optional advanced computer vision techniques for extra credit

---

## Key Features

* Real-time object detection using a lightweight YOLOv8n model
* Geometry-based distance estimation without depth sensors
* Supports both image and video inference
* Clean separation of detection, estimation, and visualization logic
* Portable pipeline that runs on local machines and cloud notebooks
* Designed with edge-device constraints in mind

---

## Objectives

* Detect navigation-relevant objects from camera input
* Estimate distance of detected objects from the robot (camera perspective)
* Annotate detections with class labels and distance estimates
* Support inference on both images and videos
* Maintain a clean, modular, and edge-aware implementation

---

## Approach Summary

### Object Detection

* Model: YOLOv8n (Ultralytics)
* Framework: PyTorch
* Pretrained on COCO for fast and reliable detection
* Suitable for real-time robotics applications

### Distance Estimation

Distance is estimated using the pinhole camera model:

Distance = (H_real × f) / H_pixel

Where:

* H_real is the real-world height of the object (assumed)
* f is the camera focal length
* H_pixel is the bounding box height in pixels

This provides a geometry-based approximation suitable for navigation and obstacle awareness.

---

## Dataset Usage

Images are sourced from the BDD100K driving dataset. Due to the large dataset size, exploration and experimentation were conducted using Kaggle Notebooks. Only a small representative subset of images and videos is downloaded locally for inference.

Dataset annotations are not required for inference since a pretrained detector is used.

---

## Project Structure

```
object-detection-distance-estimation/
│
├── notebooks/
│   └── bdd_yolov8_pipeline.ipynb
│
├── models/
│   └── yolov8n.pt
│
├── src/
│   ├── detector.py
│   ├── distance.py
│   ├── visualize.py
│   └── inference.py
│
├── extra/
│   ├── epipolar_geometry.py
│   ├── birdseye_view.py
│   └── optical_flow.py
│
├── data/
│   ├── images/
│   └── videos/
│
├── outputs/
│   ├── images/
│   └── videos/
│
├── configs/
│   └── camera.yaml
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## How to Run

### Install Dependencies

```
pip install -r requirements.txt
```

### Add Input Data

* Place images in: data/images/
* Place videos in: data/videos/

### Run Inference

```
python main.py
```

Annotated results will be saved to:

* outputs/images/
* outputs/videos/

---

## Image and Video Inference

* Images are processed individually with bounding boxes and distance labels
* Videos are processed frame-by-frame with real-time annotations
* Output videos preserve original resolution and FPS

---

## Extra Credit Implementations

The project includes optional advanced computer vision techniques relevant to robotics:

* Epipolar Geometry: Disparity-based depth estimation using feature matching
* Bird’s-Eye View Transformation: Perspective transform for navigation-friendly top-down mapping
* Optical Flow: Motion tracking of objects across consecutive frames

These modules are implemented in the extra directory.

---

## Edge and Performance Considerations

* Lightweight YOLOv8n model selected for real-time performance
* Suitable for CPU-only systems and embedded platforms
* Modular design allows easy quantization or backbone replacement
* Minimal memory footprint by avoiding full dataset downloads

---

## Assumptions and Limitations

* Distance estimation is approximate and based on assumed real-world object heights
* Camera intrinsic parameters are approximated using a fixed focal length
* Monocular estimation does not account for camera pitch or road slope
* Accuracy is sufficient for navigation awareness, not precise measurement

---

## Results and Outputs

* Annotated images with bounding boxes and distance labels
* Annotated videos with frame-by-frame detection and distance estimation
* Outputs are saved in organized directories for easy review

---

## Contact Information

Name: Shahroze Baig
Contact No: +91 9392713232
Email: [shahrozeb98@gmail.com]