'''
Usage:
main.py --filepath=<string> --field=<string>

operation:
   --filepath=<string>  Absolute path to the vcd file to parse
   --field=<string>     Target field in the selected VCD file
'''
from docopt import docopt
import numpy as np

from src.vcd import VCD
from src.vcd_factory import VCDFactory

if (__name__ == '__main__'):
    args = docopt(__doc__)
    # Create VCD structure/object
    vcd = VCDFactory.read(args["--filepath"])
    # Select values for specified fields
    values = vcd.select(args["--field"])
    # print selections
    print(args["--field"]+":", values)
