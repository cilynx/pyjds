from unittest import TestCase
import pyjds

class SysTest(TestCase):
    jds = pyjds.JDS()

    def test_modelnum(self):
        self.assertIsInstance(self.jds.model, int)

    def test_serialnum(self):
        self.assertIsInstance(self.jds.serialnum, int)

    def test_sound(self):
        for s in (True, False, 1, 0):
            with self.subTest(s=s):
                self.jds.sound = s
                self.assertEqual(self.jds.sound, s)

    def test_sound_invalid(self):
        for s in (None, "", "1", -1, 2):
            with self.subTest(s=s):
                with self.assertRaises(ValueError):
                    self.jds.sound = s

    def test_brightness(self):
        for b in range(13):
            with self.subTest(b=b):
                self.jds.brightness = b
                self.assertEqual(self.jds.brightness, b)

    def test_brightness_invalid(self):
        for b in (None, "", "1", -1, 13):
            with self.subTest(b=b):
                with self.assertRaises(ValueError):
                    self.jds.brightness = b

    def test_language(self):
        for l in (1,0):
            with self.subTest(l=l):
                self.jds.language = l
                self.assertEqual(self.jds.language, l)

    def test_language_invalid(self):
        for l in (None, "", "1", -1, 2):
            with self.subTest(l=l):
                with self.assertRaises(ValueError):
                    self.jds.language = l

    def test_sync(self):
        for s in ((True,False,True,False,True),(True,0,1,0,1),(1,0,False,0,1),(0,1,0,1,0),(1,1,1,1,1),[1,0,1,0,1],(0,0,0,0,0)):
            with self.subTest(s=s):
                self.jds.sync = s
                self.assertEqual(self.jds.sync, tuple(s))

    def test_sync_invalid(self):
        for s in (None, "", "1", 1, 0, -1, (1,1,1,1), (), [], (1,1,1,1,2), (1,1,1,1,""), (None,1,1,1,1)):
            with self.subTest(s=s):
                with self.assertRaises(ValueError):
                    self.jds.sync = s

    def test_arb_max(self):
        for m in (1, 10, 60, 15):
            with self.subTest(m=m):
                self.jds.arb_max = m
                self.assertEqual(self.jds.arb_max, m)

    def test_arb_max_invalid(self):
        for m in (None, "", "1", -1, 0, 61):
            with self.subTest(m=m):
                with self.assertRaises(ValueError):
                    self.jds.arb_max = m
