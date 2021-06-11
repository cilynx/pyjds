class Channel:
    def __init__(self, dds, num):
        self.dds = dds
        self.num = num

    WAVEFORMS = (   "Sine",
                    "Square",
                    "Pulse",
                    "Triangle",
                    "PartialSine",
                    "CMOS",
                    "DC",
                    "Half-Wave",
                    "Full-Wave",
                    "Pos-Ladder",
                    "Neg-Ladder",
                    "Noise",
                    "Exp-Rise",
                    "Exp-Decay",
                    "Multi-Tone",
                    "Sinc",
                    "Lorenz")

    @property
    def enabled(self):
        statuses = self.dds.read(self.dds.CHANNEL_ENABLE).split(',')
        return bool(int(statuses[self.num]))

    @enabled.setter
    def enabled(self, value):
        param = [0,0]
        param[self.num] = int(value)
        other_channel = self.dds.channels[int(not self.num)]
        param[int(not self.num)] = int(other_channel.enabled)
        self.dds.write(self.dds.CHANNEL_ENABLE, param)

    @property
    def wave(self):
        return self.WAVEFORMS[int(self.dds.read(self.dds.WAVEFORM + self.num))]

    @wave.setter
    def wave(self, value):
        try:
            self.dds.write(self.dds.WAVEFORM + self.num, self.WAVEFORMS.index(value))
        except:
            self.dds.write(self.dds.WAVEFORM + self.num, int(value))

    @property
    def freq(self):
        return int(self.dds.read(self.dds.FREQUENCY + self.num).split(',')[0])/100.0

    @freq.setter
    def freq(self, value):
        self.dds.write(self.dds.FREQUENCY + self.num, value*100)

    @property
    def amplitude(self):
        return int(self.dds.read(self.dds.AMPLITUDE + self.num).split(',')[0])/1000.0

    @amplitude.setter
    def amplitude(self, value):
        self.dds.write(self.dds.AMPLITUDE + self.num, value*1000)

    @property
    def offset(self):
        return (int(self.dds.read(self.dds.OFFSET + self.num))-1000)/100

    @offset.setter
    def offset(self, value):
        self.dds.write(self.dds.OFFSET + self.num, 1000+(100*value))

    @property
    def duty(self):
        return int(self.dds.read(self.dds.DUTY + self.num))/10

    @duty.setter
    def duty(self, value):
        self.dds.write(self.dds.DUTY + self.num, value*10)
