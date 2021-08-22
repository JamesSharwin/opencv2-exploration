import cv2
# from image_process import process_image

model = cv2.CascadeClassifier('cascade/cascade.xml')

vc = cv2.VideoCapture(0)

rec, frame = vc.read()

cv2.waitKey(500)

while rec:

    cv2.imshow('opencv', frame)

    rec, frame = vc.read()

    # frame = process_image(frame)
    rects = model.detectMultiScale3(
        frame,
        1.1,
        12,
        outputRejectLevels=True
    )

    for i, (x, y, w, h) in enumerate(rects[0]):
        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            color=(0,0,255),
            thickness=3
        )

    key = cv2.waitKey(50)

    if key == 27:
        break

cv2.destroyAllWindows()


