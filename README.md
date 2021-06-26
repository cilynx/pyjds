# Quickstart
```python
#!/usr/bin/env python

import pyjds

jds = pyjds.JDS('/dev/ttyUSB0')

chan1 = jds.channels[0]
chan2 = jds.channels[1]

chan1.wave 	    = 'Sine'
chan1.freq 	    = 10 # Hz
chan1.amplitude = 5  # Vpp
chan1.offset 	 = 1  # V
chan1.duty 	    = 50 # %

chan2.wave 	    = 'Square'
chan2.freq 	    = 10 # Hz
chan2.amplitude = 5  # Vpp
chan2.offset 	 = -1 # V
chan2.duty 	    = 50 # %

jds.phase = 10 # Deg

chan1.enabled = True
chan2.enabled = True
```
# channel.enabled
Channel output.  Can be set by `bool` (`True`/`False`) or `int` (`1`/`0`).  Returns `bool` state.
```python
# Enable channel output
channel.enabled = True
# or
channel.enabled = 1

# Disable channel output
channel.enabled = False
# or
channel.enabled = 0

# Print the current output state (`bool`)
print(channel.enabled)

# Valid values are:
(True, False, 1, 0)
```

# jds.model
The device model number...ish.  Generally aligns with the maximum frequency.  Read-only.
```python
# Prints `60` on my 60MHz Koolertron GH-CJDS26-F
print(jds.model)
```

# jds.serial
The device serial number.  Probably unique on each device.  Mine is 183xxxxxxx.  I'd be curious to know what others see.  Read-only.
```python
# Prints `183xxxxxxx` (not masked IRL) on my Koolertron GH-CJDS26-F
print(jds.serial)
```

# jds.panel
The current mode / visible UI panel.  Can be set by name or integer index.  Returns name `str` of the current panel.
```python
# Bring up the main panel with Channel 1 on top
jds.panel = 'Channel 1 Main'
# or
jds.panel = 0

# Print the active panel name (`str`)
print(jds.panel)

# Valid values/indexes are:
("Channel 1 Main",
 "Channel 2 Main",
 "System Settings",
 None,
 "Measurement",
 "Counter",
 "Channel 1 Sweep",
 "Channel 2 Sweep",
 "Pulse",
 "Burst")
```

# jds.sound
Keypress beeps.  They're super annoying on the Koolertron GH-CJDS26-F, so I keep them disabled.  Can be set by `bool` (`True`/`False`) or `int` (`1`/`0`).  Returns `int` state.
```python
# Turn on the keypress beep
jds.sound = True
# or
jds.sound = 1

# Turn off the keypress beep
jds.sound = False
# or
jds.sound = 0

# Print the current sound state (`int`)
print(jds.sound)

# Valid values are:
(True, False, 1, 0)
```

# jds.brightness
Display brightness. Takes an `int` from `0` (off) to `12` (full bright).  Returns an `int` of the current brightness.
```python
# Turn off the display
jds.brightness = 0

# Set the display to maximum brightness
jds.brightness = 12

# Print the current brightness (`int`)
print(jds.brightness)

# Valid values are:
range(13)
```

# jds.language
Display language.  Takes an `int`, either `0` (English) or `1` (Chinese).  Takes full effect on the next display refresh.  Returns an `int` of the currently selected language.
```python
# Set the language to English
jds.language = 0

# Set the language to Chinese
jds.language = 1

# Print the `int` representing the current language
print(jds.language)

# Valid values are:
(0,1)
```

# jds.phase
Phase angle between Channel 1 and Channel 2 in degrees.  Takes a `float` precise to 0.1 deg.  Returns a `float` precise to 0.1 deg.  Range from 0.0 to 359.9 degrees.
```python
# Set the phase angle to 10.5 degrees
jds.phase = 10.5

# Set the phase angle to 0 degrees
jds.phase = 0

# Print the current phase angle
print(jds.phase)

# Valid values are:
0.0 <= phase <= 359.9
```

# jds.sync
Channel synchronization lock.  Takes a `bool` (`True`/`False`) or `int` (`1`/`0`) 5-element `list` or `tuple`.  Returns a 5-`tuple` of `int` of whether each element is sync-locked across both channels (`1`) or can be set independently (`0`).
```python
# Fields are (Frequency, Waveform, Amplitude, Duty, Offset)

# Sync-lock only frequency and amplitude
jds.sync = (1, 0, 1, 0, 0)

# Sync-lock everything
jds.sync = (True, True, True, True, True)

# Sync-lock nothing
jds.sync = [0, 0, 0, 0, 0]

# Print an `int` 5-`tuple` of sync-lock state
print(jds.sync)
```

# jds.arb_max
How many Arbitrary Waveform slots to show in the waveform selector interface.  You can show from 0 to 60 Arbitrary Waveforms.  If you don't use a lot of Arbitrary Waveforms, setting this to a low number can save you a bunch of scrolling through the UI.  Takes and returns an `int` ranging from `0` to `60`.
```python
# Show all 60 possible Arbitrary Waveforms
jds.arb_max = 60

# Don't show any Arbitrary Waveforms
jds.arb_max = 0

# Show the default 15 Arbitrary Waveforms
jds.arb_max = 15

# Print the current number (`int`) of Arbitrary Waveforms available in the UI
print(jds.arb_max)

# Valid values are:
range(61)
```
