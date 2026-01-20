import cv2
import numpy as np

def track_motion(prev_img, curr_img):
    prev_gray = cv2.cvtColor(prev_img, cv2.COLOR_BGR2GRAY)
    curr_gray = cv2.cvtColor(curr_img, cv2.COLOR_BGR2GRAY)
    points = cv2.goodFeaturesToTrack(prev_gray, maxCorners=100, qualityLevel=0.3, minDistance=7)
    next_points, status, _ = cv2.calcOpticalFlowPyrLK(prev_gray, curr_gray, points, None)
    motion = []
    for i in range(len(points)):
        if status[i]:
            motion.append((points[i][0], next_points[i][0]))
    return motion