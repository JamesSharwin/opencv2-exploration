import cv2
from fire import Fire
from image_process import process_image
import os

def capture_timelapse(max_images=2000, interval_ms=1000):


    indexes = [int(x.replace(".png", "")) for x in os.listdir("raw_images") if x.endswith(".png")]
    i = 0
    if indexes:
        i = max(indexes) + 1


    vc = cv2.VideoCapture(0)
    if vc.isOpened():  # try to get the first frame
        rval, frame = vc.read()
        key = cv2.waitKey(1000)

    while i < max_images:
        rval, frame = vc.read()
        frame = process_image(frame)
        cv2.imwrite(f"raw_images/{str(i)}.png", frame)
        key = cv2.waitKey(interval_ms)

        cv2.imshow("Capturing", frame)
        i += 1
        if key == 27: # exit on ESC
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    Fire(capture_timelapse)