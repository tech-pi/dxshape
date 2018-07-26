import unittest
import numpy as np
import math
from dxl.shape.data import Point, Box, Vector
from dxl.shape.data import AXIS3_X, AXIS3_Y, AXIS3_Z, Axis
from dxl.shape.function import testing
from dxl.function.tensor import all_close

import pytest

class TestPoint(unittest.TestCase):
    def test_init(self):
        p = Point([1.0, 2.0, 0.0])
        assert isinstance(p.origin, Vector)
        assert all_close(p.origin, [1.0, 2.0, 0.0])

    def test_ndim(self):
        p = Point(origin=np.array([1.0, 2.0, 0.0]))
        self.assertEqual(p.ndim, 3)

    def test_translate(self):
        p = Point(origin=np.array([1.0, 2.0, 0.0]))
        assert testing.all_close(p.translate(-np.array([1.0, 1.0, 3.0])),
                                 Point(np.array([0.0, 1.0, -3.0])))

    @pytest.mark.skip('maybe not needed')
    def test__rotate_on_direction(self):
        p = Point(origin=np.array([1.0, 2.0, 0.0]))
        direction_x = np.array([1.0, 0.0, 0.0])
        direction_y = np.array([0.0, 1.0, 0.0])
        direction_z = np.array([0.0, 0.0, 1.0])
        theta = math.pi / 2
        # p_rot_x = p._rotate_on_direction(direction_x, theta)
        # p_rot_y = p._rotate_on_direction(direction_y, theta)
        # p_rot_z = p._rotate_on_direction(direction_z, theta)
        self.assertAlmostEquals(p._rotate_on_direction(
            direction_x, theta), Point(np.array([1.0, 0.0, 2.0])))
        self.assertAlmostEquals(p._rotate_on_direction(
            direction_y, theta), Point(np.array([0.0, 2.0, -1.0])))
        self.assertAlmostEquals(p._rotate_on_direction(
            direction_z, theta), Point(np.array([-2.0, 1.0, 0.0])))

    def test_rotate(self):
        p = Point(origin=np.array([0.0, 2.0, 0.0]))
        axis = Axis(normal=[-1.0, 0.0, 0.0],
                    origin=np.array([0.0, 1.0, 0.0]))
        the = math.pi / 2
        p_rotate = p.rotate(axis, the)
        self.assertAlmostEqual(p_rotate, Point([0.0, 1.0, -1.0]))

    def test_is_in(self):
        p1 = Point([0, 0, 0])
        p2 = Point([20, 0, 0])
        b = Box([10, 10, 10], [0, 0, 0], [0, 0, 1])
        self.assertIs(p1.is_in(b), True)
        self.assertIs(p2.is_in(b), False)


if __name__ == "__main__":
    unittest.main()
