from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import time


def _print_fps(fps, name=None):
    prefix = '' if name is None else '[{}] '.format(name)
    print('{}FPS: {}'.format(prefix, fps))


class Fps:
    def __init__(self, func=_print_fps, name=None):
        self.func = func
        self.last = 0
        self.reset()
        self.second = 1.0
        self.name = name

    @property
    def last_fps(self):
        return self.last

    def reset(self):
        self.fps = 0
        self.tick = time.time()

    def update(self, *argc, **args):
        dur = time.time() - self.tick
        if dur >= self.second:
            self.last = self.fps
            if self.func is not None:
                self.func(self.fps, *argc, **args, name=self.name)
            self.reset()
        else:
            self.fps += 1

