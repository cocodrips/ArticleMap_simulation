# -*- coding: utf-8 -*-
IMAGE_RATIO = 1.3
class Rect:
    x = 0
    y = 0
    width = 0
    height = 0

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def vec4(self):
        return (self.x, self.y, self.width, self.height)

    def __repr__(self):
        return unicode("[{}, {}, {}, {}]".format(self.x, self.y, self.width, self.height))


class Page:
    rect = None
    ideal_area = 0
    priority = 0
    type = None

    def __init__(self, priority, string):
        self.priority = priority
        self.type = string

    def __repr__(self):
        # return unicode("<Page priority:{0}>".format(self.priority))
        return unicode("<{0}>".format(self.priority))

