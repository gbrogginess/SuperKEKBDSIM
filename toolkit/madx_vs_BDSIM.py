import pybdsim 
from generic_parser import EntryPointParameters, entrypoint


# Script arguments -------------------------------------------------------------
def get_params():
    params = EntryPointParameters()
    params.add_parameter(
        name="lattice",
        type=str,
        required=True,
        help="SuperKEKB lattice: ler or her",
    )
    params.add_parameter(
        name="bdsim_optics_file",
        type=str,
        required=True,
        help="Path to the BDSIM optics file to be compared with the MAD-X twiss",
    )

    return params


# Entrypoint -------------------------------------------------------------------
@entrypoint(get_params(), strict=True)
def main(inp):

    if (inp.lattice == 'ler'):
        pybdsim.Compare.MadxVsBDSIM('../madx_twiss/twiss_ler_1707_80_1_simple.tfs', inp.bdsim_optics_file)
    elif (inp.lattice == 'her'):
        pybdsim.Compare.MadxVsBDSIM('../madx_twiss/twiss_her_5781_60_1_simple.tfs', inp.bdsim_optics_file)


# Script Mode ------------------------------------------------------------------
if __name__ == '__main__':
    main()