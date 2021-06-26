from unittest import TestCase
import pyjds

class PanelsTest(TestCase):
    jds = pyjds.JDS()

    def test_panels(self):
        for p in (0,1,2,4,5,6,7,8,9): # You cannot access the Calibration panel (#3) directly
            with self.subTest(p=p):
                self.jds.panel = p
                self.assertEqual(self.jds.panel, self.jds.PANELS_W[p])
        self.jds.panel = 0
