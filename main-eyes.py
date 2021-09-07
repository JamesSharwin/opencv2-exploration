import cv2
from image_process import process_image
import numpy as np
MINSIZE = (25, 25)
model_left = cv2.CascadeClassifier('default_models/cascade_hammy_left_eye.xml')
model_right = cv2.CascadeClassifier('default_models/cascade_hammy_right_eye.xml')


def get_eye_rects(frame, model_left=model_left, model_right=model_right, minsize=MINSIZE):

    left_rects = model_left.detectMultiScale3(
        frame,
        1.07,
        25,
        minSize=minsize,
        outputRejectLevels=True
    )

    right_rects = model_right.detectMultiScale3(
        frame,
        1.07,
        25,
        minSize=minsize,
        outputRejectLevels=True
    )

    # highest two non-overlapping boxes

    return sorted(tuple(zip(left_rects[0], [x[0] for x in left_rects[2]])), key=lambda x: -x[1])[:1], \
            sorted(tuple(zip(right_rects[0], [x[0] for x in right_rects[2]])), key=lambda x: -x[1])[:1]




def draw_cat_face(frame, left_eye_rect, right_eye_rect, minsize=MINSIZE):

    cv2.rectangle(frame, (0,0), minsize, color=(0, 255, 0), thickness=5)
    if len(left_eye_rect) != 1:
        return

    if len(right_eye_rect) != 1:
        return

    le = left_eye_rect[0][0]
    re = right_eye_rect[0][0]

    cle = np.array((int(le[0] + 0.5 * le[2]), int(le[1] + 0.5 * le[3])))
    cre = np.array((int(re[0] + 0.5 * re[2]), int(re[1] + 0.5 * re[3])))

    angle = np.rad2deg(np.arctan2(cle[1] - cre[1], cle[0] - cre[0]))

    cf = (int((cle[0] + cre[0]) / 2), int(((cle[1] + cre[1]) / 2) + re[3]/4))

    rf = int(np.linalg.norm(cre - cle))

    cv2.circle(frame, cre, int(re[2]/2), color=(0, 0, 255), thickness=6)
    cv2.circle(frame, cle, int(le[2]/2), color=(0, 255, 0), thickness=6)
    cv2.circle(frame, cf, rf, color=(255, 0, 0), thickness=7)
    cv2.putText(frame, text=str(angle), org=(100,100), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3, color=(0,0,0), thickness=3)




vc = cv2.VideoCapture(0)

rec, frame = vc.read()

cv2.waitKey(500)

while rec:

    cv2.imshow('opencv', frame)

    rec, frame = vc.read()

    frame = process_image(frame)
    left_eye_rects, right_eye_rects = get_eye_rects(frame, model_left, model_right)
    draw_cat_face(frame, left_eye_rects, right_eye_rects)

    key = cv2.waitKey(50)

    if key == 27:
        break

cv2.destroyAllWindows()


