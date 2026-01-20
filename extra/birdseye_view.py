import cv2
import numpy as np

def birdseye_transform(image, src_points, dst_points, size):
    matrix = cv2.getPerspectiveTransform(src_points, dst_points)
    warped = cv2.warpPerspective(image, matrix, size)
    return warped