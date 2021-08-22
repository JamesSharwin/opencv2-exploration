import cv2
from fire import Fire

def capture_timelapse(max_images=2000, interval_ms=1000):

    vc = cv2.VideoCapture(0)
    if vc.isOpened():  # try to get the first frame
        rval, frame = vc.read()
        key = cv2.waitKey(1000)

    for i in range(max_images):
        rval, frame = vc.read()
        cv2.imwrite(f"raw_images/{str(i)}.png", frame)
        key = cv2.waitKey(interval_ms)
        if key == 27: # exit on ESC
            break


if __name__ == "__main__":
    Fire(capture_timelapse)