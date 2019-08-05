## Installation README

* Website:  
            https://www3.mrc-lmb.cam.ac.uk/relion/

            This container is build around Relion 3.0.7 but also includes  
            MotionCor2 v1.2.6, Gctf v1.06, Ctffind v4.1.13 and Resmap 1.1.4

* Source:   
            https://github.com/3dem/relion

* Licence:  
            Relion - GPLv2, as mentioned on the website.
            Resmap - CC Attribution-NonCommercial-NoDerivs CC BY-NC-ND License - https://creativecommons.org/licenses/by-nc-nd/3.0/ as mentioned on the website.

* Prerequisites:
            This container recipe was constructed using HPCCM - please refer to https://github.com/NVIDIA/hpc-container-maker for details on installation.

            To build the recipe using HPCCM:
            hpccm --recipe relion_3.0_staged.py --format singularity --singularity-version 3.2 > relion_3.0.7.def

            Due to software licensing, MotionCor2 v1.2.6 needs to be downloaded from https://msg.ucsf.edu/software and placed in the same folder as the recipe.

            Singularity >= v3.2.0 is required to build this container. This is due to the use of a multi-stage build. (https://sylabs.io/singularity/)

* Run:      
            singularity exec imageFileName.simg relion

* Test:     
            singularity exec imageFileName.simg relion

* Examples:
            Refer to the Relion website to access the Relion tutorial documentation.
