import re

from src.vcd import *
from src.module import *
from src.interval_list import *
from src.wire import *

class VCDFactory():
    """
    Factory class
    """

    seperator = "$enddefinitions $end"

    @staticmethod
    def read_raw(filename):
        with open(filename, 'r') as f:
            raw_data = f.read()
        return raw_data

    @staticmethod
    def parseMeta(meta, vcd):
        meta = re.sub('\n+','',re.sub(' +',' ',meta)).replace(" $end "," $end")
        meta = meta.split(" $end")[:-1]
        pointer = Module()
        for elem in meta:
            data = elem.split(" ")
            if (data[0] == "$var"):
                vcd.nameToId.setdefault(data[4], data[3])
                values = vcd.idToValues.setdefault(data[3], IntervalList())
                pointer.addWire(Wire(data[2], data[3], data[4], values))
            elif (data[0] == "$scope"):
                if (vcd.topModule is None):
                    pointer.setName(data[2])
                    vcd.topModule = pointer
                else:
                    module = Module(data[2], parent=pointer)
                    pointer.addModule(module)
                    pointer = module
            elif (data[0] == "$upscope"):
                pointer = pointer.parent

    @staticmethod
    def convert(string):
        if (string[0] in ('b', 'h')):
            string = '0'+string
        return eval(string)

    @staticmethod
    def parseData(data, vcd):
        data = data.strip().split("\n")
        counter = 0
        while (True):
            try:
                lower_bound_index = data.index("#"+str(counter))+1
                upper_bound_index = data.index("#"+str(counter+1))
                updates = data[lower_bound_index : upper_bound_index]
                for update in updates:
                    id = update[-1:]
                    value = update[:-1].strip()
                    vcd.idToValues[id].insert(counter, VCDFactory.convert(value))
                counter += 1
            except ValueError as e:
                break

    @staticmethod
    def parse(raw_data):
        # Pre-process the raw data
        index = raw_data.find(VCDFactory.seperator)
        meta = raw_data[:index]
        data = raw_data[index+len(VCDFactory.seperator):]
        # Create the VCD object
        vcd = VCD()
        # Parse raw data and populate the VCD object accordingly
        VCDFactory.parseMeta(meta, vcd)
        VCDFactory.parseData(data, vcd)
        return vcd

    @staticmethod
    def read(filename):
        return VCDFactory.parse(VCDFactory.read_raw(filename))
