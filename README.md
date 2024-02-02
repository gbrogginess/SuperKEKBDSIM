# SuperKEKBDSIM

Repository containing the inputs and the scripts for generating a SuperKEKB BDSIM model starting from MAD-X twiss tables. The repository also contains a script for validating the generated BDSIM model by comparing quantities of interest (e.g., optics functions) with the starting MAD-X twiss table.

The ```madx_twiss``` directory contains MAD-X twiss tables for SuperKEKB LER and HER. These twiss tables have been produced as explained in the following repository: https://gitlab.cern.ch/gbroggi/skekb_to_madxsuite (see forBDSIM_conversion branch). 

With the ```tfs_to_gmad.py``` script in the ```toolkit``` directory, it is possible to generate a SuperKEKB BDSIM model (.gmad format) with a MAD-X .tfs file given as input. The .gmad files produced by this script are written in the ```bdsim``` directory.

Running the 'main' .gmad script produced by the ```tfs_to_gmad.py``` script with BDSIM:

```bdsim --file=main_script.gmad --batch --ngenerate={n_particles} --outfile=output_file_name```

one gets a bdsim output file ```output_file_name.root```.

It is then possible to evaluate the optics running the command:

```rebdsimOptics output_file_name.root optics_file_name.root```.

This produces a BDSIM optics file ```optics_file_name.root```.

One can then compare the MAD-X and BDSIM optics running the ```madx_vs_BDSIM.py``` script in the ```toolkit``` directory. The outcome of the comparison is written in the same location where the BDSIM optics file is located as a .pdf file ```optics_file_name.pdf```.