from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import time


def _print_fps(fps: 'Fps'):
    prefix = '' if fps.name is None else '[{}] '.format(fps.name)
    print('{}FPS: {} (elapsed: {:.9f} sec.)'.format(prefix, fps.last_fps, fps.elapsed), flush=True)


class Fps:
    def __init__(self, func=_print_fps, name=None):
        self.func = func
        self.last = 0
        self.reset()
        self.second = 1.0
        self.name = name
        self.elapsed = 0

    @property
    def last_fps(self):
        return self.last

    def reset(self, offset=0):
        self.fps = 0
        self.tick = time.time() + offset

    def update(self, *argc, **args):
        _boom = False
        dur = time.time() - self.tick
        if dur >= self.second:
            _boom = True
            self.last = self.fps
            self.elapsed = dur
            self.reset(dur - self.second)
            if self.func is not None:
                self.func(self, *argc, **args)
        else:
            self.fps += 1
        return _boom

