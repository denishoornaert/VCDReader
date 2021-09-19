import numpy as np
import matplotlib.pyplot as plt

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
    lfsr  = vcd.select("io_out")
    # plot values
    fig, axs = plt.subplots(1, 2, tight_layout=True)
    axs[0].plot(lfsr.values)
    axs[0].set_ylabel("Pseudo random numbers")
    axs[1].hist(lfsr.values, bins=100)
    axs[1].set_ylabel("PRN Distribution")
    plt.show()
