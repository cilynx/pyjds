from unittest import TestCase
import pyjds

class JDSTest(TestCase):
    jds = pyjds.JDS()

    def test_phase(self):
        for p in (359.9, 36, 3.6, 3, 0.6, 0):
            with self.subTest(p=p):
                self.jds.phase = p
                self.assertEqual(self.jds.phase, p)

    def test_panel(self):
        for p in range(len(self.jds.PANELS_W)):
            if p != 3: # There is no Mode 3 -- it's a no-op
                with self.subTest(p=p):
                    self.jds.panel = p
                    self.assertEqual(self.jds.panel, self.jds.PANELS_W[p])
        self.jds.panel = 0
