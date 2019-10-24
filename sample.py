from pyfps import Fps
import time
import cv2


def main():
    fps = Fps(None)

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'FPS: {}'.format(fps.last),
                    (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (128, 128, 0), 1, cv2.LINE_AA)
        cv2.imshow('preview', frame)
        fps.update()
        if cv2.waitKey(1) == ord('q'):
            break

if __name__ == '__main__':
    main()
