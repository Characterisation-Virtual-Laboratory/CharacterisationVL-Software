## Installation README

* Website:  
            http://www.mrtrix.org/
* Source:   
            https://github.com/MRtrix3/mrtrix3

* Licence:  
            Mozilla Public License Version 2.0: https://mrtrix.readthedocs.io/en/latest/installation/before_install.html?highlight=license#license

* Notes:
            This software container also includes a build of ANTs and FSL.
            Some of the MRTRIX commands rely on ANTs and FSL to execute.
            https://github.com/ANTsX/ANTs
            https://fsl.fmrib.ox.ac.uk

* Prerequisites:
            Due to software licensing requirements of FSL, please obtain a copy of
            "fslinstaller.py" from  https://fsl.fmrib.ox.ac.uk/fsldownloads_registration
            in order to build this container.
* Run:      
            singularity exec imageFileName.simg dwifslpreproc

* Test:     
            singularity exec imageFileName.simg dwifslpreproc

* Examples:
            Getting started with MRTRIX  - https://mrtrix.readthedocs.io/en/latest/getting_started/beginner_dwi_tutorial.html
