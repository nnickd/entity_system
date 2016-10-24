from vector import vector


class point(object):

    def __init__(self, space, pos=(0, 0), vel=(0, 0)):
        self._pos = vector(space.origin, pos)
        self._vel = vector((0, 0), vel)
        space.field.append(self)

    def tick(self, force=None, spin=None):
        if force is not None:
            self.vel += force
        if spin is not None:
            self._vel.rotate(spin)
        self.pos += self.vel
        self.boundary()

    @property
    def pos(self):
        return self._pos.xy

    @pos.setter
    def pos(self, value):
        self._pos.xy = value

    @property
    def vel(self):
        return self._vel.xy

    @vel.setter
    def vel(self, value):
        self._vel.xy = value

    @property
    def acc(self):
        return self._acc.xy

    @acc.setter
    def acc(self, value):
        self._acc.xy = value
