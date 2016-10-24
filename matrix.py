import numpy as np


class matrix(object):

    def __init__(self, field):
        self.field = field
        self.positions = np.array([point.pos for point in field])
        self.velocities = np.array([point.vel for point in field])

    def tick(self, deg=0):
        self.velocities = self.velocities @ self.rotmat(deg)
        #force = np.random.randn(len(self.velocities), 2) / 30
        #self.velocities += force
        self.positions += self.velocities

    def rotmat(self, deg):
        angle = np.radians(deg)
        c = np.cos(angle)
        s = np.sin(angle)
        return np.matrix([[c, -s], [s, c]])
