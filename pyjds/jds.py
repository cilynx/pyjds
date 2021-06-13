import serial
from .channel import Channel

class JDS:

    # Registers
    MODEL_NUM       = 0  # Not yet implemented
    SERIAL_NUM      = 1  # Not yet implemented
    #               = 2  # 29
    #               = 3  # 32002
    #               = 4  # 2042
    #               = 5  # 1024
    #               = 6  # 78
    #               = 7  # 1720
    #               = 8  # 1729
    #               = 9  # 1727
    #               = 10 # 2857
    #               = 11 # 2069
    #               = 12 # 1037
    #               = 13 # 80
    #               = 14 # 1724
    #               = 15 # 1731
    #               = 16 # 1730
    #               = 17 # 2839
    #               = 18 # 5050
    #               = 19 # 0
    CHANNEL_ENABLE  = 20
    WAVEFORM        = 21 # and 22
    FREQUENCY       = 23 # and 24
    AMPLITUDE       = 25 # and 26
    OFFSET          = 27 # and 28
    DUTY            = 29 # and 30
    PHASE           = 31
    ACTION          = 32 # Not yet implemented
    PANEL           = 33
    #               = 34 # 0
    #               = 35 # 0
    MEASURE_COUP    = 36 # Not yet implemented
    MEASURE_GATE    = 37 # Not yet implemented
    MEASURE_MODE    = 38 # Not yet implemented
    COUNTER_RESET   = 39 # Not yet implemented
    SWEEP_START     = 40 # Not yet implemented
    SWEEP_END       = 41 # Not yet implemented
    SWEEP_TIME      = 42 # Not yet implemented
    SWEEP_DIRECTION = 43 # Not yet implemented
    SWEEP_MODE      = 44 # Not yet implemented
    PULSE_WIDTH     = 45 # Not yet implemented
    PULSE_PERIOD    = 46 # Not yet implemented
    PULSE_OFFSET    = 47 # Not yet implemented
    PULSE_AMPLITUDE = 48 # Not yet implemented
    BURST_COUNT     = 49 # Not yet implemented
    BURST_MODE      = 50 # Not yet implemented
    SYS_SOUND_W     = 51
    SYS_SOUND_R     = 52
    SYS_BRIGHT_W    = 52
    SYS_BRIGHT_R    = 53
    SYS_LANGUAGE_W  = 53
    SYS_LANGUAGE_R  = 54
    SYS_SYNC_W      = 54
    SYS_SYNC_R      = 55
    SYS_ARB_MAX_W   = 55
    SYS_ARB_MAX_R   = 56
    #               = 57 # 0
    #               = 58 # 0
    #               = 59 # 0
    #               = 60 # 0
    #               = 61 # 0
    #               = 62 # 0
    #               = 63 # 0
    #               = 64 # 0
    #               = 65 # 0
    #               = 66 # 0
    #               = 67 # 0
    #               = 68 # 0
    #               = 69 # 0
    PROFILE_SAVE    = 70 # Not yet implemented
    PROFILE_LOAD    = 71 # Not yet implemented
    PROFILE_CLEAR   = 72 # Not yet implemented
    #               = 73 # 0
    #               = 74 # 0
    #               = 75 # 0
    #               = 76 # 0
    #               = 77 # 0
    #               = 78 # 0
    #               = 79 # 0
    COUNTER_DATA    = 80 # Not yet implemented
    MEAS_FREQ_F     = 81 # Not yet implemented
    MEAS_FREQ_T     = 82 # Not yet implemented
    MEAS_POS_PULSE  = 83 # Not yet implemented
    MEAS_NEG_PULSE  = 84 # Not yet implemented
    MEAS_PERIOD     = 85 # Not yet implemented
    MEAS_DUTY       = 86 # Not yet implemented
    MEAS_U1         = 87 # Not yet implemented
    MEAS_U2         = 88 # Not yet implemented
    MEAS_U3         = 89 # Not yet implemented
    #               = 90 # 0
    #               = 91 # 0
    #               = 92 # 0
    #               = 93 # 0
    #               = 94 # 0
    #               = 95 # 0 # Last register you can read with extended read
    #               = 96 # 0
    #               = 97 # 0
    #               = 98 # 0
    #               = 99 # 0 # Last register you can read with single read

    PANELS_W = ("Channel 1 Main",
                "Channel 2 Main",
                "System Settings",
                None,
                "Measurement",
                "Counter",
                "Channel 1 Sweep",
                "Channel 2 Sweep",
                "Pulse",
                "Burst")

    PANELS_R = ("Channel 1 Main",
                "PANEL_1",
                "Channel 2 Main",
                "PANEL_3",
                "System Settings",
                "PANEL_5",
                "PANEL_6",
                "PANEL_7",
                "Measurement",
                "Counter",
                "Channel 1 Sweep",
                "Channel 2 Sweep",
                "Pulse",
                "Burst")

    def __init__(self, port="/dev/ttyUSB0"):
        self.channels = list()
        self.channels.append(Channel(self, 0))
        self.channels.append(Channel(self, 1))

        self.serial = serial.Serial(
            port        = port,
            baudrate    = 115200
        )

    def write(self, command="", plist="", debug=False):
        self.serial.flushInput()
        self.serial.flushOutput()
        try:
            params = ','.join(str(i) for i in plist)
        except:
            params = plist
        self.serial.write(f":w{command}={params}.\r\n".encode())
        response = self.serial.readline().decode().strip()
        if debug:
            print("Raw Write Request:", f":w{command}={params}.\r\n".encode())
            print(f"Raw Write Response: {response}")
        if response != ':ok':
            print("Unexpected Response:", response)
            print("Sent:", f":w{command}={params}.\r\n".encode())
        return response

    def read(self, command, count=0, debug=False):
        # Normalize all commands to 2-digit character representations
        # Single digits get a 0 added to the end by the device
        # e.g. '1' will be interpreted as '10'.  No bueno.
        command = f'{int(command):02}'
        if debug:
            print("Raw Read Request:", f":r{command}={count}.\r\n".encode())
        self.serial.write(f":r{command}={count}.\r\n".encode())
        response = {}
        while count >= 0:
            raw_response = self.serial.readline()
            if debug:
                print(f"Raw Response {count}: {raw_response}")
            tokens = raw_response.decode().strip().split('=')
            register_address = tokens[0][2:]
            register_value = tokens[1][:-1]
            response[register_address] = register_value
            count -= 1
        if debug:
            print("Dict Response:", response)
        if len(response) == 1:
            return(response[str(command)])
        return(response)

    @property
    def panel(self):
        return self.PANELS_R[int(self.read(self.PANEL))//8]

    @panel.setter
    def panel(self, value):
        self.write(self.PANEL, value)

    @property
    def phase(self):
        return int(self.read(self.PHASE))/10

    @phase.setter
    def phase(self, value):
        self.write(self.PHASE, value*10)

    @property
    def model(self):
        return int(self.read(self.MODEL_NUM))

    @property
    def serialnum(self):
        return int(self.read(self.SERIAL_NUM))

    @property
    def sound(self):
        return int(self.read(self.SYS_SOUND_R))

    @sound.setter
    def sound(self, value):
        if value not in (0,1):
            raise ValueError("SYS_SOUND can only be set to 0 (Off) or 1 (On)")
        self.write(self.SYS_SOUND_W, int(value))

    @property
    def brightness(self):
        return int(self.read(self.SYS_BRIGHT_R))

    @brightness.setter
    def brightness(self, value):
        if value not in range(13):
            raise ValueError("SYS_BRIGHT can only be set to integers from 0-12")
        self.write(self.SYS_BRIGHT_W, value)

    @property
    def language(self):
        return int(self.read(self.SYS_LANGUAGE_R))

    @language.setter
    def language(self, value):
        if value not in (0,1):
            raise ValueError("SYS_LANGUAGE can only be set to 0 (English) or 1 (Chinese)")
        self.write(self.SYS_LANGUAGE_W, value)

    @property
    def sync(self):
        return eval(self.read(self.SYS_SYNC_R))

    @sync.setter
    def sync(self, value):
        try:
            if len(value) != 5:
                raise ValueError("SYS_SYNC can only be set to a 5-tuple (Freq, Wave, Ampl, Duty, Offs) with values of 0 (Not-Synchronized) or 1 (Synchronized)")
            for val in value:
                if val not in (0, 1):
                    raise ValueError("SYS_SYNC can only be set to a 5-tuple (Freq, Wave, Ampl, Duty, Offs) with values of 0 (Not-Synchronized) or 1 (Synchronized)")
            self.write(self.SYS_SYNC_W, tuple(map(int, value)))
        except:
            raise ValueError("SYS_SYNC can only be set to a 5-tuple (Freq, Wave, Ampl, Duty, Offs) with values of 0 (Not-Synchronized) or 1 (Synchronized)")

    @property
    def arb_max(self):
        return int(self.read(self.SYS_ARB_MAX_R))

    @arb_max.setter
    def arb_max(self, value):
        if value not in range(1,61):
            raise ValueError("SYS_ARB_MAX can only be set to integers from 1-60")
        self.write(self.SYS_ARB_MAX_W, value)
