import cv2
import os
from src.detector import ObjectDetector
from src.distance import DistanceEstimator
from src.visualize import Visualizer

class InferencePipeline:
    def __init__(self, model_path, focal_length):
        self.detector = ObjectDetector(model_path)
        self.estimator = DistanceEstimator(focal_length)
        self.visualizer = Visualizer()
        self.class_names = self.detector.model.names

    def run_on_image(self, image_path, output_path):
        image = cv2.imread(image_path)
        detections = self.detector.detect(image)
        annotated = self.visualizer.draw(image, detections, self.estimator, self.class_names)
        cv2.imwrite(output_path, annotated)

    def run_on_video(self, video_path, output_path):
        cap = cv2.VideoCapture(video_path)

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            detections = self.detector.detect(frame)
            annotated = self.visualizer.draw(frame, detections, self.estimator, self.class_names)
            writer.write(annotated)

        cap.release()
        writer.release()