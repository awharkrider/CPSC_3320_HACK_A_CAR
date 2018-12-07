from pyvit import can
from pyvit.hw.cantact import CantactDev
from pyvit.hw import cantact
import sys

dev = CantactDev("/dev/cu.usbmodem1421")
dev.set_bitrate(500000)
dev.start()
while True:
    print(dev.recv())