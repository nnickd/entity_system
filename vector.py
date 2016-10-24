import numpy as np
from random import random


class vector(object):

    def __init__(self, origin=(0, 0), xy=(0, 0)):
        self.o = np.array(origin)
        self.xy = np.array(xy) + self.o

    def __add__(self, other):
        return self + other

    def __sub__(self, other):
        return self - other

    def __mul__(self, other):
        return self * other

    def __truediv__(self, other):
        return self / other

    @property
    def x(self):
        return self.xy[0]

    @property
    def y(self):
        return self.xy[1]

    @property
    def relative(self):
        return self.xy - self.o

    @property
    def mag(self):
        return np.linalg.norm(self.relative)

    @property
    def rad(self):
        return np.arctan2(self.y, self.x)

    @property
    def deg(self):
        return np.degrees(self.rad)

    def norm(self):
        self.xy = self.xy / self.mag

    def dot(self, other):
        return np.dot(self, other)

    def rotate(self, angle, deg=True):
        rad = np.radians(angle) if deg is True else angle
        x = self.x*np.cos(rad) - self.y*np.sin(rad)
        y = self.y*np.cos(rad) + self.x*np.sin(rad)
        self.xy = np.array([x, y])

    def make(mag=1, focii=(1, 1), angle=None):
        if angle is None:
            angle = random() * 360
        angle = np.radians(angle)
        x = mag * focii[0] * np.cos(angle)
        y = mag * focii[1] * np.sin(angle)
        return x, y
