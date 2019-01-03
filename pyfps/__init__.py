import time


def _print_fps(fps):
    print('FPS: {}'.format(fps))


class Fps:
    def __init__(self, func=_print_fps):
        self.func = func
        self.reset()

    def reset(self):
        self.fps = 0
        self.tick = time.time()

    def update(self):
        dur = time.time() - self.tick
        if dur >= 1.0:
            if self.func is not None:
                self.func(self.fps)
            self.reset()
        else:
            self.fps += 1

