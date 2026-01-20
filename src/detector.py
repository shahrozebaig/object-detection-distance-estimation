from ultralytics import YOLO
import cv2

class ObjectDetector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect(self, image):
        results = self.model(image)
        return results[0]