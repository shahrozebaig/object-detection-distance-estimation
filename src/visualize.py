import cv2

class Visualizer:
    def draw(self, image, detections, estimator, class_names):
        for box in detections.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls_id = int(box.cls[0])
            cls_name = class_names[cls_id]
            pixel_height = y2 - y1
            distance = estimator.estimate(pixel_height, cls_name)
            if distance is not None:
                label = f"{cls_name}, {distance:.2f}m"
            else:
                label = cls_name
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, label, (x1, max(20, y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        return image