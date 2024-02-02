import pybdsim 
from generic_parser import EntryPointParameters, entrypoint


# Script arguments -------------------------------------------------------------
def get_params():
    params = EntryPointParameters()
    params.add_parameter(
        name="tfs_file",
        type=str,
        required=True,
        help="Path to the tfs file.",
    )
    params.add_parameter(
        name="lattice",
        type=str,
        required=True,
        help="SuperKEKB lattice: ler or her",
    )
    params.add_parameter(
        name="linear",
        type=bool,
        required=True,
        help="Linear or nonlinear model",
        # Note, with nonlinear optics (i.e. including sextupoles and higher) the emittance between each plane (horizontal, vertical) will be mixed
        # and the calculated optical functions are not representative. A model converted with the linear flag will however be valid.
    )

    return params


# Entrypoint -------------------------------------------------------------------
@entrypoint(get_params(), strict=True)
def main(inp):

    if (inp.lattice == 'ler') & (inp.linear == True):
        a, b = pybdsim.Convert.MadxTfs2Gmad(inp.tfs_file, '../bdsim/ler_linear', linear=True)
    elif (inp.lattice == 'ler') & (inp.linear == False):
        a, b = pybdsim.Convert.MadxTfs2Gmad(inp.tfs_file, '../bdsim/ler')

    elif (inp.lattice == 'her') & (inp.linear == True):
        a, b = pybdsim.Convert.MadxTfs2Gmad(inp.tfs_file, '../bdsim/her_linear', linear=True)
    elif (inp.lattice == 'her') & (inp.linear == False):
        a, b = pybdsim.Convert.MadxTfs2Gmad(inp.tfs_file, '../bdsim/her')


# Script Mode ------------------------------------------------------------------
if __name__ == '__main__':
    main()
