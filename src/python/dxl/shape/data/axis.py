from .base import Entity
import numpy as np

from doufo import dataclass
from doufo.tensor import Vector

__all__ = ['Axis', 'AXIS3_X', 'AXIS3_Y', 'AXIS3_Z', 'AXES3']

@dataclass
class Axis(Entity):
    normal: Vector
    origin: Vector = Vector([0.0, 0.0, 0.0])

    def rotate_on_direction(self, direction: Vector, theta: float):
        from dxl.shape.function import rotate
        return self.replace(normal = rotate(self.normal, direction, theta),
                            origin = rotate(self.origin, direction, theta))

    def fmap(self, f):
        return Axis(f(self.normal), f(self.origin))

    @classmethod
    def from_axis_like(axis_like, possible_origin=None):
        if possible_origin is None:
            possible_origin = Vector([0.0, 0.0, 0.0])
        if isinstance(axis_like, Axis):
            normal, origin = axis_like.normal, axis_like.origin
        else:
            normal, origin = axis_like, possible_origin
        normal, origin = Vector(normal), Vector(origin)
        return Axis(normal, origin)

AXIS3_X = Axis(Vector([1.0, 0.0, 0.0]))
AXIS3_Y = Axis([0.0, 1.0, 0.0])
AXIS3_Z = Axis([0.0, 0.0, 1.0])


class AXES3:
    x = AXIS3_X
    y = AXIS3_Y
    z = AXIS3_Z
