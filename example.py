import numpy as np

from src.vcd import *
from src.vcd_factory import *

if (__name__ == '__main__'):
    vcd = VCDFactory.read("file/LFSR16.vcd")

    reset = vcd.select("reset")
    clock = vcd.select("clock")
    lfsr  = vcd.select("io_out")
    res = (clock.filterAnd(reset.filterInvert())).filterPosedge()
    lfsr = lfsr.filterEq(res)
    print(lfsr.__str__()[:200])
