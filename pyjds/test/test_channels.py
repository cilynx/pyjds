from unittest import TestCase
import pyjds

class ChannelsTest(TestCase):
    jds = pyjds.JDS()

    def test_enabled(self):
        for e in (True, False):
            with self.subTest(e=e):
                for channel in self.jds.channels:
                    channel.enabled = e
                    self.assertEqual(channel.enabled, e)

    def test_frequency(self):
        for f in (0.01, 0.1, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 0):
            with self.subTest(f=f):
                for channel in self.jds.channels:
                    channel.freq = f
                    self.assertEqual(channel.freq, f)

    def test_amplitude(self):
        for v in (0.001, 0.01, 0.1, 1, 20, 0):
            with self.subTest(v=v):
                for channel in self.jds.channels:
                    channel.amplitude = v
                    self.assertEqual(channel.amplitude, v)

    def test_offset(self):
        for o in (-9.99, -.99, 1, 9.99, 0):
            with self.subTest(o=o):
                for channel in self.jds.channels:
                    channel.offset = o
                    self.assertEqual(channel.offset, o)

    def test_duty(self):
        for d in (99.9, 10, 1, 0.1, 0):
            with self.subTest(d=d):
                for channel in self.jds.channels:
                    channel.duty = d
                    self.assertEqual(channel.duty, d)

    def test_wave(self):
        for w in (self.jds.channels[0].WAVEFORMS):
            with self.subTest(w=w):
                for channel in self.jds.channels:
                    channel.wave = w
                    self.assertEqual(channel.wave, w)