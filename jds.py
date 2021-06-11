import serial
from channel import Channel

class JDS:

    CHANNEL_1       = 0
    CHANNEL_2       = 1
    SYS             = 2
    MEASUREMENT     = 4
    COUNTER         = 5
    SWEEP_0         = 6
    SWEEP_1         = 7
    PULSE           = 8
    BURST           = 9
    CHANNEL_ENABLE  = 20
    WAVEFORM        = 21
    FREQUENCY       = 23
    AMPLITUDE       = 25
    PANEL           = 33

    def __init__(self, port="/dev/ttyUSB0"):
        self.channels = list()
        self.channels.append(Channel(self, self.CHANNEL_1))
        self.channels.append(Channel(self, self.CHANNEL_2))

        self.serial = serial.Serial(
            port        = port,
            baudrate    = 115200
        )

    def write(self, command="", plist=""):
        self.serial.flushInput()
        self.serial.flushOutput()
        try:
            params = ','.join(str(i) for i in plist)
        except:
            params = plist
#        print(f":w{command}={params}.\r\n".encode())
        self.serial.write(f":w{command}={params}.\r\n".encode())
        response = self.serial.readline().decode().strip()
        if response != ':ok':
            print("Unexpected Response:", response)
            print("Sent:", f":w{command}={params}.\r\n".encode())
        return response

    def read(self, command):
#        print("Read:", f":r{command}=0.\r\n".encode())
        self.serial.write(f":r{command}=0.\r\n".encode())
        response = self.serial.readline().decode().strip().split('=')[1][:-1]
#        print("Response:", response)
        return(response)

    @property
    def panel(self):
        panels = ("Channel 1 Main", "PANEL_1", "Channel 2 Main", "PANEL_3", "System Settings", "PANEL_5", "PANEL_6", "PANEL_7",
                  "Measurement", "Counter", "Channel 1 Sweep", "Channel 2 Sweep", "Pulse", "Burst")
        return panels[int(self.read(self.PANEL))//8]

    @panel.setter
    def panel(self, value):
        self.write(self.PANEL, value)
