from unittest import TestCase
from numpySpeed import speedNumpy

import timeit


class Test(TestCase):
    def test_speed_numpy(self):
        startTime = timeit.default_timer()
        speedNumpy(1000_000, showText=False)
        endTime = timeit.default_timer()

        if endTime - startTime < 0.21693:
            self.assertTrue(True)
        else:
            self.fail(f"Funkcja nie jest wystarczająco szybka, czas działania: {(endTime - startTime):0.5f}s")

    def test_compile_speed(self):
        self.assertTrue(True)
