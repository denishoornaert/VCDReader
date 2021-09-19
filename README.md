# VCDReader

Simple python-based VCD file reader.

## Command line extraction
A specific field can be extracted from a given VCD file using the ```main.py``` script.
One just need to provide the path to the target file and the name of the field.
For instance:
```bash
python3 main.py --filepath=examples/files/LFSR16.vcd --field-io_out
```

### Helper
```
Usage:
main.py --filepath=<string> --field=<string>

operation:
   --filepath=<string>  Absolute path to the vcd file to parse
   --field=<string>     Target field in the selected VCD file
```

## Examples
The code examples located in folder ```examples/``` can be run as follows:
```bash
python3 examples/extract_print.py
python3 examples/plot.py
```

## Disclaimer
This is a side project. The code is provided as it and done without any pretensions.

## TODOs (amongst many others)

 - Implementation of filters
 - Refactor the ```IntervalList``` class to use trees
