class DistanceEstimator:
    def __init__(self, focal_length):
        self.focal_length = focal_length
        self.real_heights = {
            "person": 1.7,
            "car": 1.5,
            "traffic light": 1.0,
            "stop sign": 0.75
        }

    def estimate(self, pixel_height, class_name):
        if class_name not in self.real_heights:
            return None
        if pixel_height <= 0:
            return None
        return (self.real_heights[class_name] * self.focal_length) / pixel_height