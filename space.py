import numpy as np
from random import random
from point import point
from vector import vector


class space(object):

    def __init__(self, length=600, height=600, amount=0, focii=(300, 300)):
        self.length = length
        self.height = height
        self.origin = (length/2, height/2)
        self.field = []
        self.create(amount, focii, False)
        self.amount = amount

    def tick(self, times=1, force=None, spin=None):
        for i in range(times):
            for pt in self.field:
                pt.tick(force, random())

    def create(self, amount, focii, fill=True):
        for i in range(amount):
            vel = vector.make(1, (1, 1))
            if fill is True:
                pos = vector.make(random(), focii)
                point(self, pos, vel)
            else:
                pos = vector.make(1, focii)
                point(self, pos, vel)
