class Channel:
    def __init__(self, dds, num):
        self.dds = dds
        self.num = num

    WAVEFORMS = (   "sine",
                    "square",
                    "pulse",
                    "triangle",
                    "partialsine",
                    "cmos",
                    "dc",
                    "half-wave",
                    "full-wave",
                    "pos-ladder",
                    "neg-ladder",
                    "noise",
                    "exp-rise",
                    "exp-decay",
                    "multi-tone",
                    "sinc",
                    "lorenz")

    @property
    def enabled(self):
        statuses = self.dds.read(self.dds.CHANNEL_ENABLE).split(',')
        return bool(int(statuses[self.num]))

    @enabled.setter
    def enabled(self, value):
        if value not in (False,True,'0','1'):
            raise ValueError("Channel.enable state can only be set to bool (True/False) or int (0/1)")
        param = [0,0]
        param[self.num] = int(value)
        other_channel = self.dds.channels[not self.num]
        param[not self.num] = int(other_channel.enabled)
        self.dds.write(self.dds.CHANNEL_ENABLE, param)

    @property
    def wave(self):
        wave_num = int(self.dds.read(self.dds.WAVEFORM + self.num))
        if wave_num < len(self.WAVEFORMS):
            return self.WAVEFORMS[wave_num]
        else:
            return 'Arbitrary' + "{:02d}".format(wave_num-100)

    @wave.setter
    def wave(self, value):
        try:
            # Built-in waveform names
            if isinstance(value, str) and value.lower() in self.WAVEFORMS:
                self.dds.write(self.dds.WAVEFORM + self.num, self.WAVEFORMS.index(value.lower()))
            # Arbitrary waveform names
            elif isinstance(value, str) and value.lower().startswith('arbitrary'):
                if int(value.lower().replace('arbitrary','')) in range(1,61):
                    self.dds.write(self.dds.WAVEFORM + self.num, int(value.lower().replace('arbitrary',''))+100)
                else:
                    raise ValueError("Channel.wave arbitrary waveform name must be in range(1,61)")
            # Built-in and arbitrary waveform indexes
            elif int(value) in tuple(range(len(self.WAVEFORMS))) + tuple(range(101,161)):
                self.dds.write(self.dds.WAVEFORM + self.num, int(value))
            else:
                raise ValueError("Channel.wave can only be set to a known waveform `str` or its index `int`")
        except:
            raise ValueError("Channel.wave can only be set to a known waveform `str` or its index `int`")

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
