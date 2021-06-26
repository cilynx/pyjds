from unittest import TestCase
import pyjds

class ChannelsTest(TestCase):
    jds = pyjds.JDS()

    def test_enabled(self):
        for e in (True, 1, '1', "1"):
            with self.subTest(e=e):
                for channel in self.jds.channels:
                    other_index = not channel.num
                    other_channel = self.jds.channels[other_index]
                    other_before = other_channel.enabled
                    channel.enabled = e
                    self.assertEqual(channel.enabled, True)
                    self.assertEqual(other_channel.enabled, other_before)
        for e in (False, 0, '0', "0"):
            with self.subTest(e=e):
                for channel in self.jds.channels:
                    other_index = not channel.num
                    other_channel = self.jds.channels[other_index]
                    other_before = other_channel.enabled
                    channel.enabled = e
                    self.assertEqual(channel.enabled, False)
                    self.assertEqual(other_channel.enabled, other_before)

    def test_enabled_invalid(self):
        for e in (None, "", '', 'a', "foo", -1, 13):
            with self.subTest(e=e):
                with self.assertRaises(ValueError):
                    for channel in self.jds.channels:
                        channel.enabled = e

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
        waveforms = self.jds.channels[0].WAVEFORMS
        for w in waveforms: # Built-in waveform names
            for w in (w, w.lower(), w.upper()):
                with self.subTest(w=w):
                    for channel in self.jds.channels:
                        channel.wave = w
                        self.assertEqual(channel.wave, w.lower())
        for n in ('Arbitrary1','arbitrary02',"ARBITRARY60"): # Arbitrary wavefrom names
            with self.subTest(w=w):
                for channel in self.jds.channels:
                    channel.wave = w
                    self.assertEqual(channel.wave.lower().replace('y0','y'), w.lower().replace('y0','y'))
        for w in range(len(waveforms)): # Built-in waveform indexes
            with self.subTest(w=w):
                for channel in self.jds.channels:
                    channel.wave = w
                    self.assertEqual(channel.wave, waveforms[w])
        for w in range(101,161): # Arbitrary waveform indexes
            with self.subTest(w=w):
                for channel in self.jds.channels:
                    channel.wave = w
                    self.assertEqual(channel.wave, 'Arbitrary' + "{:02d}".format(w-100))

    def test_wave_invalid(self):
        for w in (None, "", '', 'a', "foo", 'Arbitrary0', "arbitrary61", -1, len(self.jds.channels[0].WAVEFORMS), 100):
            with self.subTest(w=w):
                with self.assertRaises(ValueError):
                    for channel in self.jds.channels:
                        channel.wave = w
