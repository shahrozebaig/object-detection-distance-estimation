import cv2
import numpy as np

def estimate_depth(disparity, focal_length, baseline):
    if disparity <= 0:
        return None
    return (focal_length * baseline) / disparity

def compute_disparity(img1, img2):
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    disparities = []
    for m in matches:
        p1 = kp1[m.queryIdx].pt
        p2 = kp2[m.trainIdx].pt
        disparities.append(abs(p1[0] - p2[0]))
    if len(disparities) == 0:
        return None
    return np.mean(disparities)