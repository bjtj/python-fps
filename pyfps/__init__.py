from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import time


def _print_fps(fps):
    print('FPS: {}'.format(fps))


class Fps:
    def __init__(self, func=_print_fps):
        self.func = func
        self.reset()
        self.second = 1.0

    def reset(self):
        self.fps = 0
        self.tick = time.time()

    def update(self, *argc, **args):
        dur = time.time() - self.tick
        if dur >= self.second:
            if self.func is not None:
                self.func(self.fps, *argc, **args)
            self.reset()
        else:
            self.fps += 1

