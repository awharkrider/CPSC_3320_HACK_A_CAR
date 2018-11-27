from pyvit import can
from pyvit.hw.cantact import CantactDev
from pyvit.hw import cantact
import sys


def write_to_can_bus(input):
    dev = cantact.CantactDev(sys.argv[1])
    dev.ser.write(input.encode())        # input => 'S0\r'
    dev.start()
    count = 0
    while True:
        count = count + 1
        frame = dev.recv()
        dev.send(frame)
        print("%d: %s" % (count, str(frame)))


def read_from_can_bus():
    dev = CantactDev("/dev/cu.usbmodem1451")      # need to set serial port correctly
    dev.set_bitrate(500000)
    dev.start()
    while True:
        print(dev.recv())
