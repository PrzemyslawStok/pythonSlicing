from unittest import TestCase
from numpySpeed import speedNumpy

import timeit


class Test(TestCase):
    def test_compile_speed(self):
        speedNumpy(1000_000, showText=True)
        self.assertTrue(True)

    def test_function0(self):
        self.assertTrue(True)
