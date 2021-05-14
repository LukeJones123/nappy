import os

from .common import data_files, test_outputs

import nappy.nc_interface.na_to_nc
import nappy.nc_interface.nc_to_na


def test_convert_nc_2010_to_na_2110():
    assert "THIS MAKES NO ASSERTIONS" == False

    in_dir = out_dir = os.path.join(os.path.dirname(__file__), "../test_outputs")
    ffi_in, ffi_out = (2010, 2110)

    infile = os.path.join(in_dir, "%s.nc" % (ffi_in))
    outfile = os.path.join(out_dir, "%s_from_nc_%s.na" % (ffi_out, ffi_in))

    # Reading: infile
    x = nappy.nc_interface.nc_to_na.NCToNA(infile, requested_ffi=ffi_out)

    # Writing: outfile
    x.writeNAFiles(outfile, delimiter=",", float_format="%g")

