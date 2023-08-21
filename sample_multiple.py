from pyfps import Fps
import time
import cv2
import threading
import queue

def handler_thread(qu, fps):
    while 1:
        item = qu.get()
        if item is None:
            break
        fps.update()
        time.sleep(0.1)

    print('[handler thread] DONE.')


def main():
    cam_fps = Fps(name="CAM")
    handler_fps = Fps(name="HANDLER")

    qu = queue.Queue()

    cap = cv2.VideoCapture(0)

    tx = threading.Thread(target=handler_thread, args=(qu, handler_fps))
    tx.start()

    while True:
        ret, frame = cap.read()
        if not ret:
            time.sleep(0.1)
            print('read failed - wait...')
            continue

        if qu.empty():
            qu.put(frame)

        cv2.putText(frame, 'FPS: {}'.format(cam_fps.last_fps),
                    (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (128, 128, 0), 1, cv2.LINE_AA)
        cv2.imshow('preview', frame)
        cv2.setWindowTitle('preview', 'preview (press `q` to quit)')
        cam_fps.update()
        if cv2.waitKey(1) == ord('q'):
            break

    qu.put(None)
    tx.join()

if __name__ == '__main__':
    main()
