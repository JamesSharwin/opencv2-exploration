import cv2
import os
from fire import Fire
import shutil


BASE_PATH = 'raw_images'
KEY_FOLDER_MAP = {
    112: 'positive_images',
    110: 'negative_images',
    105: 'inconclusive_images'
}


def sort_images():
    for f in os.listdir(BASE_PATH):
        if f.endswith(".png"):
            frame = cv2.imread(os.path.join(BASE_PATH, f))
            cv2.imshow('sorter', frame)
            key = cv2.waitKey(0)
            if key == 27:
                break
            elif key in KEY_FOLDER_MAP:
                shutil.move(os.path.join(BASE_PATH, f), KEY_FOLDER_MAP[key])


    cv2.destroyWindow('sorter')


if __name__ == '__main__':
    Fire(sort_images)