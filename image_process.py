import cv2

def process_image(frame):
    frame = cv2.bilateralFilter(frame, 9, 75, 75)
    return frame



