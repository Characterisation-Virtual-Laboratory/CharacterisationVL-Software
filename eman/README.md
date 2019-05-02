## Installation README

* Website:  
            https://blake.bcm.edu/emanwiki/EMAN2
* Source:   
            https://cryoem.bcm.edu/cryoem/downloads/view_eman2_versions
* Licence:  
            GPL licensed as per the EMAN2 wiki page - http://moinmo.in/GPL
* Run:      
            singularity exec --nv imageFileName.simg e2proc2d.py --help

* Test:     

            singularity exec --nv imageFileName.simg vglrun e2version.py
            singularity exec --nv imageFileName.simg vglrun e2speedtest.py
            singularity exec --nv imageFileName.simg vglrun e2display.py
            singularity exec --nv imageFileName.simg vglrun e2proc2d.py :64:64:1 test.hdf --process mask.sharp:outer_radius=24
            singularity exec --nv imageFileName.simg vglrun e2display.py test.hdf
