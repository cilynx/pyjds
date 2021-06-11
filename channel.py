class Channel:
    def __init__(self, dds, num):
        self.dds = dds
        self.num = num

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
        return self.dds.WAVEFORMS[int(self.dds.read(self.dds.WAVEFORM + self.num))]

    @wave.setter
    def wave(self, value):
        try:
            self.dds.write(self.dds.WAVEFORM + self.num, self.dds.WAVEFORMS.index(value))
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
