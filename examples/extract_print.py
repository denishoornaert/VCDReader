import numpy as np

# Just for running the examples
import sys
import os
sys.path.append(os.getcwd())

from src.vcd import VCD
from src.vcd_factory import VCDFactory

if (__name__ == '__main__'):
    # Create VCD structure/object
    vcd = VCDFactory.read("examples/files/LFSR16.vcd")
    # Select values for specified fields
    reset = vcd.select("reset")
    clock = vcd.select("clock")
    lfsr  = vcd.select("io_out")
    # print selections
    print("reset: ", reset)
    print("clock: ", clock)
    print("lfsr: ", lfsr)
